"""trt_ssd.py

This script demonstrates how to do real-time object detection with
TensorRT optimized Single-Shot Multibox Detector (SSD) engine.
"""


import sys
import time
import argparse
import threading

import cv2
import pycuda.autoinit  # This is needed for initializing CUDA driver

from utils.ssd_classes import get_cls_dict
from utils.ssd import TrtSSD
from utils.display import open_window, set_display, show_fps
from utils.visualization import BBoxVisualization

class Range(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __eq__(self, other):
        return self.start <= other <= self.end

WINDOW_NAME = 'Thermal Camera Detection'

NETWORK_INPUT_SIZE = (300, 300)

VIDEO_DEVICES = [
    '/dev/video0',
    '/dev/video1',
    '/dev/video2',
]
SUPPORTED_MODELS = [
    'ssd_mobilenet_v2_coco',
    'ssd_mobilenet_v2_thermal',
]

TESTING_PATH = './testing/'

def parse_args():
    """Parse input arguments."""
    desc = ('Capture and display live camera video, while doing '
            'real-time object detection with TensorRT optimized '
            'SSD model on Jetson')

    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--model',     dest='model',       type=str,   default='ssd_mobilenet_v2_thermal',choices=SUPPORTED_MODELS)
    parser.add_argument('--model_path',dest='model_path',  type=str )
    parser.add_argument('--video',     dest='video',       type=str,   default='/dev/video0', choices=VIDEO_DEVICES) 
    parser.add_argument('--width',     dest='image_width', type=int,   default=640) # This is the resolution of the thermal camera
    parser.add_argument('--height',    dest='image_height',type=int,   default=512)
    parser.add_argument('--conf_th',   dest='conf_th',     type=float, default=0.5, choices=[Range(0,1)]) 
    parser.add_argument('--testing',   dest='testing',     type=bool,  default=False) 

    args = parser.parse_args()
    return args


def grab_img(cam):

    global img

    global thread_running

    while thread_running:
        _, img = cam.read()
        if img is None:
            logging.warning('grab_img(): cap.read() returns None...')
            break


def loop_and_detect(cam, trt_ssd, conf_th, vis, testing):
    """Continuously capture images from camera and do object detection.

    # Arguments
      cam: the camera instance (video source).
      trt_ssd: the TRT SSD object detector instance.
      conf_th: confidence/score threshold for object detection.
      vis: for visualization.
    """
    global img

    full_scrn = False
    i = 0
    fps = 0.0

    width  = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    while True:
        if cv2.getWindowProperty(WINDOW_NAME, 0) < 0:
            break

        tic = time.time()

        if img is not None:

            boxes, confs, clss = trt_ssd.detect(img, conf_th)
            toc = time.time()

            img = vis.draw_bboxes(img, boxes, confs, clss)
            img = show_fps(img, fps)
            cv2.imshow(WINDOW_NAME, img)

            #Store the result of inference for later verification
            if testing == True:
                cv2.imwrite(TESTING_PATH + 'img{}.jpeg'.format(i),img)
                i = i + 1

            #calculate the FPS
            fps = 1.0 / (toc - tic)

        else:
            print("[ERROR] - FRAME CAPTURE")

        key = cv2.waitKey(1)
        if key == 27:  # ESC key: quit program
            break
        elif key == ord('F') or key == ord('f'):  # Toggle fullscreen
            full_scrn = not full_scrn
            set_display(WINDOW_NAME, full_scrn)


def main():

    args = parse_args()

    #Get the Class Labels
    cls_dict = get_cls_dict(args.model.split('_')[-1])

    #Load the TRT Engine from file
    trt_ssd = TrtSSD(args.model, args.model_path, NETWORK_INPUT_SIZE)
    
    open_window(WINDOW_NAME, args.image_width, args.image_height,'Camera TensorRT SSD Demo for Jetson')
   
    vis = BBoxVisualization(cls_dict)
 
    #Open camera device
    gst_str = ('v4l2src device=/dev/video{} ! '
                   'video/x-raw, width=(int){}, height=(int){} ! '
                   'videoconvert ! appsink').format(args.video[-1], args.image_width, args.image_height)
    
    cam = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)

    #Start the Thread to capture images
    global thread_running

    thread_running = True

    thread = threading.Thread(target=grab_img, args=(cam,))
    thread.start()

    #Start detection
    loop_and_detect(cam, trt_ssd, args.conf_th, vis, args.testing)

    #Stop the Thread to capture images
    thread_running = False
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

"""trt_ssd.py

This script demonstrates how to do real-time object detection with
TensorRT optimized Single-Shot Multibox Detector (SSD) engine.
"""


import sys
import time
import argparse

import cv2
import pycuda.autoinit  # This is needed for initializing CUDA driver

from utils.ssd_classes import get_cls_dict
from utils.ssd import TrtSSD
from utils.camera import add_camera_args, Camera
from utils.display import open_window, set_display, show_fps
from utils.visualization import BBoxVisualization


class Range(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __eq__(self, other):
        return self.start <= other <= self.end

TESTING_PATH = './testing/'
WINDOW_NAME = 'TrtSsdDemo'
NETWORK_INPUT_SIZE = (300, 300)

SUPPORTED_MODELS = [

    'ssd_mobilenet_v2_coco',
    'ssd_mobilenet_v2_thermal',
]


def parse_args():
    """Parse input arguments."""
    desc = ('Capture and display live camera video, while doing '
            'real-time object detection with TensorRT optimized '
            'SSD model on Jetson')
    parser = argparse.ArgumentParser(description=desc)
    parser = add_camera_args(parser)
    parser.add_argument('--model', type=str, default='ssd_mobilenet_v2_thermal',choices=SUPPORTED_MODELS)
    parser.add_argument('--conf_th',   dest='conf_th',     type=float, default=0.6, choices=[Range(0,1)]) 
    parser.add_argument('--model_path',dest='model_path',  type=str )
    parser.add_argument('--testing',   dest='testing',     type=bool,  default=False) 
    args = parser.parse_args()
    return args


def loop_and_detect(cam, trt_ssd, conf_th, vis, testing):
    """Continuously capture images from camera and do object detection.

    # Arguments
      cam: the camera instance (video source).
      trt_ssd: the TRT SSD object detector instance.
      conf_th: confidence/score threshold for object detection.
      vis: for visualization.
    """
    i = 0
    full_scrn = False
    fps = 0.0
    #tic = time.time()
    while True:
        if cv2.getWindowProperty(WINDOW_NAME, 0) < 0:
            break
        tic = time.time()
        img = cam.read()
        if img is not None:
            boxes, confs, clss = trt_ssd.detect(img, conf_th)
            toc = time.time()
            img = vis.draw_bboxes(img, boxes, confs, clss)
            img = show_fps(img, fps)
            cv2.imshow(WINDOW_NAME, img)

            curr_fps = 1.0 / (toc - tic)
            # calculate an exponentially decaying average of fps number
            fps = curr_fps if fps == 0.0 else (fps*0.95 + curr_fps*0.05)
            #tic = toc
            #Store the result of inference for later verification
            if testing == True:
                cv2.imwrite(TESTING_PATH + 'img{}.jpeg'.format(i),img)
                i = i + 1

        key = cv2.waitKey(1)
        if key == 27:  # ESC key: quit program
            break
        elif key == ord('F') or key == ord('f'):  # Toggle fullscreen
            full_scrn = not full_scrn
            set_display(WINDOW_NAME, full_scrn)


def main():
    args = parse_args()
    cam = Camera(args)
    cam.open()
    if not cam.is_opened:
        sys.exit('Failed to open camera!')

    cls_dict = get_cls_dict(args.model.split('_')[-1])
    trt_ssd = TrtSSD(args.model, args.model_path, NETWORK_INPUT_SIZE)

    cam.start()
    open_window(WINDOW_NAME, args.image_width, args.image_height,
                'Camera TensorRT SSD Demo for Jetson')
    vis = BBoxVisualization(cls_dict)
    loop_and_detect(cam, trt_ssd, args.conf_th, vis, args.testing)

    cam.stop()
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

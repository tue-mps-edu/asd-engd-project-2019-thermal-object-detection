'''ssd_utils.py
'''


import numpy as np
import cv2
import tensorflow as tf
import tensorflow.contrib.tensorrt as trt


def read_label_map(path_to_labels, num_classes):
    """Read from the label map file and return a class dictionary which
    maps class id (int) to the corresponding display name (string).

    Reference:
    https://github.com/tensorflow/models/blob/master/research/object_detection/object_detection_tutorial.ipynb
    """
    from object_detection.utils import label_map_util

    label_map = label_map_util.load_labelmap(path_to_labels)
    categories = label_map_util.convert_label_map_to_categories(
        label_map, max_num_classes=num_classes, use_display_name=True)
    # We do `x['id']-1` below, because 'class' output of the object
    # detection model is 0-based, while class ids in the label map
    # is 1-based.
    return {int(x['id'])-1: x['name'] for x in categories}


def build_trt_pb(model_name, pb_path, download_dir='data'):
    """Build TRT model from the original TF model, and save the graph
    into a pb file for faster access in the future.

    The code was mostly taken from the following example by NVIDIA.
    https://github.com/NVIDIA-Jetson/tf_trt_models/blob/master/examples/detection/detection.ipynb

    Note 'max_batch_size' might need to be set to 4, reference:
    https://devtalk.nvidia.com/default/topic/1036906/tensorrt/cudnnfusedconvactlayer-cpp-64-cuda-error-in-createfiltertexturefused-11/post/5270634/#5270634
    """
    from tf_trt_models.detection import download_detection_model
    from tf_trt_models.detection import build_detection_graph
    from utils.egohands_models import get_egohands_model

    if 'coco' in model_name:
        config_path, checkpoint_path = \
            download_detection_model(model_name, download_dir)
    else:
        config_path, checkpoint_path = \
            get_egohands_model(model_name)
    frozen_graph_def, input_names, output_names = build_detection_graph(
        config=config_path,
        checkpoint=checkpoint_path
    )
    assert input_names[0] == 'input'
    assert 'boxes' in output_names
    assert 'classes' in output_names
    assert 'scores' in output_names
    trt_graph_def = trt.create_inference_graph(
        input_graph_def=frozen_graph_def,
        outputs=output_names,
        max_batch_size=1,
        max_workspace_size_bytes=1 << 26,
        precision_mode='FP16',
        minimum_segment_size=50
    )
    with open(pb_path, 'wb') as pf:
        pf.write(trt_graph_def.SerializeToString())


def load_trt_pb(pb_path):
    """Load the TRT graph from the pre-build pb file."""
    trt_graph_def = tf.GraphDef()
    with tf.gfile.GFile(pb_path, 'rb') as pf:
        trt_graph_def.ParseFromString(pf.read())
    # force CPU device placement for NMS ops
    for node in trt_graph_def.node:
        if 'NonMaxSuppression' in node.name:
            node.device = '/device:CPU:0'
    with tf.Graph().as_default() as trt_graph:
        tf.import_graph_def(trt_graph_def, name='')
    return trt_graph


def write_graph_tensorboard(sess, log_path):
    """Write graph summary to log_path, so TensorBoard could display it."""
    writer = tf.summary.FileWriter(log_path)
    writer.add_graph(sess.graph)
    writer.flush()
    writer.close()


def preprocess(src, shape=(300, 300)):
    """Preprocess input image for the TF-TRT object detection model."""
    img = cv2.resize(src, shape)
    img = img.astype(np.uint8)
    # BGR to RGB
    img = img[..., ::-1]
    return img


def postprocess(img, boxes, scores, classes, conf_th):
    """Postprocess ouput of the TF-TRT object detector."""
    h, w, _ = img.shape
    out_box = boxes[0] * np.array([h, w, h, w])
    out_box = out_box.astype(np.int32)
    out_conf = scores[0]
    out_cls = classes[0].astype(np.int32)

    # only return bboxes with confidence score above threshold
    mask = np.where(out_conf >= conf_th)
    return (out_box[mask], out_conf[mask], out_cls[mask])


def detect(origimg, tf_sess, conf_th):
    """Do object detection over 1 image."""
    tf_input = tf_sess.graph.get_tensor_by_name('input:0')
    tf_scores = tf_sess.graph.get_tensor_by_name('scores:0')
    tf_boxes = tf_sess.graph.get_tensor_by_name('boxes:0')
    tf_classes = tf_sess.graph.get_tensor_by_name('classes:0')

    img = preprocess(origimg)
    scores, boxes, classes = tf_sess.run(
        [tf_scores, tf_boxes, tf_classes],
        feed_dict={tf_input: img[None, ...]})
    box, conf, cls = postprocess(origimg, boxes, scores, classes, conf_th)
    return (box, conf, cls)

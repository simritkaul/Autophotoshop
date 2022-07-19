from pixellib.instance import instance_segmentation
import os
import cv2
import numpy as np
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

def bboxFinder(imagePath):
  segmentation_model = instance_segmentation()
  segmentation_model.load_model('mask_rcnn_coco.h5')

  """ Read the image """
  # image = cv2.imread(imagePath, cv2.IMREAD_COLOR)

  target_classes = segmentation_model.select_target_classes(person=True)

  # segmentation_model.segmentImage(imagePath, segment_target_classes= target_classes, show_bboxes= True, extract_segmented_objects= True, save_extracted_objects=True)
  seg_mask, res = segmentation_model.segmentImage(imagePath, segment_target_classes= target_classes, show_bboxes= True)
  # img = res[1]
  # mask = seg_mask['masks']
  bbox = seg_mask['rois']

  print('Boundary Box Done')

  return bbox[0][0], bbox[0][1], bbox[0][2], bbox[0][3] 
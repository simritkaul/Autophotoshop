import cv2
import os

def cropImage(imagePath, name, x, y, w, h):
  img = cv2.imread(imagePath, cv2.IMREAD_COLOR)
  cv2.imwrite(f'remove_bg\{name}-seg-crop.png', img[x:w, y:h])
  os.remove(imagePath)
  print('Segment Crop Done')
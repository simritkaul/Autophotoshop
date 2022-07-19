from bboxFinder import bboxFinder
from transparent import convertImageBG
from watercolour import watercolourEffect
from subjectExtractor import subjectExtractor
from cropImage import cropImage
from bgChanger import background_changer
import os

pos_w = int(input('Enter x position: '))
pos_h = int(input('Enter y position: '))

scale = float(input('Enter the scale factor (0.5 means half, 4 means four times): '))

def create_dir(path):
  if not os.path.exists(path):
    os.makedirs(path)

""" Load the dataset """
imageList = os.listdir('images/subject/')

currPath = os.getcwd()
imagePath = os.path.join(currPath, f'images\subject\{imageList[0]}')

""" Extracting name """
name = imageList[0].split("/")[-1].split(".")[0]

create_dir('remove_bg')

subjectExtractor(imagePath, name)
x,y,w,h = bboxFinder(imagePath)
cropImage(f'remove_bg\{name}-segment.png', name, x, y, w, h)
watercolourEffect(name)
convertImageBG(f'remove_bg\{name}-watercolor.png', f'remove_bg\{name}-transparent.png')
background_changer(f'remove_bg\{name}-transparent.png', name, pos_w, pos_h, scale)



#!/usr/bin/env python
# Computer Science 685 Assignment 3
# Paul McKerley (G00616949)

import cv2
import pdb
import sys

def main(image_file_name):
    original   = cv2.imread(image_file_name)
    gray       = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)

    gray_name = image_file_name.replace('.png', '_gray.png')
    cv2.imwrite(gray_name, gray)

    thresh_name = image_file_name.replace('.png', '_thresh.png')

    cv2.imwrite(thresh_name, thresh)


if __name__=='__main__':
    main(sys.argv[1])

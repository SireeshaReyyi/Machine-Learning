# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 15:25:27 2019

@author: apssdc
"""

import cv2
img = cv2.imread('C:\\Users\\apssdc\\Pictures\\Screenshots\\Screenshot (1).png',0)
cv2.imshow("Window",img)
cv2.waitKey(1000000)
cv2.destroyAllWindows()
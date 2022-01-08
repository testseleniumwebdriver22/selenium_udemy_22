# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 13:24:13 2021

@author: luca
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os, random
import cv2
import numpy as np
import math


class Image_rec:
    def __init__(self):
        image = cv2.imread('screenshot.png')
        
        original = image.copy()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        lower_left_line = np.array([22, 93, 0], dtype="uint8")
        upper_left_line = np.array([25, 255, 255], dtype="uint8")
        mask_left_line = cv2.inRange(image, lower_left_line, upper_left_line)
        
        
        lower_right_line = np.array([10, 17, 73], dtype="uint8")
        upper_right_line = np.array([130, 130, 120], dtype="uint8")
        mask_right_line = cv2.inRange(original, lower_right_line, upper_right_line)
        
        thresh_left_line = cv2.threshold(mask_left_line, 0, 255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        
        thresh_right_line = cv2.threshold(mask_right_line, 0, 255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        
        
        # cv2.imshow('right contours',thresh_right_line)
        # cv2.imshow('left contours',thresh_left_line)
                
        edges = cv2.Canny(thresh_right_line,50,150,apertureSize = 3)
        # cv2.imshow('edges',edges)
            
        
        minLineLength=12
        lines_r = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=12,lines=np.array([]), minLineLength=minLineLength,maxLineGap=5)
        print("line r:"+str(lines_r))
        
        
        if lines_r is None:
            lines_r=np.array([[[120, 0, 0], [120, 0, 0]]], np.int32)

        if lines_r is not None:
          a,b,c = lines_r.shape
          print("a,b,c="+str(a)+" "+str(b)+" "+str(c))
         
          for i in range(a):
            cv2.line(original, (lines_r[i][0][0], lines_r[i][0][1]), (lines_r[i][0][2], lines_r[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)
        
        
        edges = cv2.Canny(thresh_left_line,50,150,apertureSize = 3)
        minLineLength=17
        
        lines_l = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=25,lines=np.array([]), minLineLength=minLineLength,maxLineGap=20)
        
        
        if lines_l is None:
            lines_l=np.array([[[0, 0, 0], [0, 0, 0]]], np.int32)
            
        if lines_l is not None:
         a,b,c = lines_l.shape
        
         for i in range(a):
            cv2.line(original, (lines_l[i][0][0], lines_l[i][0][1]), (lines_l[i][0][2], lines_l[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)
        
        
        #cv2.imshow('original', original)
        
        
        # cv2.destroyWindow('original')
        # cv2.destroyWindow('left contours')
        # cv2.destroyWindow('right contours')
        # cv2.destroyWindow('edges')

        lines_l_filtered=[]   #filter only vertical/horizontal lines
        lines_r_filtered=[]
        lines_r_filtered_x=[]
        lines_l_filtered_x=[]
        
        if (len(lines_r))>0:
         a,b,c = lines_r.shape
        
         for i in range(a):
            
            if (abs(lines_r[i][0][0]-lines_r[i][0][2])<2 or abs(lines_r[i][0][1]-lines_r[i][0][3])<2) and lines_r[i][0][0]>70 :
                    lines_r_filtered.append(lines_r[i][0])
                    lines_r_filtered_x.append(lines_r[i][0][0])
        
        if (len(lines_l))>0:
         a,b,c = lines_l.shape
        
         for i in range(a):
            
            if (abs(lines_l[i][0][0]-lines_l[i][0][2])<2 or abs(lines_l[i][0][1]-lines_l[i][0][3])<2) and lines_l[i][0][0]<70 :
                    lines_l_filtered.append(lines_l[i][0])
                    lines_l_filtered_x.append(lines_l[i][0][0])
        
        
        if (len(lines_l)>0):
         a,b,c = lines_l.shape
         for i in range(a):
            if abs((lines_l[i][0][0]-lines_l[i][0][2])<2 or abs(lines_l[i][0][1]-lines_l[i][0][3])<2):
                    lines_l_filtered.append(lines_l[i][0])
        
        print("\n\nlines_l_filtered:\n")
        if (len(lines_l_filtered)>0):
         for i in range(len(lines_l_filtered)):
        
            print(str(lines_l_filtered[i])+"\n")
            
        print("\nlines_r_filtered_x"+str(lines_r_filtered_x))
        print("\n\nlines_r_filtered:\n")
        if (len(lines_r_filtered)>0):
         for i in range(len(lines_r_filtered)):
        
            print(str(lines_r_filtered[i])+"\n")
        
        
         
        # cv2.imshow('original', original)
        # cv2.waitKey()
        
       
        if len(lines_r_filtered_x)==0 or len(lines_l_filtered_x)==0:
           self.lines_l_filtered_x_min=0
           self.lines_r_filtered_x_min=120       
        else: 
         self.lines_r_filtered_x_min=min(lines_r_filtered_x)
         self.lines_l_filtered_x_min=min(lines_l_filtered_x)
        
        
    def get_slide_quantity(self):     
        return self.lines_r_filtered_x_min-self.lines_l_filtered_x_min
        
#obj=Image_rec()
#print(str(obj.get_slide_quantity()))
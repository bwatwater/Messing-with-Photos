# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:43:18 2019

@author: Bennett
Written to autocrop square photos. Seems to work fairly well if the background is consistent..
"""
import os
from PIL import Image
for filename in os.listdir(r'C:\Users\Bennett\Desktop\swag'):
    im=Image.open(r'C:\Users\Bennett\Desktop\swag\{}'.format(filename))
    for i in range(30):
        try:
            j=i
            im.seek(j)
            pix = im.load()
            white=pix[2543,3295]
            xlimit0=white
            x0=1355
            while xlimit0==white:
                x0-=1
                xlimit0=pix[x0,500]
            ylimit0=white
            y0=1500
            while ylimit0==white:
                y0-=1
                ylimit0=pix[500,y0]
            xlimit1=0
            x1=0
            while xlimit1==white:
                x1+=1
                xlimit1=pix[x1,0]
            y1=0
            ylimit1=0
            while ylimit1==white:
                y1+=1
                ylimit1=pix[500,y1]
            sally=im.crop((x1,y1,x0,y0))
            sally.save('{}_page{}.tif'.format(filename,i))
            print("Saved!")
        except EOFError:
            break


    
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 18:50:25 2019

@author: Bennett
Made for randomizing photos in a slideshow. Takes all the photos
and adds them to an array. Shuffles them and names them integer 
values. 
"""
import os
import random
from PIL import Image
files=[]
for filename in os.listdir(r'C:\Users\Bennett\Desktop\celeboflife'):
    try:
        files.append(Image.open(r'C:\Users\Bennett\Desktop\celeboflife\{}'.format(filename)))
        print('did it')
    except EOFError:
        break
random.shuffle(files)
i=0
for item in files:
    item.save('{}.tif'.format(i))
    print("Saved!")
    i+=1


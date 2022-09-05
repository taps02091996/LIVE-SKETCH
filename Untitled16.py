#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[3]:


pip install cv2module


# In[2]:


import numpy as np


# In[ ]:


def sketch(image):
    img_grey = cv2.cvtColor(image , cv2.COLOR_BGRA2GRAY)
    img_gray_blur = cv2.GaussianBlur(img_grey,(5,5),0)
    canny_edges = cv2.Canny(img_gray_blur,10,70)
    ret,mask = cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY_INV)
    return mask

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    cv2.imshow('Our Live Sketcher',sketch(frame))
    
    if cv2.waitKey(1) == 13:
        break
        
cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:





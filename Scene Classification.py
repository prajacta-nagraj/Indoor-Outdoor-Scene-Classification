#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.models import load_model
model = load_model('firstb_try.h5')


# In[16]:


txt = raw_input("Type image name: ")
import numpy as np
from keras.preprocessing import image
img = image.load_img(txt, target_size=(64, 64))
x = np.expand_dims(image.img_to_array(img), axis=0)
images = np.vstack([x])
classes = model.predict_classes(images, batch_size=10)
if classes==1:
    print 'outdoor'
else:
    print 'indoor'


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


from rembg import remove
from PIL import Image


# In[2]:


#User Car Image
input_path = 'Downloads/Car Image Wb.jpg'
user_car_image = Image.open(input_path)


# In[3]:


output_image = remove(user_car_image)
output_image.show()


# In[4]:


output_path = 'Downloads/car_no_bg.png'
output_image.save(output_path)


# In[7]:



from PIL import Image

def add_new_background(car_image_path, background_image_path, output_path):
    car_image = Image.open(car_image_path).convert("RGBA")
    background_image = Image.open(background_image_path).convert("RGBA")
    
    # Resize the background to match the car image size
    background_image = background_image.resize(car_image.size)
    
    # Combine the car image with the new background
    combined_image = Image.alpha_composite(background_image, car_image)
    combined_image.save(output_path)


# In[8]:


car_image_path = 'Downloads/car_no_bg.png'
background_image_path ='Downloads/RoadImage.jpg'
final_image_path = 'Downloads/final_image.png'


# In[9]:


add_new_background(car_image_path, background_image_path, final_image_path)


# In[10]:


final_image = Image.open(final_image_path)
final_image.show()


# In[ ]:





# In[ ]:





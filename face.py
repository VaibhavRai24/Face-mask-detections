import streamlit as st
import os
from keras.models import load_model
from PIL import Image, ImageOps
import cv2
import numpy as np

# NOW WE ARE GOING TO GIVE THE HEADER
model = load_model(" face mask .h5")

# TREAMLIT UI BASICALLY MAI YHA PE PAGE PE KYA DIKHEGA DEFINE KRUNGA AB
st.header(' Face mask detection ')
st.write('Upload the image to check that wheather the image is in mask or not..')

# NOW WE ARE GOING TO UPLOAD THE IMAGE
uploaded_file = st.file_uploader("Choose an image...", type= ["jpeg", "jpg", "png"])

if uploaded_file is not None:
    # THE IMAGE IS UPLOADED NOW WE ARE GOING TO SHOW IT ON THE PAGE
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    #NOW PREPROCESSING OF THE IMAGE BASICALLY WAHI JO HUMNE MODEL DEVELOP KRTE TIME KIA THA
    img_array = np.array(image)
    image_resized = cv2.resize(img_array, (128,128))
    image_resized = image_resized / 255.0
    image_reshaped = np.expand_dims(image_resized, axis=0)
    
    #NOW WE ARE GOING TO DO THE PREDICTIONS
    
    predictions = model.predict(image_reshaped)
    mask_label = "Given picture is with the mask " if predictions[0][0]> 0.5 else "The given picture is without the mask"
    
    st.write(f"Predictions:{mask_label}")
import streamlit as st
import pandas as pd
import requests
import base64
import base64
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
st.set_page_config('Paddy Disease Prediction')

@st.cache_resource
def load_model():
    return tf.keras.models.load_model('n.keras')
model=load_model()

st.title("Paddy Disease Prediction")

uploaded_file = st.file_uploader("Choose a paddy disease file")
if uploaded_file is not None:
    with st.status(label='predicting',expanded=False) as upt:
        bytes_data = uploaded_file.getvalue()
        format=uploaded_file.name.split('.')[1]
        img=base64.b64encode(bytes_data).decode('utf-8')
        img=base64.b64decode(img)
        with open(f"img.{format}",'wb') as f:
            f.write(img)
        img_path = f'img.{format}'
        img = image.load_img(img_path, target_size=(256, 256))
        img_array = image.img_to_array(img)

        img_array = tf.keras.preprocessing.image.img_to_array(img_array)
        img_array = tf.expand_dims(img_array, 0)
        predictions = model.predict(img_array)
        class_names=['Bacterial leaf blight', 'Brown spot', 'Healthy']
        predicted_class = class_names[np.argmax(predictions[0])]
        confidence = round(100 * (np.max(predictions[0])), 2)
        st.write(predicted_class)
        upt.update(state='complete',expanded=True,label='Predicted')
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Cargar el modelo entrenado
model = tf.keras.models.load_model('flower_classification_model.h5')

st.title("Clasificación de Flores")

# Subir una imagen
uploaded_file = st.file_uploader("Sube una imagen de una flor", type=["jpg", "jpeg", "png"])

# Lista de clases
class_names = ['Daisy', 'Dandelion', 'Rose', 'Sunflower', 'Tulip']

if uploaded_file is not None:
    # Mostrar la imagen cargada
    img = Image.open(uploaded_file)
    st.image(img, caption='Imagen cargada', use_column_width=True)
    
    # Preprocesar la imagen
    img = img.resize((150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    
    # Generar predicción
    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction[0])
    
    # Mostrar la clase predicha
    st.write(f"La imagen es probablemente una {class_names[class_idx]}")

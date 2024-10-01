# Clasificación de Flores con Deep Learning

Este proyecto utiliza un modelo de **Deep Learning** (CNN) para clasificar imágenes de flores en 5 categorías diferentes: **Daisy**, **Dandelion**, **Rose**, **Sunflower** y **Tulip**. La aplicación está construida con **TensorFlow** y **Streamlit**.

## Descripción del Proyecto

Este proyecto clasifica imágenes de flores en cinco categorías diferentes utilizando un modelo de **red neuronal convolucional (CNN)**. La aplicación permite a los usuarios cargar imágenes de flores y obtener una predicción sobre la clase de la flor.

### Dataset

El dataset utilizado es el **Flowers Recognition** de Kaggle, que puedes descargar aquí: [Flowers Recognition Dataset](https://www.kaggle.com/datasets/alxmamaev/flowers-recognition).

### Estructura del Dataset

El dataset debe estar organizado en subcarpetas para cada clase de flor:

```bash
flowers/
    daisy/
    dandelion/
    rose/
    sunflower/
    tulip/
```

### Instalación y ejecución en local.
1. Descargar el dataset de kaggle y dejar la carpeta de imagenes "flowers" dentro del directorio del proyecto
3. Instalar python 3.9
4. Crear el entorno virtual de Python
    ```sh
    python3.9 -m venv venv
    ```
4. Activar el entorno virtual de Python
    ```sh
    source venv/bin/activate
    ```
5. Instalar las dependencias
    ```sh
    pip install -r requirements.txt
    ```
6. Instalar Jupyter Notebook
    ```sh
    pip install notebook
    ```
7. Abrir jupyter
    ```sh
    jupyter notebook
    ```
8. Ejecutar los Notebooks en orden.
9. Generar la imagen de docker
    ```sh
    docker build -t classificacion-dl-image .  
    ```
10. Crear el contenedor de docker
    ```sh
    docker run -p 8501:8501 classificacion-dl-image
    ```
11. Abrir la aplicación en chrome y cargar una imagen (dentro del directorio del proyecto tenemos la imagen "test_image.jpg") para predecir el tipo de imagen.
    [http://localhost:8501](http://localhost:8501)

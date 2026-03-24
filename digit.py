import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# 1. Model load karein (ensure karein ki digit_model.h5 isi folder mein ho)
model = tf.keras.models.load_model("digit_model.h5")

st.title("Handwritten Digit Classifier")

# 2. Image upload karne ka option
uploaded_file = st.file_uploader("Upload Digit Image", type=["png","jpg"])

if uploaded_file is not None:
    # Image processing
    image = Image.open(uploaded_file).convert("L")
    st.image(image, caption="Uploaded Image", width=200)

    image = image.resize((28,28))
    img_array = np.array(image) / 255.0
    img_array = img_array.reshape(1,28,28,1)

    # 3. Prediction dikhayein
    prediction = model.predict(img_array)
    digit = np.argmax(prediction)

    st.success(f"Predicted Digit: {digit}")
# MNIST-Digit-classifier-Project-app

✍️🔢A Deep Learning web application built with TensorFlow and Streamlit that recognizes handwritten digits (0-9) in real-time.

🚀 Live DemoYou can access the live web app here: []


📌 Project OverviewThis project uses a Convolutional Neural Network (CNN) (or Dense Neural Network, depending on your model) trained on the famous MNIST dataset. Users can upload an image of a handwritten digit, and the model will predict the number with high accuracy.

🛠️ FeaturesImage Upload: Support for .png, .jpg, and .jpeg files.Real-time Processing: Uses OpenCV/Pillow to grayscale and resize images to 28 * 28 pixels (MNIST format).Deep Learning Backend: Powered by TensorFlow/Keras.Interactive UI: Clean and simple dashboard built with Streamlit.

📂 Tech StackLanguage: PythonDeep Learning: TensorFlow, KerasImage Processing: Pillow (PIL), NumPyFramework: StreamlitDeployment: Streamlit Community Cloud⚙️ How it WorksInput: User uploads an image of a handwritten digit.Preprocessing: The app converts the image to grayscale, resizes it to 28 * 28, and normalizes pixel values.Inference: The .h5 model processes the image array.Output: The predicted digit is displayed with a confidence score.

👤 Author :Shruti Nath
   First-year B.Tech Student
   Mechanical Engineering
   NIT Durgapur

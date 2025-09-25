**Crop Disease Prediction**

**Overview**

This project is a Crop(Paddy) Disease Prediction System built using Streamlit, designed to help farmers and researchers detect diseases in paddy crops. The application uses a Convolutional Neural Network (CNN) model to classify paddy leaf diseases based on uploaded images.

**Features**

•	User-Friendly Interface: Simple web-based UI for uploading paddy leaf images.

•	Machine Learning Integration: Utilizes CNN for disease detection.

•	Real-Time Prediction: Instantly classifies diseases and provides insights.

•	Data Visualization: Displays disease trends using interactive charts.

•	Local Storage: Stores uploaded images and predictions locally.

•	Cloud Deployment: Easily deployable on Streamlit Cloud, AWS, or GCP.

**Tech Stack**

•	Framework: Streamlit

•	Language: Python

•	Machine Learning: Convolutional Neural Network (CNN) using Keras and TensorFlow

•	Libraries: Pandas, NumPy, Matplotlib, Seaborn

•	Storage: Local storage for images and predictions

**Process**

•	Data Collection: Gather paddy leaf images with labeled diseases.

•	Preprocessing: Resize images, normalize pixel values, and augment data if necessary.

•	Model Training: Train a CNN model using Keras and TensorFlow.

•	Model Evaluation: Test the model's accuracy using validation datasets.

•	Deployment: Integrate the trained model into a Streamlit application.

•	User Interaction: Users upload images, and the model predicts the disease.

•	Visualization: Display results and trends using interactive charts.


**Usage**

*Upload an Image*

 •	On the app’s homepage, click the “Upload” button to select a paddy leaf image (JPEG/PNG).
 
 •	The uploaded image will be displayed on the screen for confirmation.

*Model Prediction*

 •	Once uploaded, the CNN model (trained using Keras & TensorFlow) automatically processes the image.
 
 •	The model classifies whether the paddy leaf is healthy or has a specific disease (e.g., blast, blight, brown spot).

*View Results*

 •	The predicted disease name (or “Healthy”) is shown clearly on the screen.
 
 •	A confidence score (e.g., 92%) is displayed, showing how certain the model is about its prediction.

*Save/Download Results*

 •	Users can choose to save predictions locally or download them for later reference.

**Deployment on Streamlit Cloud**

•	Push your project code, requirements file (requirements.txt), and trained model to a GitHub repository.

•	Go to Streamlit Community Cloud and log in with GitHub.

•	Select your repository, branch, and main app file.

•	Configure environment dependencies (make sure tensorflow, keras, pandas, etc. are in requirements.txt).

•	Click Deploy. Streamlit Cloud will build your app and provide a shareable URL.

 

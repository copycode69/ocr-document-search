# OCR and Document Search Web Application

This project is a web-based prototype that performs Optical Character Recognition (OCR) on uploaded images with text in both Hindi and English. It also features a keyword search within the extracted text.

## Features

- Upload an image containing text in Hindi and/or English.
- Extract text from the image using OCR.
- Perform keyword search within the extracted text.
- Web app interface built using Streamlit.

## Prerequisites

Before running the project, ensure you have the following installed on your system:

- Python 3.7 or above
- pip (Python package installer)
- (Optional) Virtual environment tool (virtualenv or venv)

## Setting Up the Environment

### Step 1: Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone <REPO_URL>
cd ocr-document-search
```

## Setting Up the Environment

### Step 2: Create a Virtual Environment (Recommended)

It's recommended to use a virtual environment to avoid conflicts with system-wide packages. Follow the instructions based on your operating system:

#### Windows

```bash
python -m venv ocr-app-env
ocr-app-env\Scripts\activate
```
#### macOS/Linux

```bash
python3 -m venv ocr-app-env
source ocr-app-env/bin/activate
```

## Step 3: Install Dependencies

Once your virtual environment is activated, install the required dependencies by running:

```bash
pip install -r requirements.txt
```
#### The requirements.txt file should contain:
```
streamlit
easyocr
torch
transformers
Pillow
```

#### If you run into issues with installing torch, refer to the official PyTorch installation guide.

# Running the Web Application Locally
### Step 1: Run the Streamlit Application
#### After installing the dependencies, you can run the application using Streamlit:
```
streamlit run app.py
```
This will launch a local development server. You can access the application by navigating to http://localhost:8501 in your web browser.

### Step 2: Using the Application
- Go to the local URL (http://localhost:8501).
- Upload an image containing text in Hindi and/or English.
- The OCR will extract text from the image and display it.
- Use the search functionality to find specific keywords in the extracted text.

# Deployment Process
To make the web application accessible online, you can deploy it using a cloud service like Streamlit Sharing or a platform of your choice. Here’s how you can do it:

## Step 1: Push the Code to GitHub
Ensure your project is pushed to a GitHub repository. If you haven't already, create a new GitHub repository and upload your project files.

```
git init
git remote add origin <GITHUB_REPO_URL>
git add .
git commit -m "Initial commit"
git push -u origin main
```

### Step 2: Deploy on Streamlit Sharing
- Visit Streamlit Sharing.
- Log in with your GitHub account.
- Select the repository containing your project.
- Choose the app.py file as the entry point.
- Streamlit will automatically deploy the application and provide you with a public URL.

# Project Structure
```
ocr-document-search/
│
├── app.py                    # Main Streamlit app file
├── requirements.txt           # List of dependencies
└── README.md                  # Project documentation
```
# Additional Notes
- This application uses the easyocr library to perform OCR, which supports both Hindi and English text.
- The web interface is built using Streamlit, which provides a fast and easy way to create web applications with Python.
- The application is designed to be lightweight and simple, demonstrating the core functionality of OCR and keyword search.

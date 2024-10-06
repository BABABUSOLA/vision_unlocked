Below is a detailed `README.md` for your Flask-based image and question processing API:

---

# Vision Chat API

## Prerequisites

- Python 3.9 or higher
- Google Cloud Platform account with a **Storage Bucket** created
- Google Cloud SDK installed and authenticated
- Service account credentials with access to your GCS bucket
- Ollama account for interacting with the LLaVA model
- To configure gogle storage as public:
1. Make the Object Public:
You need to make the object (the image file) accessible to everyone. There are two main ways to do this:

Option 1: Via Google Cloud Console
Go to the Google Cloud Console.
Navigate to Cloud Storage and find your bucket.
Click on your bucket to view the objects inside it.
Select the specific object (image) you want to make public.
In the object details, click on Edit Permissions.
Add a new Principal:
Under New Principals, type allUsers.
Under Role, select Storage Object Viewer.
Save the changes.
This will make the file publicly accessible, and anyone with the URL will be able to access it.

## Overview

Vision Chat API is a Flask-based web service that allows users to upload an image and ask a question about the image. The API processes the image and the question using the **Ollama llava** model to generate a relevant response. The service is built with modularity in mind and separates concerns into controllers, services, and route definitions.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Upload an image and ask a question.
- Leverages the **Ollama llava** model to answer questions related to the image.
- Modular structure for easy extension and maintainability.
- Error handling and input validation for robustness.

---

## Project Structure

The project is structured to keep the code modular and maintainable. Below is the directory structure:

```bash
/vision-chat-app
│
├── vision.py                     #Main entry point for running the Flask app
├── controllers
│   └── vision_chat_controller.py # Handles routes and request processing
├── services
│   └── vision_chat_service.py   # Business logic for image processing and question answering
│   └── google_cloud_storage_service.py
├── requirements.txt
├── Dockerfile
└── README.md

```

- **`app.py`**: The entry point for the Flask app that registers blueprints and starts the server.
- **`controllers/`**: Contains route definitions and request handlers.
- **`services/`**: Contains the logic for interacting with the Ollama model and answering the user's question.
- **`uploads/`**: Directory where images uploaded by the user are stored.
- **`models/`**: Reserved for future data models.

---

## Installation

To get started with the Vision Chat API, follow these steps:

### Prerequisites

- Python 3.x
- Pip (Python package manager)
- [Ollama CLI](https://ollama.com/) (Make sure it's installed and accessible from your command line)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/vision-chat-api.git
   cd vision-chat-api
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app:**

   ```bash
   python app.py
   ```

   The application will start on `http://localhost:8000`.

---

## Usage

### Testing via Postman or `curl`

1. **POST request to the `/vision-chat` endpoint:**

   You can upload an image and ask a question in the same request. The server will respond with a generated answer based on the image.

   - **Example using `curl`:**

     ```bash
     curl -X POST http://localhost:8000/vision-chat \
          -F "image=@path/to/image.jpg" \
          -F "question=What is shown in this image?"
     ```

   - **Example using Postman:**
     - Set the method to `POST`.
     - Set the URL to `http://localhost:8000/vision-chat`.
     - In the "Body" tab, choose `form-data`.
     - Add two fields:
       - `image`: Choose an image file.
       - `question`: Type your question as plain text.
     - Send the request.

2. **Response:**

   The API will respond with a JSON object that contains the result of the image and question analysis.

   ```json
   {
       "response": "This image contains a cat sitting on a chair."
   }
   ```

---

## API Endpoints

### POST `/vision-chat`

This endpoint handles image uploads and responds with the Ollama model's answer to the user's question.

- **Request Parameters:**
  - `image` (file, required): The image file to analyze.
  - `question` (string, required): The question you want to ask about the image.

- **Response:**
  - `response` (string): The Ollama model's answer to the question.

- **Error Handling:**
  - If the image or question is missing, the server returns a `400 Bad Request` error.
  - If there is an internal error, the server returns a `500 Internal Server Error`.

---

## Environment Variables

You can configure your application using environment variables.

- **`UPLOAD_FOLDER`**: Specifies the directory where uploaded images are stored. By default, it is set to `uploads`.

You can use a `.env` file (along with libraries like `python-dotenv`) for managing environment variables in production environments.

---

## Testing

To run tests for the Vision Chat API:

1. **Ensure you have the required testing libraries** installed. This project is designed for flexibility in testing. You can add test cases using popular libraries like `unittest` or `pytest`.

2. **Run your tests** by simply executing them within your testing framework:

   ```bash
   pytest
   ```

   (Or) run the tests with `unittest`:

   ```bash
   python -m unittest discover
   ```

---

## Contributing

We welcome contributions! Please feel free to submit issues, fork the repository, and open pull requests.

### Steps to Contribute:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---
### Locally run docker
1. docker build -t vision-app .
2. `docker run -p 8080:8080 \
-e GOOGLE_APPLICATION_CREDENTIALS=./serviceAccount.json \
vision-app`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Full `README.md` for Flask-based Vision Chat API project. This file provides detailed information about the project, installation instructions, API usage, and more.
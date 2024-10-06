from flask import Flask
from controllers.vision_controller import vision_chat_bp
import os

# Create the Flask app
app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Register the blueprint for vision routes
app.register_blueprint(vision_chat_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

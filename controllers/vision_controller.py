from flask import Blueprint, request, jsonify, current_app
import os
from services.vision_service import vision_chat

# Create a blueprint for vision-related routes
vision_chat_bp = Blueprint('vision_chat_bp', __name__)

@vision_chat_bp.route('/vision-chat', methods=['POST'])
def vision_chat_endpoint():
    """
    Handle image upload and question, and respond with the processed output.
    """
    # Check if an image and question are provided
    if 'image' not in request.files or 'question' not in request.form:
        return jsonify({'error': 'Image and question are required'}), 400

    image = request.files['image']
    question = request.form['question']

    # Save the uploaded image
    image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image.filename)
    image.save(image_path)

    # Process the image and question
    try:
        response = vision_chat(image_path, question)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

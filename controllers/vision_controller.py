from flask import Blueprint, request, jsonify
from services.vision_service import vision_chat
from services.google_cloud_storage_service import upload_to_gcs

# Create a blueprint for vision-related routes
vision_chat_bp = Blueprint('vision_chat_bp', __name__)

@vision_chat_bp.route('/vision-chat', methods=['POST'])
def vision_chat_endpoint():
    """
    Handle image upload and a question and respond with the answer.

    Returns:
        JSON response with the response content or an error message.
    """
    # Ensure image and question are present in the request
    if 'image' not in request.files or 'question' not in request.form:
        return jsonify({'error': 'Image and question are required'}), 400

    image = request.files['image']
    question = request.form['question']

    print(f"Received image: {image.filename}, question: {question}")    
    # Upload image to Google Cloud Storage
    try:
        image_url = upload_to_gcs(image, image.filename)
        response = vision_chat(image_url, question)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

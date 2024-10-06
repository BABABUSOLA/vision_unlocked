from flask import Flask
from controllers.vision_controller import vision_chat_bp

# Create the Flask app
app = Flask(__name__)

# Register the blueprint for vision routes
app.register_blueprint(vision_chat_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

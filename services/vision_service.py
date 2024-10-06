import requests
from io import BytesIO
from ollama import chat



def download_image(url: str):
    """
    Download the image from the given URL and return a file-like object.
    
    Args:
        url (str): The URL of the image to download.
    
    Returns:
        BytesIO: The image in a file-like object.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        raise Exception(f"Failed to download image from {url}")

def vision_chat(image_url: str, question: str) -> str:
    """
    Process the question and image URL using the Ollama model.

    Args:
        image_url (str): The URL of the uploaded image.
        question (str): The question to ask.

    Returns:
        str: The response content from the model.
    """
    # Download the image from the URL and pass it as a file-like object
    image_file = download_image(image_url)

    # Prepare the prompt with the image URL and question
    prompt = [{'role': 'user', 'content': question, 'images': [image_file]}]
    
    # Call the model and return the response content
    response = chat(model="llava", messages=prompt)
    return response['message']['content']

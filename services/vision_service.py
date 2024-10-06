from ollama import chat

def vision_chat(image_path: str, question: str) -> str:
    """
    Process an image and question with the Ollama model and return the response content.

    Args:
        image_path (str): The path to the image.
        question (str): The question to answer.

    Returns:
        str: The response content.
    """
    prompt = [
        {'role': 'user', 'content': question, 'images': [image_path]}
    ]
    response = chat(model="llava", messages=prompt)
    return response['message']['content']

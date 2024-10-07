# Use an appropriate base image (e.g., Python with dependencies)
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install curl
RUN apt-get update && apt-get install -y curl

# Install Ollama CLI
RUN curl -fsSL https://ollama.com/install.sh | sh

# Pull the required model 'llava' using the Ollama CLI
RUN ollama pull llava

# Copy the application files
COPY . .

# Expose the port that the app will run on
EXPOSE 8080

# Run the application
CMD ["sh", "-c", "ollama serve & python3 vision.py"]
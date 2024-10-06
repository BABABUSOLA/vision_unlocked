from google.cloud import storage
import os

# Initialize the Google Cloud Storage client
storage_client = storage.Client()
bucket_name = 'alx_portfolio_image_to_pdf_converter'  # Replace with your GCP bucket name
bucket = storage_client.bucket(bucket_name)

def upload_to_gcs(file, filename):
    """
    Upload a file to Google Cloud Storage and return its public URL.

    Args:
        file: The file to be uploaded.
        filename: The name of the file to store in the bucket.

    Returns:
        str: The public URL of the uploaded file.
    """
    print(f"Uploading {file} to Google Cloud Storage")
    # Upload the file to the GCS bucket
    blob = bucket.blob(filename)
    print(f"Uploading {blob}")
    blob.upload_from_file(file)

    print(blob.public_url,'the blob public url')
    
    # Make the blob publicly accessible and return the public URL
    return blob.public_url

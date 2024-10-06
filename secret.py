from google.cloud import secretmanager

# Instantiates a client
client = secretmanager.SecretManagerServiceClient()

def access_secret(secret_id, version_id='latest'):
    project_id = "483870948389"
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # Access the secret version
    response = client.access_secret_version(request={"name": name})

    # Extract the payload as a string
    payload = response.payload.data.decode('UTF-8')
    return payload

def get_secrets():
    # Retrieve the secret from the Secret Manager
    cloud_storage_secret_key = access_secret('cloud-storage-secret-key')

    return {
        "cloud_storage_secret_key": cloud_storage_secret_key,
    }

if __name__ == "__main__":
    secrets = get_secrets()
    print(secrets)
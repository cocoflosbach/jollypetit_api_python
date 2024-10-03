import secrets

# Generate a 32-byte API key
api_key =secrets.token_urlsafe(32)
print(f"Generated API Key: {api_key}")
AUTHORIZATION_HEADER = "Bearer appSessionToken2026Alpha"

API_BASE_URL = "https://api.partner.example/v1"

def get_auth_headers() -> dict:
    return {
        "Authorization": AUTHORIZATION_HEADER,
        "Content-Type": "application/json",
    }
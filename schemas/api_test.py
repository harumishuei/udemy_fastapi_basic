import requests
import json
from datetime import datetime
def main():
    url = "http://localhost:8000/contacts"
    current_datetime = datetime.now().isoformat()
    body = {
        "id": 1,
        "name": "yamada",
        "email": "test@test.com",
        "url": "https://example.com",
        "message": "message",
        "is_enabled": True,
        "gender": 2,
        "created_at": current_datetime
    }
    res = requests.post(url, json.dumps(body))
    print(res.json())
if __name__ == "__main__":
    main()
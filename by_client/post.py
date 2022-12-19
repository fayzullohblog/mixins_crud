import requests

data={
        "title": "qavun",
        "content": "qashqadaryo bizda bitda"
    }
endpoint=requests.post('http://127.0.0.1:8000/post/',json=data)

print(endpoint.json())
import requests

response = requests.post(
    "http://localhost:8000/openai/invoke",
     json={'input': 'tell me a 10 words story about zebra'}
)
print (response.text)
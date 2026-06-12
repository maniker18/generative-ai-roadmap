# API Test - Connect to real APIs!

import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()
    print(f"Title: {data['title']}")
    print(f"Body: {data['body']}")
except Exception as e:
    print(f"Error: {e}")
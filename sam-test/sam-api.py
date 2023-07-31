import requests
url = "http://1.14.15.140:7860/sam/heartbeat"
response = requests.get(url)
reply = response.json()

print(reply)
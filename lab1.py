import requests

print(requests.__version__)

result = requests.get("http://google.com/")

print(result.text)
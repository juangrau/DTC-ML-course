import requests

# url = 'http://localhost:9696/predict'
url = 'http://localhost:8080/predict'

data = {'url': 'https://tensorflow.org/images/blogs/serving/cat.jpg'}

result = requests.post(url, json=data).json()
print(result)
import requests

url = 'http://0.0.0.0:8080/2015-03-31/functions/function/invocations'
data = {'url': 'http://bit.ly/mlbookcamp-pants'}

result = requests.post(url, json=data).json()
print(result)
import requests

url = 'http://0.0.0.0:8080/2015-03-31/functions/function/invocations'
data = {'url': 'https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg'}

result = requests.post(url, json=data).json()
print(result)
import requests

customer = {
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 1,
    'monthlycharges': 29.85,
    'totalcharges': 29.85
}

customer

#url = 'http://172.25.212.32:9696/predict'
url = 'http://127.0.0.1:9696/predict'

result = requests.post(url, json=customer).json()
print(result)

if result['churn'] == 1.0:
    print('Sending promotional email to client')
else:
    print('Not Sending promotional email to client')



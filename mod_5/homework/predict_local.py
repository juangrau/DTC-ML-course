import pickle

model_file = 'model1.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)

customer = {'job': 'management', 'duration': 400, 'poutcome': 'success'}

def predict(dv, model, customer):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0,1]
    churn = y_pred >= 0.5

    result = {
        'y_pred': float(y_pred),
        'churn': float(churn)
    }
    
    return result

result = predict(dv, model, customer)
print(result['y_pred'])
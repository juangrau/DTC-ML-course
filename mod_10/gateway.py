import grpc
import tensorflow as tf
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc
import numpy as np
from keras_image_helper import create_preprocessor
import os

from flask import Flask
from flask import request
from flask import jsonify

from proto import np_to_protobuf

host = os.getenv('TF_SERVING_HOST', 'localhost:8500')

channel = grpc.insecure_channel(host)
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
preprocessor = create_preprocessor('xception', target_size=(224, 224))

def prepare_request(X):
    pb_request = predict_pb2.PredictRequest()
    pb_request.model_spec.name = 'resnet'
    pb_request.model_spec.signature_name = 'serving_default'
    pb_request.inputs['input_1'].CopyFrom(np_to_protobuf(X))
    return pb_request

def predict(url):
    #url = 'https://tensorflow.org/images/blogs/serving/cat.jpg'
    X = preprocessor.from_url(url)
    pb_request = prepare_request(X)
    pb_response = stub.Predict(pb_request, timeout=30.0)
    result = prepare_response(pb_response)
    return result

def prepare_response(pb_response):
    result = pb_response.outputs['activation_49'].float_val
    result_dict = {}
    result_dict['index'] = float(np.argmax(result))
    result_dict['prob'] = float(result[np.argmax(result)])
    return result_dict

app = Flask('gateway')

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    data = request.get_json()
    url = data['url']
    result = predict(url)
    return jsonify(result)


if __name__=='__main__':
    url = 'https://tensorflow.org/images/blogs/serving/cat.jpg'
    response = predict(url)
    print(response)
    # app.run(debug=True, host="0.0.0.0", port=9696)



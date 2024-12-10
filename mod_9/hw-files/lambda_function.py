#%%
import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor
from io import BytesIO
from urllib import request
import numpy as np

from PIL import Image

#%%
interpreter = tflite.Interpreter(model_path='model_2024_hairstyle_v2.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

#%%
# url = 'http://bit.ly/mlbookcamp-pants'

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img

def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img


def predict(url):

    img = download_image(url)
    prepared_img = prepare_image(img, (200, 200))
    preprocessed_img = np.array(prepared_img) * (1. / 255)
    
    preprocessor = create_preprocessor('xception', target_size=(200, 200))
    X = preprocessor.from_url(url)
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    float_predictions = preds[0].tolist()

    return float_predictions

def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result



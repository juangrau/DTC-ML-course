FROM tensorflow/serving

COPY resnet /models/resnet

ENV MODEL_NAME="resnet"
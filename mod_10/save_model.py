#%%
import tensorflow as tf
from tensorflow import keras

#%%
model = keras.models.load_model('./terrain_model.h5.keras')

#%%

tf.saved_model.save(model, 'terrain_model')

#%%
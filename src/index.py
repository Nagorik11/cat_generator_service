from flask import Flask
from flask import send_file
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib
from random import randint

app = Flask(__name__)
tf.__version__

matplotlib.use('agg')
imported = tf.saved_model.load("generator_model")

def generate_and_save_images(model, epoch, test_input):
  predictions = model(test_input, training=False)

  fig = plt.figure(figsize=(4,4))

  for i in range(predictions.shape[0]):
      plt.subplot(4, 4, i+1)
      plt.imshow(predictions[i, :, :, 0] * 127.5 + 127.5, cmap='gray')
      plt.axis('off')
  plt.savefig('image_{:04d}.png'.format(epoch))



@app.route('/generate_cats')
def generate_cats():
    
    random_e = randint(1,100)
    gen_seed = tf.random.normal([16, 100])
    generate_and_save_images(imported, random_e, gen_seed)
    return send_file('image_{:04d}.png'.format(random_e), mimetype='image/png')

app.run(host='0.0.0.0')
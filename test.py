import tensorflow as tf
import numpy
import random

model:tf.keras.Model = tf.keras.models.load_model(r"C:\Users\timh\Downloads\tah\nn\model")


for x in range(0, 10):
    i1 = random.randint(0, 100)
    i2 = random.randint(0, 100)
    inputs = numpy.array([[i1, i2]])
    vals = model.predict(inputs, verbose=False)
    correct = i1 * i2
    print(str(i1) + " x " + str(i2) + " = " + str(vals[0][0]) + " (correct: " + str(correct) + ")")
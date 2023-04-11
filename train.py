import tensorflow as tf
import numpy
import random



inputs:tf.keras.layers.Dense = tf.keras.layers.Input(2)
h1:tf.keras.layers.Dense = tf.keras.layers.Dense(30, "relu")
h2:tf.keras.layers.Dense = tf.keras.layers.Dense(20, "relu")
h3:tf.keras.layers.Dense = tf.keras.layers.Dense(10, "relu")
h4:tf.keras.layers.Dense = tf.keras.layers.Dense(5, "relu")
outputs:tf.keras.layers.Dense = tf.keras.layers.Dense(1)

model = tf.keras.Sequential()
model.add(inputs)
model.add(h1)
model.add(h2)
model.add(h3)
model.add(h4)
model.add(outputs)

model.compile("adam", "mean_squared_error")

x_train = []
y_train = []

for x in range(0, 200000):
    i1 = random.randint(0, 100)
    i2 = random.randint(0, 100)

    x_train.append([i1, i2])
    y_train.append([i1 * i2])


x_train = numpy.array(x_train)
y_train = numpy.array(y_train)

model.fit(x_train, y_train, epochs=50)


# save
print("Saving...")
model.save(r"C:\Users\timh\Downloads\tah\nn\model")

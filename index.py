import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import rcParams
from IPython.display import set_matplotlib_formats
from sklearn.datasets import make_circles
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
import sys
import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-showTrainingData", "--SHOW_TRAINGING_DATA", required=False)
ap.add_argument("-showTestData", "--SHOW_TEST_DATA", required=False)
ap.add_argument("-showTestResult", "--SHOW_TEST_RESULT", required=False)
ap.add_argument("-showResult", "--SHOW_RESULT", required=False)

args = vars(ap.parse_args())
SHOW_TRAINGING_DATA = args["SHOW_TRAINGING_DATA"] != None
SHOW_TEST_DATA = args["SHOW_TEST_DATA"] != None
SHOW_TEST_RESULT = args["SHOW_TEST_RESULT"] != None
SHOW_RESULT = args["SHOW_RESULT"] != None

X, y = make_circles(n_samples=1000,
                    noise=0.1,
                    factor=0.2,
                    random_state=0)

plt.figure(figsize=(5, 5))
plt.plot(X[y==0, 0], X[y==0, 1], 'ob', alpha=0.5)
plt.plot(X[y==1, 0], X[y==1, 1], 'xr', alpha=0.5)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.legend(['0', '1'])
plt.title("Blue circles and Red crosses")

if SHOW_TRAINGING_DATA:
  plt.show()


model = Sequential()
model.add(Dense(4, input_shape=(2,), activation="tanh"))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer=SGD(lr=0.5), loss="binary_crossentropy", metrics=['accuracy'])

model.fit(X, y, epochs=50)

hticks = np.linspace(-1.5, 1.5, 101)
vticks = np.linspace(-1.5, 1.5, 101)
aa, bb = np.meshgrid(hticks, vticks)

plt.figure(figsize=(5, 5))
plt.scatter(aa, bb, s=0.3, color='blue')
# highlight one horizontal series of grid points
plt.scatter(aa[50], bb[50], s=5, color='green')
# highlight one vertical series of grid points
plt.scatter(aa[:, 50], bb[:, 50], s=5, color='red');

if SHOW_TEST_DATA:
  plt.show()

ab = np.c_[aa.ravel(), bb.ravel()]

c = model.predict(ab)

cc = c.reshape(aa.shape)

plt.figure(figsize=(5, 5))
plt.scatter(aa, bb, s=20*cc);
if SHOW_TEST_RESULT:
  plt.show()

plt.figure(figsize=(5, 5))
plt.contourf(aa, bb, cc, cmap='bwr', alpha=0.2)
plt.plot(X[y==0, 0], X[y==0, 1], 'ob', alpha=0.5)
plt.plot(X[y==1, 0], X[y==1, 1], 'xr', alpha=0.5)
plt.title("Blue circles and Red crosses");

if SHOW_RESULT:
  plt.show()
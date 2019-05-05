import tensorflow as tf
import numpy as np
import pandas as pd

data = np.array([[[1,0,0],[0,1,0],[1,0,0],[0,1,0]],
                 [[1,0,0],[1,0,0],[0,1,0],[0,0,1]],
                 [[1,0,0],[1,0,0],[0,1,0],[0,0,1]],
                 [[0,1,0],[0,0,1],[1,0,0],[1,0,0]],
                 [[0,1,0],[0,0,1],[1,0,0],[1,0,0]],
                 [[1,0,0],[0,0,1],[1,0,0],[0,0,1]],
                 [[1,0,0],[0,0,1],[1,0,0],[0,0,1]]])

data = np.genfromtxt('data.csv')
print('data\n',data)

X_train = data[:4,1:]
y_train = data[:4,:1]
print('X_train\n',X_train)
print('y_train\n',y_train)
X_test = data[4:,1:]
y_test = data[4:,:1]
print('X_test\n',X_test)
print('y_test\n',y_test)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(2,activation=tf.nn.softmax))
model.compile(optimizer='adam',loss='mean_squared_error',metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10)

predictions = model.predict(X_test)

matches = 0
for i in range(np.size(predictions,0)):
    x = int(np.argmax(predictions[i-1]))
    y = int(y_test[i-1][0])
    print(x,y)
    if (x == y):
        matches += 1
print(matches/int(np.size(predictions,0))*100,'%')

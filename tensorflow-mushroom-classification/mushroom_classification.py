import pandas as pd
import tensorflow as tf
import numpy as np

"""
tf.enable_eager_execution()
data_path = 'mushroom_data/mushroom.data'
def csv_to_dataset(verbose=0):
    dataset = tf.data.experimental.CsvDataset(
            data_path,
            np.full(22,tf.string),
            select_cols=list(range(1,23)) # select features, omit label
            )
    if (verbose == 1):
        i = 0
        for element in dataset:
            i += 1
            print(element) 
        print(i,'data records')
    return dataset
if (__name__ == '__main__'):
    dataset = csv_to_dataset()
    iterator = dataset.make_one_shot_iterator()
    next_element = iterator.get_next()
    print(next_element)
    print(type(next_element))
    
   #with tf.Session() as sess, tqdm(total = iterations) as pbar:
   #    sess.run(tf)
   #     try:
   #         sess = tf.Session()
   #         value = sess.run(next_element)
   #         print(value)
   #     except tf.errors.OutOfRangeError:
   #         break
"""


data_path = 'mushroom_data/mushroom_data_without_missing_values.csv'


def generate_data_array():
    df = pd.read_csv(data_path)
    data = pd.get_dummies(df).to_numpy()
    print('data\n',data)
    return data

if (__name__ == '__main__'):
    data = generate_data_array()

    split = int(data.shape[0]/2)
    print(split)
    X_train = data[:split,1:]
    y_train = data[:split,:1]
    print('X_train\n',X_train)
    print('y_train\n',y_train)
    X_test = data[split:,1:]
    y_test = data[split:,:1]
    print('X_test\n',X_test)
    print('y_test\n',y_test)

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(11,input_shape=(99,),activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(5,activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(2,activation=tf.nn.softmax))

    model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
    model.fit(X_train,y_train,epochs=70,shuffle=True)

    predictions = model.predict(X_test)

    matches = 0
    for i in range(np.size(predictions,0)):
        x = int(np.argmax(predictions[i-1]))
        y = int(y_test[i-1][0])
        #print(x,y)
        if (x == y):
            matches += 1
    print(matches/int(np.size(predictions,0))*100,'%')

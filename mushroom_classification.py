import pandas
import tensorflow as tf
tf.enable_eager_execution()
import numpy as np

data_path = 'mushroom_data/mushroom.data'

#def data_set_to_tensor
dataset = tf.data.experimental.CsvDataset(
        data_path,
        np.full(22,tf.string),
        select_cols=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
        )

i = 0
for ele in dataset:
    i += 1
    print(ele)
print(i)
print(type(dataset))

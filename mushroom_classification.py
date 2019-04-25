import pandas
import tensorflow as tf
tf.enable_eager_execution()
import numpy as np

data_path = 'mushroom_data/mushroom.data'

def data_set_to_tensor(verbose=0):
    dataset = tf.data.experimental.CsvDataset(
            data_path,
            np.full(22,tf.string),
            select_cols=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
            )

    i = 0
    for element in dataset:
        i += 1
        if (verbose == 1):
            print(element) 
    print(i,'data records')
    return dataset

if (__name__ == '__main__'):
    #data_set_to_tensor()


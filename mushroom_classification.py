import pandas
import tensorflow as tf
import numpy as np

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

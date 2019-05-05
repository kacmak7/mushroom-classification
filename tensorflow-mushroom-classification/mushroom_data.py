import pandas as pd
import re
import shutil

file_path = 'mushroom_data/agaricus-lepiota.data'
data_path = 'mushroom_data/mushroom.data'
#dataframe = pd.read_csv(data_path)

def check_missing_values():
    regex = re.compile('\?')

    with open(file_path, 'r') as file:
        i = 0
        for line in file:
            if not (regex.search(line) is None):
                i += 1
            
            #result = regex.search(line)
            #print(result)
    print(i, 'records with missing values')

def copy_original_data_set(new_file_path):
    shutil.copyfile(file_path, new_file_path)

def delete_missing_values():
    regex = re.compile('\?')
    
    #TODO: optimize reading
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    with open(data_path, 'w') as file:
        i = 0
        deleted = 0
        for line in lines:
            i += 1
            if (regex.search(line) is None):
                file.write(line)
            else: 
                print(i, 'record deleted')
                deleted += 1
        print()
        print(deleted, 'records has been deleted')


def prepare_data_set():
    copy_original_data_set(data_path)
    #print('data set at:', data_path)
    delete_missing_values()
    print('\nData set prepared at:', data_path)


if __name__ == '__main__':
    check_missing_values()
    prepare_data_set()

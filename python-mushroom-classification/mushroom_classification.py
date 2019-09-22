import numpy as np
import pandas as pd

# without missing values TODO: handle all data
data_df = pd.read_csv('../shared/mushroom_data/mushroom_data_without_missing_values.csv')
data_df = pd.get_dummies(data_df).to_numpy()

print(data_df)
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from path import path_to_training_data
import time

t = time.time()
sample_size = 10*1e6
validation_size = 5*1e6
test_size = .33
seed = 42

train_data_path = os.path.join(path_to_training_data, 'train.csv')
print(train_data_path)
# Get a sample of train data from warehouse
sample = pd.read_csv(train_data_path, nrows=sample_size)

sample['m_distance'] = abs(sample.pickup_longitude - sample.dropoff_longitude) + \
                      abs(sample.pickup_latitude - sample.dropoff_latitude)

# validation_set = pd.read_csv(os.path.join(os.path.curdir, 'data_warhouse/test.csv'), skiprows=sample_size,
#                              nrwos=validation_size)

sample.dropna(inplace=True)
X_train, X_test, Y_train, Y_test = train_test_split(sample.m_distance.values, sample.fare_amount.values, shuffle=True,
                                                    random_state=seed, test_size=test_size)

print(time.time() - t)
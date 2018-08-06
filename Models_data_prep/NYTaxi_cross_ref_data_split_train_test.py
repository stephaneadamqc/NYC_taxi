import pandas as pd
import os
from sklearn.model_selection import train_test_split
from x_commun.NYT_Paths import *
import time


# Parametres

execute_validation = False
execute_sample = True
sample_size = 10*1e6
validation_size = 5*1e6
test_size = .33
seed = 42

t = time.time()

# Get a sample of train data from warehouse

if execute_sample:
    print('execute_sample == Y')
    #Data location
    NYTaxi_train_data = os.path.join(Path_data_Sources, 'train.csv')
    print(NYTaxi_train_data)

    NYTaxi_sample = pd.read_csv(NYTaxi_train_data, nrows=sample_size)

    NYTaxi_sample['m_distance'] = abs(NYTaxi_sample.pickup_longitude - NYTaxi_sample.dropoff_longitude) + \
                      abs(NYTaxi_sample.pickup_latitude - NYTaxi_sample.dropoff_latitude)



    NYTaxi_sample.dropna(inplace=True)
    X_train, X_test, Y_train, Y_test = train_test_split(NYTaxi_sample.m_distance.values,
                                                        NYTaxi_sample.fare_amount.values,
                                                        shuffle=True,random_state=seed,
                                                        test_size=test_size)
    print(time.time() - t)
else:
    print('execute_sample == N')

if execute_validation:
    print('execute_validation == Y')
    # Data location
    # validation_set = pd.read_csv(os.path.join(os.path.curdir, 'data_warhouse/test.csv'), skiprows=sample_size,
    #                              nrwos=validation_size)

else:
    print('execute_validation == N')
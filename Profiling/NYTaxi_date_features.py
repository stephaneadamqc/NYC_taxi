import pandas as pd
import os
from sklearn.model_selection import train_test_split
from x_commun.NYT_Paths import *
import time
from datetime import date

print(' ')
print(' PGM : NYTaxi_date_features')
print(' ')
# Parametres

#execute_NYTaxi_validation_set = True
execute_NYTaxi_validation_set = False
execute_NYTaxi_train_samples = True
#execute_NYTaxi_train_samples = False

sample_size = 100
sample_test_size = .33
validation_size = 5*1e6

seed = 42

t = time.time()

# Get a sample of train data from warehouse

if  execute_NYTaxi_train_samples:
    print('execute_NYTaxi_sample == Y')

    print('NYTaxi_train_data: ',NYTaxi_train_data)

    NYTaxi_train_sample = pd.read_csv(NYTaxi_train_data, nrows=sample_size)


    NYTaxicolumnlistprint = list(NYTaxi_train_sample.columns.values)
    print('list columns', NYTaxicolumnlistprint)

    print(NYTaxi_train_sample.pickup_datetime.head(1))
    testdateconv = pd.to_datetime(NYTaxi_train_sample.pickup_datetime.head(1))
    print('testdateconv: ', testdateconv)
    test_weekday = datetime.weekday( pd.to_datetime(NYTaxi_train_sample.pickup_datetime.head(1)))

   #test_weekday = datetime.weekday(testdateconv)
    print('test_weekday: ', test_weekday)

    NYTaxi_train_sample['m_distance'] = abs(NYTaxi_train_sample.pickup_longitude - NYTaxi_train_sample.dropoff_longitude) + \
                                        abs(NYTaxi_train_sample.pickup_latitude - NYTaxi_train_sample.dropoff_latitude)

    NYTaxi_train_sample['pickup_dateconv'] = pd.to_datetime(NYTaxi_train_sample(['pickup_datetime']), )
    #NYTaxi_train_sample['pickup_weekday'] = datetime.weekday(NYTaxi_train_sample.pickup_datetime_conv)

    NYTaxi_train_sample.dropna(inplace=True)


    print(time.time() - t)

    print(NYTaxi_train_sample)
else:
    print('execute_NYTaxi_sample == N')

if execute_NYTaxi_validation_set:
    print('execute_NYTaxi_validation_set == Y')
else:
    print('execute_NYTaxi_validation_set == N')
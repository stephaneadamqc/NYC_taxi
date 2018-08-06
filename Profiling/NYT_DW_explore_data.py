import pandas as pd
import numpy as np
import os
import time
import matplotlib.pyplot as plt
import seaborn as sns
from x_commun.NYT_Paths import *
print(' ')
print('PGM explore NYT')
print(' ')

t = time.time()
NYtaxi_test = pd.read_csv(os.path.join(Path_data_Sources, 'test.csv'))
print("Le temps d'éxecution: Lire NYTaxi test {:.3f}".format(time.time() - t))

t = time.time()
NYtaxi_train = pd.read_csv(os.path.join(Path_data_Sources, 'train.csv'), nrows=10*1e6)
print("Le temps d'éxecution: Lire NYTaxi train {:.3f}".format(time.time() - t))
print("Temps d'écution: %.3f, %s" % (time.time() - t, 'hello'))

print(NYtaxi_train.head())
print(NYtaxi_train.keys())


NYtaxi_train.describe().to_csv(os.path.join(Path_Profiling, 'describe_NYT_train.csv'))


NYtaxi_train.fare_amount.hist()
plt.title('fare_amount')
# plt.show()

plt.figure()
NYtaxi_train.fare_amount[(NYtaxi_train.fare_amount < 30) & (NYtaxi_train.fare_amount > 2)].hist()
plt.title('2 < fare amount < 30')
# plt.show()

print(NYtaxi_train.isnull().sum())
NYtaxi_train.dropna(inplace=True)
print(NYtaxi_train.isnull().sum())

# print(NYtaxi_train.loc[:, train.keys().values[3:5]].describe())
# print(NYtaxi_train.loc[:, train.keys().values[5:7]].describe())
# NYtaxi_train = NYtaxi_train[(train.pickup_longitude < 80) & (train.dropoff_longitude < 80)]
# print(NYtaxi_train.loc[:, NYtaxi_train.keys().values[3:5]].describe())
# print(NYtaxi_train.loc[:, NYtaxi_train.keys().values[5:7]].describe())

NYtaxi_train['m_distance'] = abs(NYtaxi_train.pickup_longitude - NYtaxi_train.dropoff_longitude) + \
                      abs(NYtaxi_train.pickup_latitude - NYtaxi_train.dropoff_latitude)
# train.m_distance.hist()
# plt.yscale('log')
# plt.show()

plt.figure()
NYtaxi_train = NYtaxi_train[NYtaxi_train.m_distance < 1]
NYtaxi_train.m_distance.hist()
plt.yscale('log')
plt.title('manhattan distance')


plt.figure()
sns.scatterplot(data=NYtaxi_train.iloc[0:10000], x='m_distance', y='fare_amount')


plt.figure()
print((NYtaxi_train.m_distance == 0).sum())
NYtaxi_train[NYtaxi_train.m_distance == 0].fare_amount.hist()
plt.yscale('log')
plt.title('fare_amount when manhattan distant == 0')
plt.show()

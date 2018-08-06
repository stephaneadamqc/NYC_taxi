import pandas as pd
import numpy as np
import os
import time
import matplotlib.pyplot as plt
import seaborn as sns

os.chdir("..")
print(os.path.abspath(os.curdir))
report_dir = os.path.join(os.path.abspath(os.curdir), 'reports')


print(os.path.dirname(__file__))
print(os.path.abspath(__file__))
print(os.path.relpath(__file__))
print(os.curdir)
print(os.listdir(os.path.dirname(__file__)))
t = time.time()
test = pd.read_csv(os.path.join(os.path.dirname(__file__), 'A_Sources/test.csv'))
train = pd.read_csv(os.path.join(os.path.dirname(__file__), 'A_Sources/train.csv'), nrows=10*1e6)
print("Le temps d'éxecution: {:.3f}".format(time.time() - t))
print("Temps d'écution: %.3f, %s" % (time.time() - t, 'hello'))
print(train.head())
print(train.keys())
train.describe().to_csv(os.path.join(report_dir, 'describe_train.csv'))
train.fare_amount.hist()
plt.title('fare_amount')
# plt.show()

plt.figure()
train.fare_amount[(train.fare_amount < 30) & (train.fare_amount > 2)].hist()
plt.title('2 < fare amount < 30')
# plt.show()

print(train.isnull().sum())
train.dropna(inplace=True)
print(train.isnull().sum())

# print(train.loc[:, train.keys().values[3:5]].describe())
# print(train.loc[:, train.keys().values[5:7]].describe())
# train = train[(train.pickup_longitude < 80) & (train.dropoff_longitude < 80)]
# print(train.loc[:, train.keys().values[3:5]].describe())
# print(train.loc[:, train.keys().values[5:7]].describe())

train['m_distance'] = abs(train.pickup_longitude - train.dropoff_longitude) + \
                      abs(train.pickup_latitude - train.dropoff_latitude)
# train.m_distance.hist()
# plt.yscale('log')
# plt.show()

plt.figure()
train = train[train.m_distance < 1]
train.m_distance.hist()
plt.yscale('log')
plt.title('manhattan distance')


plt.figure()
sns.scatterplot(data=train.iloc[0:10000], x='m_distance', y='fare_amount')


plt.figure()
print((train.m_distance == 0).sum())
train[train.m_distance == 0].fare_amount.hist()
plt.yscale('log')
plt.title('fare_amount when manhattan distant == 0')
plt.show()

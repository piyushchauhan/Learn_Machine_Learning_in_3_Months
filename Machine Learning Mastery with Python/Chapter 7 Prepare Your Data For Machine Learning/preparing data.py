from matplotlib import pyplot
from pandas import read_csv
from sklearn.preprocessing import MinMaxScaler

filename = '../pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
# separae array in to input and output components
X = array[:,0:8]
Y = array[:,8]

MinMaxscaler = MinMaxScaler(feature_range = (0, 1))
StScaler = StandardScaler().fit(X)


rescaledX1 = MinMaxscaler.fit_transform(X)
# summerize transformed data
set_printoptions(precision = 3)
print(rescaledX1[0:5,:])

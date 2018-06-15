# Load CSV using NumPy
from numpy import loadtxt
filename = '../pima-indians-diabetes.csv'
raw_data = open(filename, 'r')
data = loadtxt(raw_data, delimiter=",")
print(data.shape)
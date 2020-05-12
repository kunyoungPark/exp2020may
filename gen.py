from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot
import csv


# seed random number generator
seed(1)
# prepare data
data1 = 20 * randn(2000) + 100
data2 = data1 + 10 * randn(2000) + 50
# summarize
print('data1: mean=%.3f stdv=%.3f' % (mean(data1), std(data1)))
print('data2: mean=%.3f stdv=%.3f' % (mean(data2), std(data2)))
# plot
pyplot.scatter(data1, data2, s= 5)
pyplot.show()
#to CSV
f = open('C:\\Users\\Owner\\Desktop\\Cor_Data_samp.csv','w',newline='')
wr = csv.writer(f,delimiter='\t')
wr.writerow(['x', 'y'])
for i in range(len(data1)):
    wr.writerow([data1[i],data2[i]])
f.close()
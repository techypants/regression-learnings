import random
import matplotlib.pyplot as plt
from scipy import stats
import math
x=[]
y=[]
# for i in range(0,10):
#     x.append(random.randint(0,15))
#     y.append(random.randint(70,90))
# x=[22, 23, 24, 2, 25, 2, 8, 13, 21, 1]
# y=[12, 4, 2, 12, 8, 6, 6, 20, 10, 6]
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,7,77,85,86]
x=[5,7,12,16,20]
y=[40,120,180,210,240]

plt.scatter (x,y)
plt.plot()

xMean=sum(x)/len(x)
yMean=sum(y)/len(y)

xi_xMean = []
yi_yMean = []
for i in range(len(x)):
    xi_xMean.append(x[i]-xMean)
    yi_yMean.append(y[i]-yMean)

diffProd = []
for i in range(len(xi_xMean)):
    a=xi_xMean[i]*yi_yMean[i]
    diffProd.append(a)

sqXdiff = []
for i in range(len(xi_xMean)):
    sqXdiff.append(math.pow(xi_xMean[i],2))

sumDiffProd=sum(diffProd)
sumSqDiff = sum(sqXdiff)

b=sumDiffProd/sumSqDiff
a=yMean - b*xMean

x_reg = list(range(min(x),max(x)+1))
y_reg = [a+b*xi for xi in x_reg]

plt.plot(x_reg,y_reg,label='reg line')
plt.show()
    
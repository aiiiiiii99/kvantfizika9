import csv
import numpy as np
import matplotlib.pyplot as plt
import math
file=open('data2.csv', newline='')
x=np.empty(0,dtype='f')
y=np.empty(0,dtype='f')
red1=np.empty(0,dtype='f')
try:
    reader=csv.reader(file)
    for row in reader:
        red1=np.append(red1, row)
    for i in range(2,np.size(red1)):
        if i%2!=0:
            x=np.append(x, float(red1[i]))
        else:
            y=np.append(y, float(red1[i]))
finally:
    file.close()
def sred(mass,n):
    sum=0
    count=np.size(mass)
    for i in range(count):
        sum=sum+mass[i]**n
    return sum/count
def parametrs(x,y):
    xy=np.array([], dtype='f')
    for i in range(np.size(x)):
        xy=np.append(xy,(x[i]*y[i]))
    k=(sred(xy,1)-sred(x,1)*sred(y,1))/(sred(x,2)-sred(x,1)**2)
    b=sred(y,1)-k*sred(x,1)
    n=math.sqrt(np.size(x))
    dk=math.sqrt((sred(y,2)-sred(y,1)**2)/(sred(x,2)-sred(x,1)**2)-k**2)/n
    db=math.sqrt(sred(x,2)-sred(x,1)**2)*dk
    otvet=[k,b,dk,db]
    return otvet
pt=parametrs(x,y)
y1=np.empty(0)
for i in range(np.size(x)):
    i=x[i]*pt[0]+pt[1]
    y1=np.append(y1,i)
fig, ax=plt.subplots()
ax.plot(x, y1)
ax.scatter(x, y, s=2)
plt.show()


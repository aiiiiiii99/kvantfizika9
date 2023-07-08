import csv
import numpy as np
import matplotlib.pyplot as plt
import math
file=open('data1.csv',newline='')
x=np.empty(0,dtype='f')
y=np.empty(0,dtype='f')
dx=np.empty(0,dtype='f')
dy=np.empty(0,dtype='f')
red1=np.empty(0,dtype='f')
try:
    reader=csv.reader(file)
    for row in reader:
        red1=np.append(red1, row)
    for i in range(4,np.size(red1),2):
        if i%4!=0:
            x=np.append(x, float(red1[i]))
        else:
            y=np.append(y, float(red1[i]))
    for i in range(5,np.size(red1),4):
        dy=np.append(dy,float(red1[i]))
    for i in range(7,np.size(red1),4):
        dx=np.append(dx,float(red1[i]))
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
ax.errorbar(x,y,dy,dx,fmt='.')
plt.show()
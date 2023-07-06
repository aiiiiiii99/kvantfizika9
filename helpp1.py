import random
import math
import numpy as np
import matplotlib.pyplot as plt
n=int(input())
x=np.array([])
for i in range(n):
    i=random.randint(0,100)
    x=np.append(x,i)
y=np.array([], dtype='f')
otkl=0
ky=random.uniform(0,5)
by=random.uniform(0,6)
for k in range(n):
    otkl=random.uniform(-10,10)
    y=np.append(y,((float(x[k]*ky))+by+otkl))
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
y1=np.array([])
pt=parametrs(x,y)
for i in range(n):
    i=x[i]*pt[0]+pt[1]
    y1=np.append(y1,i)
fig, ax=plt.subplots()
x2 = [0, 100]
y2 = [by, ky*x2[1]+by]
ax.plot(x, y1)
ax.plot(x2,y2)
ax.scatter(x, y, s=2)
ax.set_title('Линиаризация точек')
ax.set_xlabel('ось х')
ax.set_ylabel('ось у')
plt.show()
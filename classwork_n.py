#open('name','r') or 'w'
import numpy as np
import matplotlib.pyplot as plt
'''file=open('data-txt/00 mm.txt','r')
try:
    data=file.readlines()
finally:
    file.close()
y=np.array(data[4:], dtype='i')
x=np.arange(-50,50)
fig, ax=plt.subplots()
ax.plot(x, y)
plt.show()'''
y=np.empty(0)
fig, ax=plt.subplots()
for i in range(10):
    y=np.empty(0)
    a='data-txt/{}0 mm.txt'.format(i)
    file=open(a,'r')
    try:
        data=file.readlines()
    finally:
        file.close()
    x=np.arange(-50,50)
    t=np.array(data[4:],dtype='i')
    y=np.append(y,t)
    ax.plot(x, y)
plt.show()
    
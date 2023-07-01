import numpy as np
mass=[]
for i in range(8):
    b=[]
    for k in range(8):
        if (i+k)%2==0:
            b.append(1)
        else:
            b.append(0)
    mass.append(b)
mass=np.array(mass, ndmin=2)
count=0
for i in range(8):
    for k in range(6):
        if mass[i, k]==1:
            count=count+1
print(count)

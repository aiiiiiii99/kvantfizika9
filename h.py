import numpy as np
n = int(input())
index=[2**i for i in range(1,n+1)]
znach=[i**2 for i in range(1,n+1)]
mass=np.array([index, znach], ndmin=2)
otvet_ind=[]
def drob(znach):
    result=False
    while znach%2==0:
        znach=znach//2
    while znach%5==0:
        znach=znach//5
    if znach==1:
        result=True
    return result
otvet=0
for k in range(n):
    if drob(mass[1,k])==True:
        otvet=otvet+1
        otvet_ind.append(mass[0,k])
print(otvet_ind)
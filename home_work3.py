import random as rng
import matplotlib.pyplot as plt
import numpy as np

Max = 100 
Length = 50000 

def gaussgen(low, up):
	s = low
	for i in range(up):
		s += rng.randint(0, 1)
	return s

def createDist(data):
	dist = np.zeros(Max)
	for n in data:
		dist[n] = dist[n] + 1
	for i in range(len(dist)):
		dist[i] = dist[i] / len(data)
	return dist

data = np.array([gaussgen(0, Max) for i in range(Length)])
# print(data)
dist = createDist(data)
# print(dist)
fig, ax = plt.subplots()
ax.plot(np.arange(0, Max), dist)
plt.plot(np.arange(0, Max), dist, color='grey', marker='o', markersize=2)
ax.bar(np.arange(0, Max), dist, alpha=0.5, color='grey')
ax.set_title('крутая диаграмма', color='red')
ax.set_xlabel('ось х', color='green')
ax.set_ylabel('ось у',color='blue')
plt.show()
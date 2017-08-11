import numpy as np
import time

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a,b)
toc = time.time()

print(c)
print("vector:"+ str((toc-tic)*1000) + "ms")

tic = time.time()
c = 0
for i in range(1000000):
    c+=a[i]*b[i]
toc = time.time()

print(c)
print("loop:"+ str((toc-tic)*1000) + "ms")
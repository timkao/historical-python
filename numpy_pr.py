import numpy as np

print np.nonzero([1, 2, 0, 0, 4, 0])
print (np.__version__)
np.__config__.show()

z = np.zeros(10)
z[4] = 1
print z
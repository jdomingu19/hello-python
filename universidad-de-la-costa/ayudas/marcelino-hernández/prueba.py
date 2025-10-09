
import numpy as np

m1 = [[1, 2, 3], [1.5, 2.5, 3.5], ["1", "2", "3"]]
print(m1)

m2 = np.zeros([3])
print(m2)
print(m2[0])
print(m2[1])
print(m2[2])

m2[0] = "hello"
print(m2[0])
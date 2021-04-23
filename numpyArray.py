import numpy as np

x = np.arange(15, dtype=np.int64).reshape(3, 5)
x[1:, ::2] = -99

print(x)

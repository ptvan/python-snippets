# Andrew Trask's barebones neural network
import numpy as np


# sigmoid function
def nonlin(x, deriv=False):
    if deriv is True:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


np.random.seed(1)

# input data
X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])

# output data
y = np.array([[0, 0, 1, 1]]).T

# initialize random weights
syn0 = 2*np.random.random((3, 1)) - 1

for j in range(60000):
    # forward propagation:
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))

    # calculate error
    l1_error = y - l1
    l1_delta = l1_error * nonlin(l1, True)
    syn0 += np.dot(l0.T, l1_delta)

print("Output After Training:")
print(l1)


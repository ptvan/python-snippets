import numpy as np

weight, goal_pred, input = (0.0, 0.8, 1.1)

for iteration in range(4):
    print("----\nWeight:" + str(weight))
    pred = input * weight
    error = (pred - goal_pred) ** 2
    delta = pred - goal_pred
    weight_delta = delta * input
    weight = weight - weight_delta
    print("Error:" + str(error) + " Prediction:" + str(pred))
    print("Delta:" + str(delta) + " Weight Delta:" + str(weight_delta))


## BAREBONES NEULRALNET

def nonlin(x, derive=False):
    if (derive==True):
        return x*(1-x)
    return 1/(1 + np.exp(-x))


X = np.array([[0,0,1],
              [0,1,1],
              [1,0,1],
              [1,1,1]])

# output data
y = np.array([[0, 0, 1, 1]]).T

# initialize random weights
syn0 = 2 * np.random.random((3, 1)) - 1

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


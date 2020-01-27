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


## M.N.I.S.T. 
import sys
import numpy as np
from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

images, labels = (x_train[0:1000].reshape(1000, 28*28) / 255  , y_train[0:1000])
one_hot_labels = np.zeros((len(labels), 10))

for i,l in enumerate(labels):
    one_hot_labels[i][l] = 1
labels = one_hot_labels

test_images = x_test.reshape(len(x_test), 28*28) / 255
test_labels = np.zeros((len(y_test), 10))

for i,l in enumerate(y_test): 
    test_labels[i][l] = 1

np.random.seed(1)
relu = lambda x:(x>0) * x
relu2derive = lambda x: x>=0
alpha = 0.005
iterations = 350
hidden_size = 40
pixels_per_image = 784
num_labels = 10
weights_0_1 = 0.2 * np.random.random((pixels_per_image, hidden_size)) - 0.1
weights_1_2 = 0.2 * np.random.random((hidden_size, num_labels)) - 0.1

for j in range(iterations):
    error, correct_cnt = (0.0, 0)

    for i in range(len(images)):
        layer_0 = images[i:i+1]
        layer_1 = relu(np.dot(layer_0, weights_0_1))
        layer_2 = np.dot(layer_1, weights_1_2)
        error += np.sum((labels[i:i+1] - layer_2) ** 2)
        correct_cnt += int(np.argmax(layer_2) == np.argmax(labels[i:i+1]))
        layer_2_delta = (labels[i:i+1] - layer_2)
        layer_1_delta = layer_2_delta.dot(weights_1_2.T) * relu2derive(layer_1)
        weights_1_2 += alpha * layer_1.T.dot(layer_2_delta)
        weights_0_1 += alpha * layer_0.T.dot(layer_1_delta)

    sys.stdout.write("\r"+ \
                    " I:"+str(j)+ \
                    " Error:" + str(error/float(len(images)))[0:5] + \
                    " Correct:" + str(correct_cnt/float(len(images))))

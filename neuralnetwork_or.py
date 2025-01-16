import numpy as np

# 2-input perceptron fanction
def perceptron(x1,x2, w1, w2, theta):
    f = x1*w1 + x2*w2
    if f <= theta:
        y = 0
    else:
        y = 1
    return y

# input data
x1 = np.array([0,0,1,1])
x2 = np.array([0,1,0,1])
w1 = 0.5
w2 = 0.5
theta = 0.2

for i in range(4):
    X1 = x1[i]
    X2 = x2[i]
    y = perceptron(X1, X2, w1, w2, theta)
    print("x1 = ", X1, " x2 = ", X2, " y = ", y)

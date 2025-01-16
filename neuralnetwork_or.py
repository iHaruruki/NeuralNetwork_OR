import numpy as np

# ReLU関数
def relu(x):
    return np.where(x > 0, x, 0)

# ステップ関数
def step(x):
    return np.where(x > 0, 1, 0)

# XORゲートのニューラルネットワーク
def xor_gate(input1, input2):

    x   = np.array([input1, input2])

W1  = np.array([[0.7, -0.8], [-0.4, 0.7]])
b1  = np.array([-0.2, -0.3])

m1  = np.dot(x, W1) + b1

z1  = relu_function(m1)

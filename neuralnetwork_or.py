import numpy as np

# ReLU関数
def relu(x):
    return np.where(x > 0, x, 0)

# ステップ関数
def step(x):
    return np.where(x > 0, 1, 0)

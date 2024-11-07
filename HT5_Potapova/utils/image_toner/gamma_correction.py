import numpy as np


def gamma_cor(a, img, b):
    return np.clip(a * img + b, 0, 255)

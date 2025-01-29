import numpy as np


def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])

def f2(x: np.ndarray) -> np.ndarray: 
    return (((((x[1] + x[0]) * (np.exp(2.27) * (x[2] + x[0]))) - np.abs((np.exp(3.80) * np.exp(2.29)))) * ((np.cosh(np.exp(2.29)) + (np.exp(3.99) * np.exp(3.99))) + (((x[1] + x[0]) * (x[0] + x[2])) * (np.exp(2.42) * np.exp(3.56)))))) * np.tanh(((np.tanh(x[0]) - (np.arctan(x[0]) * np.exp(1.80))) + (np.tanh(x[0]) - ((x[2] + x[1]) * np.tanh(1.67)))))

def f3(x: np.ndarray) -> np.ndarray:
    return (np.abs(8.721543058172322 * x[0]) - (3.547995991966668 * x[2] - (-5.942384762879078 * x[1]))) - (np.arctan(-77.23937875751111 * x[1]) - (-5.848196391239853 * x[1]))

def f4(x: np.ndarray) -> np.ndarray:
   return ((3.22 * np.exp((np.cos(x[1]) * (np.tanh(1.99) * np.tanh((0.16 + np.cosh(1.04))))))) + ((np.tanh((0.27 + np.cosh(x[1]))) * ((np.tanh((2.62 + (3.69 + x[0]))) * (((np.tanh(((x[1] + np.exp(1.04)) + 3.56)) * np.tanh((x[1] + np.cosh(2.55)))) * 1.06) * np.tanh((0.52 + np.cosh(x[1]))))) * np.exp(np.cosh(np.tanh(x[1]))))) * np.cos(x[1])))

def f5(x: np.ndarray) -> np.ndarray:
   return np.exp(((((((x[0] - np.cosh(np.cosh(-2.15))) +np.abs(np.arctan(3.87))) + np.cosh(0.89)) + (x[1] + 3.49)) + np.sin(np.tanh(x[1]))) + (np.tanh(np.tanh(np.tanh(x[1]))) * x[1]))) * (np.sin(x[0]) - (1.94 + np.abs(x[0])))

def f6(x: np.ndarray) -> np.ndarray:
    return (1.6943887875521109 * x[1]) + ((-6.0562334247427 * x[0]) * np.abs(0.11473376637346892))

def f7(x: np.ndarray) -> np.ndarray:
    return np.abs(-1.6458917835671343 * x[1]) * np.abs(-6.632865731462926 * x[0])
  
def f8(x):
    return x[0] - ((x[2] - (8.33968872568729 - x[0])) * np.exp(((x[0] + 7.02) + np.sqrt(x[0]))))

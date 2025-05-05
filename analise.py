import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 

matriz1 = pd.read_csv('got-s1.csv', delimiter=',', header=None)

matriz2 = pd.read_csv('got-s8.csv', delimiter=',', header=None)

graus_G1 = dict(G1.degree)
graus_G1 = list(graus_G1.values())
graus_medio_G1 = np.mean(graus_G1);


graus_G2 = dict(G2.degree)
graus_G2 = list(graus_G2.values())
graus_medio_G1 = np.mean(graus_G2);


print('graus médio da rede G1: ', grau_medio_G1)
print('graus médio da rede G2: ', grau_medio_G2)


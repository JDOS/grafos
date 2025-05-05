import csv
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Criar o grafo direcionado
G = nx.DiGraph()

print('Lendo arquivo da primeira temporada de GOT:')
# Ler o CSV e adicionar as arestas ao grafo
with open('got-s1.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    for linha in leitor:
        source = linha['Source']
        target = linha['Target']
        weight = int(linha['Weight'])
        G.add_edge(source, target, weight=weight)


print('Criando grafo...')
grafo_got1 = nx.spring_layout(G)  # Layout de posicionamento dos nós
weights1 = nx.get_edge_attributes(G, 'weight')

nx.draw(G, grafo_got1, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', arrows=True)
nx.draw_networkx_edge_labels(G, grafo_got1, edge_labels=weights1)


graus_G1 = dict(G.degree)
graus_G1 = list(graus_G1.values())
graus_medio_G1 = np.mean(graus_G1);

print('graus médio da rede T1 de GOT: ', graus_medio_G1)


print('Desenhando')
plt.title("Grafo")
# Salva como imagem PNG
plt.savefig("grafo-s1.png", format="png")
plt.close()  


# Criar o grafo direcionado
G2 = nx.DiGraph()

print('Lendo arquivo da oitava temporada de GOT:')
# Ler o CSV e adicionar as arestas ao grafo
with open('got-s8.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    for linha in leitor:
        source = linha['Source']
        target = linha['Target']
        weight = int(linha['Weight'])
        G2.add_edge(source, target, weight=weight)


print('Criando grafo...')
grafo_got2 = nx.spring_layout(G2)  # Layout de posicionamento dos nós
weights2 = nx.get_edge_attributes(G2, 'weight')

nx.draw(G2, grafo_got2, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', arrows=True)
nx.draw_networkx_edge_labels(G2, grafo_got2, edge_labels=weights2)


graus_G2 = dict(G2.degree)
graus_G2 = list(graus_G2.values())
graus_medio_G2 = np.mean(graus_G2)

print('graus médio da rede T8 de GOT: ', graus_medio_G2)


print('Desenhando')
plt.title("Grafo")
# Salva como imagem PNG
plt.savefig("grafo-s8.png", format="png")
plt.close()  
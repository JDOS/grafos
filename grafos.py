import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("grafo.csv")


# Remove a primeira coluna (índice dos vértices)
adj_matrix = df.iloc[:, 1:].values

G = nx.from_numpy_array(adj_matrix, create_using=nx.DiGraph)

# Define posições dos nós
pos = nx.spring_layout(G, k=0.1, seed=42)

# Lista de cores: pinta o nó 33 de vermelho, os demais de azul claro
node_colors = ['red' if node == 33 else 'lightblue' for node in G.nodes()]


print("É direcionado?", nx.is_directed(G))

# Quantidade de vértices
num_vertices = G.number_of_nodes()

# Quantidade de arestas
num_arestas = G.number_of_edges()

print(f"Quantidade de vértices: {num_vertices}")
print(f"Quantidade de arestas: {num_arestas}")


# Grau do vértice 33
grau_entrada = G.in_degree(33)
grau_saida = G.out_degree(33)
grau_total = grau_entrada + grau_saida
grau_medio = sum(dict(G.degree()).values()) / G.number_of_nodes()
diferenca = grau_total - grau_medio

arestas_entrada = list(G.in_edges(33))
arestas_saida = list(G.out_edges(33))
arestas_conectadas = arestas_entrada + arestas_saida

print(f"Grau Entrada no vértice 33: {grau_entrada}")
print(f"Grau Saída no vértice 33: {grau_saida}")
print(f"Grau Total vértice 33: {grau_total}")
print(f"Grau médio da rede: {grau_medio:.2f}")
print(f"Diferença da rede: {diferenca:.2f}")

print("Arestas de entrada:", arestas_entrada)
print("Arestas de saída:", arestas_saida)
print("Todas as arestas conectadas ao vértice 33:", arestas_conectadas)




# Desenha o grafo com tamanho 12x7
plt.figure(figsize=(12, 7))
pos = nx.spring_layout(G, k=0.1) 
# nx.draw(G, pos, node_size=50, arrows=True, with_labels=False)
nx.draw(
    G, pos,
    node_color=node_colors,
    node_size=80,
    with_labels=False,
    arrows=True
)

plt.title("Grafo")

# Salva como imagem PNG
plt.savefig("grafo.png", format="png")
plt.close()  
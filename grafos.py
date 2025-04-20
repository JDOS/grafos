import networkx as nx
import matplotlib.pyplot as plt

# Criar um grafo vazio
G = nx.Graph()



# Adicionar nós
G.add_node("A")
G.add_nodes_from(["B", "C", "D"])

# Adicionar arestas
G.add_edge("A", "B")
G.add_edges_from([("B", "C"), ("C", "D"), ("A", "D")])

# Desenhar
nx.draw(G, with_labels=True)

# Salvar a imagem
plt.savefig("meugrafo.png", format="png")
plt.close()  # Fecha o plot pra não mostrar na tela
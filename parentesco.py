import networkx as nx
import matplotlib.pyplot as plt


'''Crie um grafo G não direcionado que representa suas relações familiares (pais, irmãos e avós). 
Cada vértice do grafo deve ser representado pelo nome e sobrenome. 
Atribua pesos às arestas de acordo com as seguintes relações de parentesco entre os membros da sua família: peso 1,
se for uma relação consaguínea e peso 0.5 se for uma relação civil.
Ao final, calcule qual é o grau do vértice que te representa e desenhe o grafo na tela.'''

# Criar um grafo vazio
G = nx.Graph()

G.add_node("A",label="Jônatas D. Oliveira Silvério")
G.add_node("C",label="Carla Mitizy de O. Silvério")
G.add_node("B",labbel="Jéssica Mitizy de O. Silvério")
G.add_node("C",label="Mauro Silvério")
G.add_node("Maria Aparecida de Oliveira")
G.add_node("X")
G.add_node("Orlando Silverio")
G.add_node("Luzia Silverio")
           


G.add_nodes_from(["B", "C", "D"])

# Adicionar arestas
G.add_edge("A", "B")
G.add_edges_from([("B", "C"), ("C", "D"), ("A", "D")])

# Desenhar
nx.draw(G, with_labels=True)

# Salvar a imagem
plt.savefig("meugrafo.png", format="png")
plt.close()  # Fecha o plot pra não mostrar na tela

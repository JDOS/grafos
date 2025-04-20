import networkx as nx
import matplotlib.pyplot as plt


'''Crie um grafo G não direcionado que representa suas relações familiares (pais, irmãos e avós). 
Cada vértice do grafo deve ser representado pelo nome e sobrenome. 
Atribua pesos às arestas de acordo com as seguintes relações de parentesco entre os membros da sua família: peso 1,
se for uma relação consaguínea e peso 0.5 se for uma relação civil.
Ao final, calcule qual é o grau do vértice que te representa e desenhe o grafo na tela.'''

# Criar um grafo vazio
G = nx.Graph()

G.add_node("Jônatas D. Oliveira Silvério")
G.add_node("Jéssica Mitizy de O. Silvério")
G.add_node("Carla Mitizy de O. Silvério")
G.add_node("Mauro Silvério")
G.add_node("Maria Aparecida de Oliveira")
G.add_node("X")
G.add_node("Orlando Silverio")
G.add_node("Luzia Silverio")


# Adicionar arestas com valores (ex: peso)
G.add_edge("Jônatas D. Oliveira Silvério", "Jéssica Mitizy de O. Silvério", peso=1)
G.add_edge("Jônatas D. Oliveira Silvério", "Carla Mitizy de O. Silvério", peso=1)
G.add_edge("Jônatas D. Oliveira Silvério", "Mauro Silvério", peso=1)

G.add_edge("Jéssica Mitizy de O. Silvério", "Carla Mitizy de O. Silvério", peso=1)
G.add_edge("Jéssica Mitizy de O. Silvério", "Mauro Silvério", peso=1)

G.add_edge("Mauro Silvério", "Carla Mitizy de O. Silvério", peso=0.5)
G.add_edge("Mauro Silvério", "Orlando Silverio", peso=1)
G.add_edge("Mauro Silvério", "Luzia Silverio", peso= 1)

G.add_edge("Carla Mitizy de O. Silvério", "Maria Aparecida de Oliveira", peso=1)
G.add_edge("Carla Mitizy de O. Silvério","X", peso= 1)

G.add_edge("Orlando Silverio","Luzia Silverio", peso=0.5)

G.add_edge("Maria Aparecida de Oliveira","X", peso=0.5)

pos = nx.spring_layout(G, k=2) 


nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=5)

# Extrai e desenha os pesos das arestas
edge_labels = nx.get_edge_attributes(G, 'peso')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=5)


plt.title("Grafo Genealógica")

# Salva como imagem PNG
plt.savefig("grafo.png", format="png")
plt.close()  # Fecha a figura para liberar memória

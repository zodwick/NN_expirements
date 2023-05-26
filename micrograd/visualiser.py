from graphviz import Digraph


import networkx as nx
import matplotlib.pyplot as plt


def trace(root):
    nodes, edges = set(), set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child, v))
                build(child)
    build(root)
    return nodes, edges

def draw_dot(root):
    dot = Digraph(format='svg', graph_attr={'rankdir': 'LR'})

    nodes, edges = trace(root)
    for n in nodes:
        uid = str(id(n))
        dot.node(name=uid, label="{ %s | data %.4f }" % (n.label, n.data), shape='record')
        if n._op:
            dot.node(name=uid + n._op, label=n._op)
            dot.edge(uid + n._op, uid)

    for n1, n2 in edges:
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)

    return dot



def visualize_graph(root_value):
    G = nx.DiGraph()

    def traverse(value):
        G.add_node(id(value), label=str(value))

        for child in value._prev:
            G.add_edge(id(child), id(value))

            if id(child) not in G.nodes:
                traverse(child)

    traverse(root_value)

    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')

    plt.figure(figsize=(10, 8))
    nx.draw_networkx(G, pos, with_labels=False, node_color='lightblue', node_size=1000)
    nx.draw_networkx_labels(G, pos, labels, font_color='black', font_size=12)
    plt.axis('off')
    plt.show()
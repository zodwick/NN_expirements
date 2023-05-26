# from graphviz import Digraph


# import networkx as nx
# import matplotlib.pyplot as plt



  

# def draw_dot(root):
#     dot = Digraph(format='png', graph_attr={'rankdir': 'LR'})  # Specify format as 'png'

#     nodes, edges = trace(root)
#     for n in nodes:
#         uid = str(id(n))
#         label = "{ %s | data %.4f }" % (n.label, n.data)
#         dot.node(name=uid, label=label, shape='record')
#         if n._op:
#             dot.node(name=uid + n._op, label=n._op)
#             dot.edge(uid, uid + n._op)  # Connect node to operation node

#     for n1, n2 in edges:
#         dot.edge(str(id(n1)), str(id(n2)))  # Connect nodes

#     return dot



# def trace(root):
#     nodes, edges = set(), set()
    
#     def build(v):
#         if v not in nodes:
#             nodes.add(v)
#             for child in v._prev:
#                 edges.add((child, v))
#                 build(child)
    
#     build(root)
#     return nodes, edges


# def write_dot_file(root, filename):
#     nodes, edges = trace(root)

#     dot_code = 'digraph graphname {\n'
#     for n in nodes:
#         uid = str(id(n))
#         label = "{ %s | data %.4f }" % (n.label, n.data)
#         dot_code += '  {} [label="{}" shape="record"];\n'.format(uid, label)
#         if n._op:
#             dot_code += '  {}_op [label="{}"];\n'.format(uid, n._op)
#             dot_code += '  {} -> {}_op;\n'.format(uid, uid)

#     for n1, n2 in edges:
#         dot_code += '  {} -> {};\n'.format(str(id(n1)), str(id(n2)))

#     dot_code += '}'

#     with open(filename, 'w') as f:
#         f.write(dot_code)
# def visualize_graph(root_value):
#     G = nx.DiGraph()

#     def traverse(value):
#         G.add_node(id(value), label=str(value))

#         for child in value._prev:
#             G.add_edge(id(child), id(value))

#             if id(child) not in G.nodes:
#                 traverse(child)

#         if value._op != "":
#             op_node_label = f"{value._op}()"
#             op_node_id = f"op_{id(value)}"
#             G.add_node(op_node_id, label=op_node_label)
#             G.add_edge(op_node_id, id(value))

#     traverse(root_value)

#     pos = nx.spring_layout(G)
#     labels = nx.get_node_attributes(G, 'label')

#     plt.figure(figsize=(10, 8))
#     nx.draw_networkx(G, pos, with_labels=False, node_color='lightblue', node_size=1000)
#     nx.draw_networkx_labels(G, pos, labels, font_color='black', font_size=12)
#     plt.axis('off')
#     plt.show()

from graphviz import Digraph

def trace(root):
  # builds a set of all nodes and edges in a graph
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
  dot = Digraph(format='svg', graph_attr={'rankdir': 'LR'}) # LR = left to right
  
  nodes, edges = trace(root)
  for n in nodes:
    uid = str(id(n))
    # for any value in the graph, create a rectangular ('record') node for it
    dot.node(name = uid, label = "{ %s | data %.4f }" % (n.label, n.data), shape='record')
    if n._op:
      # if this value is a result of some operation, create an op node for it
      dot.node(name = uid + n._op, label = n._op)
      # and connect this node to it
      dot.edge(uid + n._op, uid)

  for n1, n2 in edges:
    # connect n1 to the op node of n2
    dot.edge(str(id(n1)), str(id(n2)) + n2._op)

  return dot
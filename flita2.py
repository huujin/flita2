import graphviz

with open("list.txt", 'r') as f:
    graph_data = graphviz.Graph()
    graph = []
    while True:
        vertices = f.readline()
        point = vertices.split()
        if len(point) == 2:
            graph_data.edge(point[0], point[1])
            graph.append(point)
        elif len(point) == 1:
            graph_data.node(point[0])
            graph.append(point)
        else:
            break

graph_data.view()
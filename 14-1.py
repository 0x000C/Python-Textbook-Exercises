def DFS(graph, start, end, path, lightest, to_print = False):
    """Assumes graph is a Digraph; start and end are nodes;
            path and lightest are lists of nodes
        Returns a path with least edge weight from start to end in graph"""
    def get_path_weight(path_to_weigh):
        path_weight = 0
        if len(path_to_weigh) > 0:
            for i in range(len(path_to_weigh)-1):
                edges = graph.children_of(path_to_weigh[i]):
                for edge in edges:
                    if edge.get_destination() == path_to_weigh[node+1]
                        path_weight += edge.get_weight()
                        break
        return path_weight

    path = path + [start]
    if to_print:
        print('Current DFS path:', print_path(path))
    if start == end:
        return path
    for edge 
    for node in graph.children_of(start):
        if node not in path:
            if lightest == None or get_path_weight(path) < get_path_weight(lightest)
                new_path = DFS(graph, node, end, path, lightest, to_print)
                if new_path != None:
                    lightest = new_path
    return lightest
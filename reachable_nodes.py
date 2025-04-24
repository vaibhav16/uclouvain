def reachable(adj_list, start_node):
    """ Compute the nodes reachable from a start node

    For the above example, reachable([[1, 3], [2], [0], [4], [3], []], 0)) must return {0, 1, 2, 3, 4}
    and reachable([[1, 3], [2], [0], [4], [3], []], 3) must return {3, 4}

    Parameters:
    -----------
    adj_list : the adjacency list of the graph
    start_node: the index of the start node

    Returns:
    --------
    reachable: set(int) the set of nodes reachable from start_node


    """
    # TODO
    visitedNodes = set()
    def dfs(node):
        if node in visitedNodes:
            return
        visitedNodes.add(node)
        
        for neighbour in adj_list[node]:
            dfs(neighbour)
            
     
    dfs(start_node)
    return visitedNodes
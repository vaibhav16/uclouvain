def mat_to_list(adj_mat):
    """ Convert adjacency matrix to an adjacency list representation

    Parameters:
    -----------
    adj_mat : (a square 0-1 matrix)
        Adjacency matrix (n x n) of the graph (of n nodes)


    Returns:
    --------
     adj_list: `list[list[int]]`
        The adjacency list of the graph

    """
    # TODO
    adj_list = []
    for i in range(len(adj_mat)):
        neighbours = []
        for j in range(len(adj_mat)):
            if adj_mat[i][j] == 1:
                neighbours.append(j)
        adj_list.append(neighbours)
    return adj_list
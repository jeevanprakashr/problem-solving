# Given a graph and a number m, return if it is possible to paint vertices with at-most m colours
# so that no two adjacent vertices should have the same colour.

def mColouringGraph(n, m, edges):
    '''
    since we need to check every possible combination of choosing colours to each vertex, we go with recursion and backtracking
    To keep it simple, we iterate the vertices and colours in the serial number order itself
    For each vertex, try every colour and if a colour is possible, call the function for next vertex, else, try next colour
    once you reach n vertices, that means all the vertices are painted with satisfiable colours and return true
    '''
    graph = getGraph(n, edges)
    color = [0 for _ in range(n)]
    return solve(0, graph, color, n, m)

def solve(node, graph, color, n, m):
    '''
    node - s.no. of curr node
    color - colors of all nodes
    n - no. of nodes
    m - no. of colors
    '''
    if node == n:
        return True
    for col in range(1, m + 1):
        if isSafe(node, graph, color, col):
            color[node] = col
            # if the current path satisfies the condition, no need to check for next colour, straight away return true here itself.
            if solve(node + 1, graph, color, n, m):
                return True
            color[node] = 0 # reset the color so that we can try with next color, this is backtracking
    # if none of the colors satisfy our condition and returned True, then return False here
    return False

def isSafe(node, graph, color, col):
    '''
    node - s.no. of curr node
    color - colors of all nodes
    col - current color in question for node
    '''
    for adNode in graph[node]:
        if color[adNode] == col:
            return False
    return True


def getGraph(n, edges):
    '''
    n - no. of vertices
    '''
    graph = [[] for _ in range(n)]
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        # -1 if vertex serial number starts from 1
        graph[v1 - 1].append(v2 - 1)
        graph[v2 - 1].append(v1 - 1)
    return graph

n = 4 # vertices
m = 3 # colours
e = 5 # edges
edges = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)]
print(mColouringGraph(n, m, edges))
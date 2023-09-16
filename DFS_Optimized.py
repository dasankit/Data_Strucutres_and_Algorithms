
graph = {}

def add_node(v):
    if v in graph:
        print(v," is already present")
    else:
       graph[v] = []


def add_edge(v1,v2):
     if v1 not in graph:
       print(v1," is not present in graph")
     elif v2 not in graph:
         print(v2 ,"not present in graph")
    
     else:
         graph[v1].append(v2)
         graph[v2].append(v1)


add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

add_edge("A","B")
add_edge("B","E")
add_edge("A","C")
add_edge("A","D")
add_edge("B","D")
add_edge("C","D")
add_edge("E","D")
print(graph)


def DFSOptimize (node,graph):
    visited = set()

    if node not in graph:
        return
    stack = []
    stack.append(node)

    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)


DFSOptimize("A",graph)
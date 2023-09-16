
graph = {}

def add_node(v):
    if v in graph:
        print(v," is already present")
    else:
       print(graph)
       graph[v] = []


def add_edge(v1,v2):
     if v1 not in graph:
       print(v1," is not present in graph")
     elif v2 not in graph:
         print(v2 ,"not present in graph")
    
     else:
         print(graph)
         graph[v1].append(v2)
         graph[v2].append(v1)
         


add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")
add_node("H")
# print(graph)

add_edge("A","B")
add_edge("B","C")
add_edge("H","B")
add_edge("C","D")
add_edge("G","E")
add_edge("C","E")
add_edge("E","F")
add_edge("E","H")
print(graph)

def DFS(node,visited,graph):
    if node in graph.keys():
        print(graph.keys())

visited = set()
DFS("A",visited,graph)


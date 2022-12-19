# Write here the code challenge solution
class Node:
    """
    class to create node
    """
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return self.value

class Edge:
   
    def __init__(self,vertex,weight=0):
        self.vertex = vertex
        self.weight = weight

class Grahp:
    """
    class to creat vertex and edge
    """
    def __init__(self):
        self.adj_list = {}

    def add_node(self,value):
        """
        methoud to create key in adj_list with empty list
        """
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex

    def add_edge(self,node1,node2,weight=0):
        """
        methoud to connect tow vertex
        """
        
        if not node1 in self.adj_list.keys():
            return("this node does not exist")

        if not node2 in self.adj_list.keys():
            return("this node does not exist")
        
        edge1 = Edge(node2,weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1,weight)
        self.adj_list[node2].append(edge2)

    def __str__(self):
        output = ''
        for vertex in self.adj_list.keys():
            output+= f'{vertex} ->'
            for edge in self.adj_list[vertex]:
                output+= f'{edge.vertex} ---> '
            output+= '\n'
        return output
    

    def bfs(self,root):
        """
    A methoud that take value argumant then using Breadth First way starting from the inputted value,
     and appending all the visited nodes values in a returned array
        """
        nodes = []
        breadth = []
        visted = set()

        breadth.append(root)
        visted.add(root)

        while len(breadth):
            front = breadth.pop(0)
            nodes.append(front.value)

            for edge in self.adj_list[front]:
                if edge.vertex not in visted:
                    breadth.append(edge.vertex)
                    visted.add(edge.vertex)

        return nodes








if __name__ == "__main__":

    graph1 = Grahp()

    a = graph1.add_node("A")
    b = graph1.add_node("B")
    c = graph1.add_node("C")
    d = graph1.add_node("D")
    e=graph1.add_node('E')
    g= graph1.add_node("g")

    graph1.add_edge(a,b)
    graph1.add_edge(a,c)
    graph1.add_edge(c,b)
    graph1.add_edge(d,b)
    graph1.add_edge(d,c)
    graph1.add_edge(d,e)
    graph1.add_edge(d,g)

    print(graph1)
    print(graph1.bfs(c))

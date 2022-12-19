# Write your test here
import pytest
from .challenge01ghh import Grahp, Node
graph1 = Grahp()



def test_grahp1():
    a = graph1.add_node("A")
    b = graph1.add_node("B")
    c = graph1.add_node("C")
    d = graph1.add_node("D")
    e=graph1.add_node('E')

    graph1.add_edge(a,b)
    graph1.add_edge(a,c)
    graph1.add_edge(c,b)
    graph1.add_edge(d,b)
    graph1.add_edge(d,c)
    graph1.add_edge(d,e)
    
    

    actial=graph1.bfs(a)
    expected=['A', 'B', 'C', 'D', 'E']
    assert actial == expected

def test_grahp2():
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

    actial=graph1.bfs(c)
    expected=['C', 'A', 'B', 'D', 'E', 'g']
    assert actial == expected    

#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

from sys import argv
from graph import Graph


def main():
    graph = Graph()  
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_directed_edge(1, 2)
    graph.add_directed_edge(2, 3)
    graph.add_directed_edge(2, 4)
    graph.add_directed_edge(3, 5)
    graph.add_directed_edge(4, 6)
    graph.add_directed_edge(4, 7)
    graph.add_directed_edge(5, 3)
    graph.add_directed_edge(6, 3)
    graph.add_directed_edge(7, 6)
    graph.add_directed_edge(7, 1)
    # print(graph.vertices)

    # graph.bft(1)
    # graph.bft(4)

    # graph.dft(1)
    # graph.dft(7)

    # print(graph.dft_r(1))
    # print(graph.dft_r(3))
    # print(graph.dft_r(4))

    # print(graph.bfs(1, 3))
    # print(graph.bfs(1, 7))
    # print(graph.bfs(3, 7))

    print(graph.dfs(1, 4))
    print(graph.dfs(1, 3))
    print(graph.dfs(1, 5))


if __name__ == '__main__':
    # TODO - parse argv
    main()
    
"""
Simple graph implementation
"""


class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}                                      # initialize an empty dictionary of vertices
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)            # key to be vertex_id and value to be Vertex
    def add_edge(self, v1, v2):                                 # undirected graph
        if v1 in self.vertices and v2 in self.vertices:         # if v1 and v2 both exist in the vertex list 
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError('Vertex not found')
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError('Vertex not found')

    def bft(self, starting_node):
        # create an empty Queue
        q = Queue()
        # create an empty visited list
        visited = set()
        # add the start node to the queue
        q.enqueue(starting_node)
        # while the Queue is not empty...
        while q.size() > 0:
            # remove the first node from the Queue
            node = q.dequeue()
            # check if node is visited
            if node not in visited:
                # if not, mark node as visited
                print(node)
                visited.add(node)
                # print(self.vertices[node].edges)
                # then put all its children in the queue
                for child in self.vertices[node].edges:
                    # if child not in visited:
                        q.enqueue(child)

    def dft(self, starting_node):
        # create an empty Stack
        s = Stack()
        # create an empty visited list
        visited = set()
        # add the start node to the stack
        s.push(starting_node)
        # while the Stack is not empty...
        while s.size() > 0:
            # remove the first node from the Stack
            node = s.pop()
            # if it hasn't been visited
            if node not in visited:
                # mark it as visited
                print(node)
                visited.add(node)
                # then put all its children in the Stack
                for child in self.vertices[node].edges:
                    s.push(child)

class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.edges = set()
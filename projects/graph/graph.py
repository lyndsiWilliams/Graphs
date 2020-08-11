"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # Creates a new vertex at the parameter id
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # If both parameters exist as vertices...
        if v1 in self.vertices and v2 in self.vertices:
            # Add parameter v2 as a new cell (edge)
            self.vertices[v1].add(v2)
        # Otherwise, one of the vertexes doesn't exist
        else:
            # The raise keyword is used to present errors
            raise IndexError("Vertex does not exist.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # Returns the neighbors of the parameter id
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        q = Queue()

        # Add the parameter ID as the starting vertex ID
        q.enqueue(starting_vertex)

        # Create a set for visited vertices
        visited = set()

        # While the queue is not empty
        while q.size() > 0:
            # Dequeue a vertex
            vertex = q.dequeue()

            # If the vertex hasn't been visited...
            if vertex not in visited:
                # Visit it! By adding it to the visited set
                visited.add(vertex)

                # Add the current vertex's neighbors to the queue
                for neighbor in self.get_neighbors(vertex):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()

        # Add the parameter ID as the starting vertex ID
        s.push(starting_vertex)

        # Create a set for visited vertices
        visited = set()

        # While the queue is not empty
        while s.size() > 0:
            # Dequeue a vertex
            vertex = s.pop()

            # If the vertex hasn't been visited...
            if vertex not in visited:
                # Visit it! By adding it to the visited set
                visited.add(vertex)

                # Add the current vertex's neighbors to the queue
                for neighbor in self.get_neighbors(vertex):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Check if visited is None
        if visited is None:
            # If so, create a set for it
            visited = set()

        # Add the starting vertex to the visited set
        visited.add(starting_vertex)

        # This will show the starting vertex during each recursive call
        print("Start dft_r: ", starting_vertex)

        # Tap into the starting vertex's neighbors
        for neighbor in self.vertices[starting_vertex]:
            # If the neighbor hasn't been visited
            if neighbor not in visited:
                # Recursively traverse through the neighbors
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        q = Queue()

        # Add the parameter ID as the starting vertex ID
        q.enqueue([starting_vertex])

        # Create a set for visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            vertex = q.dequeue()
            # Grab the last vertex from the PATH
            last_vertex = vertex[-1]

            # If that vertex has not been visited...
            if last_vertex not in visited:
                # CHECK IF IT'S THE TARGET
                if last_vertex == destination_vertex:
                    # IF SO, RETURN PATH
                    return vertex

            # Mark it as visited...
            visited.add(last_vertex)

            # Then add A PATH TO its neighbors to the back of the queue
            for neighbor in self.get_neighbors(last_vertex):
                # Add the current neighbor to the path
                path = vertex + [neighbor]
                # Append the neighbor to the back of the path
                q.enqueue(path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack
        s = Stack()

        # Add the parameter ID as the starting vertex ID
        s.push([starting_vertex])

        # Create a set for visited vertices
        visited = set()

        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first PATH
            vertex = s.pop()
            # Grab the last vertex from the PATH
            last_vertex = vertex[-1]

            # If that vertex has not been visited...
            if last_vertex not in visited:
                # CHECK IF IT'S THE TARGET
                if last_vertex == destination_vertex:
                    # IF SO, RETURN PATH
                    return vertex

            # Mark it as visited...
            visited.add(last_vertex)

            # Then add A PATH TO its neighbors to the back of the queue
            for neighbor in self.get_neighbors(last_vertex):
                # Add the current neighbor to the path
                path = vertex + [neighbor]
                # Append the neighbor to the back of the path
                s.push(path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Check if visited is None
        if visited is None:
            # If so, create a set for it
            visited = set()

        # Check if path is None
        if path is None:
            # If so, initialize a blank list for it
            path = []
            
        # Add the starting vertex to the visited set
        visited.add(starting_vertex)

        # Copy path
        path = path + [starting_vertex]

        '''
        The line above is doing this:

        path = list(path)  # makes a copy, new list with current path data
        path.append(starting_vertex)
        '''

        # Check if we're at the destination (base case)
        if starting_vertex == destination_vertex:
            # If so, return the path
            return path

        # Tap into the starting vertex's neighbors
        for neighbor in self.get_neighbors(starting_vertex):
            # If the neighbor hasn't been visited
            if neighbor not in visited:
                # Recursively search through the neighbors
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                # If the new path exists
                if new_path is not None:
                    # Return the new path
                    return new_path

        # If we didn't find the path we're looking for, return None
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

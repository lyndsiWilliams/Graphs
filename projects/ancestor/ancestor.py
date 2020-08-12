class Queue():
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


def earliest_ancestor(ancestors, starting_node):
    # ---------- Building the relatives dictionary ----------

    # Set a blank dict for the relatives
    relatives = {}

    # Loop through the parameter ancestors
    for i in ancestors:
        parent = i[0]
        child = i[1]

        # If the child isn't in the relatives dict yet...
        if child not in relatives:
            # Give the child a spot with an empty list
            relatives[child] = []
        # Add the parent to the list of relatives
        relatives[child].append(parent)

    # If the starting node isn't in the relatives dict...
    if starting_node not in relatives:
        # The child has no ancestors
        return -1

    # ---------- Setting up the search ----------

    # Set a blank list for the paths
    paths = []

    # Create an empty Queue
    q = Queue()
    
    # Add the parameter starting node to the queue
    q.enqueue([starting_node])

    # While the queue is not empty...
    while q.size() > 0:
        # Dequeue the first path
        path = q.dequeue()
        # Grab the last vertex from the PATH
        last_vertex = path[-1]

        # Check if this node is in the relatives dict
        if last_vertex in relatives:
            # Add the ancestors for this node to the queue
            for ancestor in relatives[last_vertex]:
                # Add the current ancestor to the path
                new_path = path + [ancestor]
                # Append the ancestor to the back of the path
                q.enqueue(new_path)
        # Once there are no more "last_vertex"s in the relatives dict
        # We're at the end of the path, so we can log what we've traversed
        else:
            # Copy the current path as is
            new_path = path[:]
            # Store it in the paths list
            paths.append(new_path)
            
    # ---------- Calculate the earliest ancestor ----------

    # Determine the max length of every possible path in paths
    max_length = max([len(path) for path in paths])

    # Return the smallest number from the list of paths matching the max length
    return min([path[-1] for path in paths if len(path) == max_length])


# For testing purposes:
ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(ancestors, 1))
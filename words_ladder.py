import string

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

# Create an empty set for the words
word_set = set()

# Import the word list
with open("words.txt") as f:
    # For each line in the file
    for word in f:
        # Store the words in the word set in lowercase with no white space
        word_set.add(word.strip().lower())

def get_neighbors(word):
    # Return set
    neighbors = []

    # Create a list with each letter of the word
    word_letters = list(word)

    # Loop through each letter in the word
    for i in range(len(word_letters)):
        for letter in list(string.ascii_lowercase):
            # Make a copy of the word
            temp_word = list(word_letters)
            # Substitute the letter into the word copy
            temp_word[i] = letter
            # Make it a string
            temp_word_str = "".join(temp_word)

            # If it's a real word and it isn't the original word
            # Add it to the return set
            if temp_word_str != word and temp_word_str in word_set:
                neighbors.append(temp_word_str)

    return neighbors

def get_neighbors_2(word):
    # Return set
    neighbors = []

    def word_diff_by_1(w1, w2):
        # If the lengths are different, return False
        if len(w1) != len(w2):
            return False

        # Start a count
        diff_count = 0

        # Loop through the letters of w1
        for i in range(len(w1)):
            # If w1 has different letters from w2...
            if w1[i] != w2[i]:
                # Add to the count
                diff_count += 1

        # This will cause it to return True
        return diff_count == 1

    # If they differ by one letter, add to return set
    for word2 in word_set:
        if word_diff_by_1(word, word2):
            neighbors.append(word2)

    # Return the list of neighbors
    return neighbors

# Use this to toggle between which method to use to get neighbors
# get_neighbors is faster
# get_neighbors = get_neighbors_2

def find_word_ladder(start_word, end_word):  # BFS
    # Create an empty queue
    q = Queue()

    # Add the parameter ID as the starting vertex ID
    q.enqueue([start_word])

    # Create a set for visited vertices
    visited = set()

    # While the queue is not empty...
    while q.size() > 0:
        # Dequeue the first PATH
        path = q.dequeue()
        # Grab the last vertex from the PATH
        last_vertex = path[-1]

        # If that vertex has not been visited...
        if last_vertex not in visited:
            # Mark it as visited...
            visited.add(last_vertex)

            # CHECK IF IT'S THE TARGET
            if last_vertex == end_word:
                # IF SO, RETURN PATH
                return path

            # Then add A PATH TO its neighbors to the back of the queue
            for neighbor in get_neighbors(last_vertex):
                # Add the current neighbor to the path
                path_copy = list(path)
                path_copy.append(neighbor)
                # Append the neighbor to the back of the path
                q.enqueue(path_copy)

    # Path was not found
    return None


print(find_word_ladder("sail", "boat"))
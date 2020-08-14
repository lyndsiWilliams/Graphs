from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Using queue for BFS
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

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# Set a dict to hold traversal graph rooms
traversal_graph = {}


# While the length of the traversal graph rooms is less than the total rooms
while len(traversal_graph) < len(room_graph):
    # If the current room id the player is in isn't in traversal graph yet
    if player.current_room.id not in traversal_graph:
        # Add it
        traversal_graph[player.current_room.id] = {}
        # Loop through the exits in the current room
        for exits in player.current_room.get_exits():
            # Mark the exits with a '?'
            traversal_graph[player.current_room.id][exits] = '?'

    # Check for exits in the traversal graph dict
    if '?' in traversal_graph[player.current_room.id].values():
        # Set an empty list for the exit paths
        exit_paths = []

        # Loop through the current room's exits
        for i in player.current_room.get_exits():
            # If the traversal graph room still has an exit...
            if traversal_graph[player.current_room.id][i] == '?':
                # Append any exits to the exit_paths list
                exit_paths.append(i)
        # Choose a random direction to traverse
        random_direction = random.choice(exit_paths)

        # Set the current room to be the previous room
        # (since we'll be going to a new room now)
        previous_room = player.current_room
        # Travel into the random direction
        player.travel(random_direction)
        # Set the player's current room id to the new direction's id
        traversal_graph[previous_room.id][random_direction] = player.current_room.id
        # Add the random direction to the traversal path
        traversal_path.append(random_direction)

    else:
        # Create an empty queue
        q = Queue()

        # Add the id of the current room to the queue
        q.enqueue([player.current_room.id])

        # Create a set for visited rooms
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first path
            path = q.dequeue()
            # Grab the last room from the path
            last_room = path[-1]

            # If that room hasn't been visited...
            if last_room not in visited:
                # Visit it!
                visited.add(last_room)

                # Check for exits
                if '?' in traversal_graph[last_room].values():
                    # -1 to offset because range starts a 0
                    for room in range(len(path) - 1):
                        for key, value in traversal_graph[path[room]].items():
                            if value == path[room + 1]:
                                # + 1 to avoid infinite loop
                                # Because it currently has no direction
                                direction = key
                        # Traverse into the designated direction
                        player.travel(direction)
                        # Add the traversed direction to the traversal path
                        traversal_path.append(direction)
                    break
                
                else:
                    # Loop through the values in the last_room
                    for exit in traversal_graph[last_room].values():
                        # Add the exit to the path
                        new_path = path + [exit]
                        # Add the new path to the queue
                        q.enqueue(new_path)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

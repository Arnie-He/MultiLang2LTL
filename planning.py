import numpy as np
import json
import random
from collections import deque


# Function to randomly select a point in a non-obstacle area
def select_random_point(config_space):
    while True:
        x, y = random.randint(0, config_space.shape[0] - 1), random.randint(
            0, config_space.shape[1] - 1
        )
        if config_space[x, y] == 0:  # 0 indicates non-obstacle
            return (x, y)


# Path to the JSON file
json_file_path = "maps/config_space.json"

# Read the JSON file
with open(json_file_path, "r") as file:
    # Load data from JSON file
    config_space_data = json.load(file)

# Convert the list back to a NumPy array
config_space_matrix = np.array(config_space_data, dtype=int)

# Initialize points and robots
points = []
robots = []
dest_number = 5
robot_number = 2
# Check if the shape is 100x100
if config_space_matrix.shape == (100, 100):
    print("Successfully loaded the configuration space.")
    # Initialize points a, b, c, d, h
    for _ in range(dest_number):
        points.append(select_random_point(config_space_matrix))

    # Initialize two robots
    for _ in range(robot_number):
        robots.append(select_random_point(config_space_matrix))

    print("Points:", points)
    print("Robots:", robots)
else:
    print("Warning: The configuration space does not have the expected shape.")


with open("mocked_ltl/map1.json", "r") as json_file:
    map = json.load(json_file)


def count_unique_letters(s):
    # Split by '&'
    elements = s.split("&")
    # Create a set of unique letters, skipping those that start with '!'
    unique_letters = set(
        element.strip()
        for element in elements
        if element.strip() and not element.strip().startswith("!")
    )
    # Count the unique letters
    return len(unique_letters)


def get_unique_letters(s):
    # Split by '&'
    elements = s.split("&")
    # Create a set of unique letters, skipping those that start with '!'
    unique_letters = set(
        element.strip()
        for element in elements
        if element.strip() and not element.strip().startswith("!")
    )
    # Return the set of unique letters as a list
    return list(unique_letters)


robots_plan = []
potential_maps = np.zeros((dest_number, 100, 100))


def generate_potential_map(config_space, point):
    # Initialize the potential map with high values
    potential_map = np.full(config_space.shape, np.inf)
    # Set the value at the point to 0
    potential_map[point] = 0

    # Queue for BFS
    queue = deque([point])

    while queue:
        x, y = queue.popleft()

        # Directions: up, down, left, right
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            # Check if within bounds and not an obstacle
            if (
                0 <= nx < potential_map.shape[0]
                and 0 <= ny < potential_map.shape[1]
                and config_space[nx, ny] == 0
            ):
                # Check if new value is smaller
                if potential_map[nx, ny] > potential_map[x][y] + 1:
                    potential_map[nx, ny] = potential_map[x][y] + 1
                    queue.append((nx, ny))

    return potential_map


# Generate potential maps for each of the destinations
for i, point in enumerate(points):
    potential_maps[i] = generate_potential_map(config_space_matrix, points[i])

# print(potential_maps[0])

index = len(map) - 1
while index != 0:
    for i, next in enumerate(map[index]):
        if next != "" and count_unique_letters(next) < robot_number:
            index = i
            this_targets = get_unique_letters(next)

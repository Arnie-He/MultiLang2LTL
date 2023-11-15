import numpy as np
import json


def add_rectangle(config_space, top_left, width, height):
    config_space[
        top_left[0] : top_left[0] + height, top_left[1] : top_left[1] + width
    ] = 1


def add_circle(config_space, center, radius):
    for x in range(center[0] - radius, center[0] + radius + 1):
        for y in range(center[1] - radius, center[1] + radius + 1):
            if (x - center[0]) ** 2 + (y - center[1]) ** 2 <= radius**2:
                if 0 <= x < config_space.shape[0] and 0 <= y < config_space.shape[1]:
                    config_space[x, y] = 1


def create_obstacles(space_size, num_obstacles):
    config_space = np.zeros((space_size, space_size), dtype=bool)

    for _ in range(num_obstacles):
        shape_type = np.random.choice(["rectangle", "circle"])

        if shape_type == "rectangle":
            width, height = np.random.randint(1, space_size // 10, size=2)
            top_left = np.random.randint(0, space_size - max(width, height), size=2)
            add_rectangle(config_space, top_left, width, height)

        elif shape_type == "circle":
            radius = np.random.randint(1, space_size // 20)
            center = np.random.randint(radius, space_size - radius, size=2)
            add_circle(config_space, center, radius)

    return config_space


space_size = 100
num_obstacles = 30  # Number of obstacles

# Generate configuration space with obstacles
config_space = create_obstacles(space_size, num_obstacles).tolist()

# Write to JSON file
with open("config_space.json", "w") as json_file:
    json.dump(config_space, json_file, indent=4)

print("Configuration space with various shaped obstacles saved to config_space.json")

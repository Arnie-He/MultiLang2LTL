import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import json

# Configuration Space Dimensions
space_size = 100

# Create a 2D grid for the space (all zeros initially)
config_space = np.zeros((space_size, space_size))


with open("maps/config_space.json", "r") as json_file:
    config_space = json.load(json_file)

# Initialize robot positions
robot_positions = np.array([[2, 2], [98, 98]])  # Adjusted for larger space

# Colors and shapes for each robot
robot_colors = ["red", "blue"]
robot_shapes = ["o", "^"]


# Update function for animation
def update(timestep):
    global robot_positions
    plt.cla()  # Clear the current axes

    # Update robot positions here (your logic will go here)
    robot_positions += np.random.randint(-1, 2, robot_positions.shape)

    # Ensure robot positions stay within bounds
    robot_positions = np.clip(robot_positions, 0, space_size - 1)

    # Redraw the configuration space
    plt.imshow(config_space, cmap="gray", extent=[0, space_size, 0, space_size])
    plt.clim(-1, 1)  # Set the color limit for better contrast

    # Plot robot positions
    for idx, pos in enumerate(robot_positions):
        plt.scatter(pos[1], pos[0], c=robot_colors[idx], s=10, marker=robot_shapes[idx])

    plt.grid(True)  # Enable grid
    plt.gca().set_facecolor("black")  # Set background color to black
    # plt.gca().grid(color="white", linestyle="-", linewidth=0.5)
    plt.tick_params(
        axis="both",
        which="both",
        bottom=False,
        top=False,
        left=False,
        right=False,
        labelbottom=False,
        labelleft=False,
    )


# Create the animation
fig = plt.figure(figsize=(10, 10))
ani = FuncAnimation(fig, update, frames=100, interval=300)

plt.show()

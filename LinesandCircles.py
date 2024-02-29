from typing import List, Tuple
import matplotlib.pyplot as plt
import numpy as np

def sb_tree(rn: List[Tuple[int, int]], n: int) -> List[Tuple[int, int]]:
    if not n:
        return rn
    def new_rn():
        for i in range(len(rn) - 1):
            yield from (rn[i], tuple(map(sum, zip(rn[i], rn[i+1]))))
        yield rn[i+1]
    return sb_tree(list(new_rn()), n-1)

def split_tree(tree: List[List[Tuple[int, int]]]) -> Tuple[List[List[Tuple[int, int]]], List[List[Tuple[int, int]]]]:
    left_tree, right_tree = [], []
    for level in tree:
        left_level, right_level = [], []
        for num, den in level:
            if num < den:  # Less than 1
                left_level.append((num, den))
            elif num > den:  # Greater than 1
                right_level.append((num, den))
        left_tree.append(left_level)
        right_tree.append(right_level)
    return left_tree, right_tree

def plot_with_all_intersection_coordinates(left_tree: List[List[Tuple[int, int]]], right_tree: List[List[Tuple[int, int]]]):
    fig, ax = plt.subplots(figsize=(10, 10))
    max_radius = 0

    # Find the maximum radius from the right_tree
    for level in right_tree:
        for num, den in level:
            if den != 0:  # Ensure denominator is not zero
                radius = num / den
                if radius > max_radius:
                    max_radius = radius

    # Plot circles for the right segment
    for level_index, level in enumerate(right_tree[1:], start=1):  # Skip level 0
        for num, den in level:
            if den != 0:  # Ensure denominator is not zero
                radius = num / den
                circle = plt.Circle((0, 0), radius, fill=False, edgecolor=np.random.rand(3,), linestyle='-', linewidth=1.5)
                ax.add_artist(circle)

    # Convert each fraction to degrees and plot extended lines for the left segment
    for level_index, left_level in enumerate(left_tree[1:], start=1):  # Skip level 0
        for num, den in left_level:
            if den != 0:  # Ensure valid fraction
                degree = 360 * (num / den)  # Convert fraction to degree
                radian = np.deg2rad(degree)
                x_end = max_radius * np.cos(radian)  # Extend to the furthest circle
                y_end = max_radius * np.sin(radian)
                ax.plot([0, x_end], [0, y_end], linewidth=1)
                
                # Display coordinates at the largest circle
                ax.annotate(f'({x_end:.2f}, {y_end:.2f})', (x_end, y_end), textcoords="offset points", xytext=(5,-10))

    ax.set_xlim(-max_radius*1.1, max_radius*1.1)
    ax.set_ylim(-max_radius*1.1, max_radius*1.1)
    ax.set_aspect('equal', 'box')
    plt.title('All Intersection Coordinates for Left Segment Degrees on Largest Circle')
    plt.show()

# Generate and split the Stern-Brocot tree for a desired number of levels
num_levels = 19  # You can change this number to generate more or fewer levels
tree = [list(sb_tree([(0, 1), (1, 0)], i)) for i in range(num_levels+1)]
left_tree, right_tree = split_tree(tree)

# Plot the visualization
plot_with_all_intersection_coordinates(left_tree, right_tree)

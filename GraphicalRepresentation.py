from typing import List, Tuple
import matplotlib.pyplot as plt
import numpy as np

# Function to generate Stern-Brocot tree
def sb_tree(rn: List[Tuple[int, int]], n: int) -> List[Tuple[int, int]]:
    if not n:
        return rn
    def new_rn():
        for i in range(len(rn) - 1):
            yield from (rn[i], tuple(map(sum, zip(rn[i], rn[i+1]))))
        yield rn[i+1]
    return sb_tree(list(new_rn()), n-1)

# Function to split the Stern-Brocot tree into left and right segments
def split_tree(tree: List[List[Tuple[int, int]]]) -> Tuple[List[List[Tuple[int, int]]], List[List[Tuple[int, int]]]]:
    left_tree = []
    right_tree = []
    for level in tree:
        left_level = []
        right_level = []
        for num, den in level:
            if den == 0 or num / den < 1:
                left_level.append((num, den))
            else:
                right_level.append((num, den))
        left_tree.append(left_level)
        right_tree.append(right_level)
    return left_tree, right_tree

# Corrected plotting function
def plot_lines_for_left_segment_corrected(left_tree, right_tree, ax):
    max_radii = {}
    for level_index, level in enumerate(right_tree[1:], start=1):
        for num, den in level:
            if den:
                fraction = num / den
                degree = 360 * fraction
                if degree not in max_radii or level_index < max_radii[degree]:
                    max_radii[degree] = level_index
    for level_index, level in enumerate(left_tree[1:], start=1):
        for num, den in level:
            if den:
                fraction = num / den
                degree = 360 * fraction
                if degree in max_radii:
                    radius = max_radii[degree]
                    radian = np.deg2rad(degree)
                    x_end = radius * np.cos(radian)
                    y_end = radius * np.sin(radian)
                    ax.plot([0, x_end], [0, y_end], linewidth=1, color="black")

# Generate and split the Stern-Brocot tree
num_levels = 15
tree = [list(sb_tree([(0, 1), (1, 0)], i)) for i in range(num_levels+1)]
left_tree, right_tree = split_tree(tree)

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))
max_radius = 0
for level_index, level in enumerate(right_tree[1:], start=1):
    for num, den in level:
        if den:
            radius = num / den
            if radius > max_radius:
                max_radius = radius
            circle = plt.Circle((0, 0), radius, fill=False, edgecolor=np.random.rand(3,), linestyle='-', linewidth=1.5)
            ax.add_artist(circle)
ax.set_xlim(-max_radius*1.1, max_radius*1.1)
ax.set_ylim(-max_radius*1.1, max_radius*1.1)
ax.set_aspect('equal', 'box')
plot_lines_for_left_segment_corrected(left_tree, right_tree, ax)
plt.title('Circles for Right Segment & Corrected Degree Lines for Left Segment')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import math
from itertools import cycle

def continued_fraction_sqrt(n, max_length=20):
    """Compute the continued fraction representation of the square root of an integer."""
    m, d, a0 = 0, 1, int(math.sqrt(n))
    a = a0
    cf = [a]

    if a * a == n:
        return cf  # Terminate if n is a perfect square

    for _ in range(1, max_length):
        m = d * a - m
        d = (n - m * m) / d
        a = int((a0 + m) / d)
        cf.append(a)

    return cf

def plot_incremental_steps(sequences, custom_sequences=None, node_size=5, target_x=None, coordinates=None):
    plt.figure(figsize=(12, 8))
    color_cycle = cycle(plt.rcParams['axes.prop_cycle'].by_key()['color'])
    
    # Determine plot range if coordinates are provided
    if coordinates:
        x_min, x_max, y_min, y_max = coordinates
    elif target_x:
        x_min, x_max = 0, target_x
        y_min, y_max = None, None  # Auto-scale y-axis based on data
    else:
        x_min, x_max, y_min, y_max = None, None, None, None

    for seq in sequences:
        color = next(color_cycle)
        x, y = [0], [0]  # Starting points
        step_count = 0
        for index, value in enumerate(seq):
            direction = 1 if index % 2 == 0 else -1
            for _ in range(value):
                if target_x and step_count >= target_x:
                    break  # Stop if reached target_x
                x.append(x[-1] + 1)
                y.append(y[-1] + direction)
                step_count += 1
        plt.plot(x, y, marker='o', linestyle='-', color=color, markersize=node_size)

    if custom_sequences:
        for custom_seq in custom_sequences:  # Iterate over multiple custom sequences
            color = next(color_cycle)
            x, y = [0], [0]
            step_count = 0
            for index, value in enumerate(custom_seq):
                direction = 1 if index % 2 == 0 else -1
                for _ in range(value):
                    if target_x and step_count >= target_x:
                        break
                    x.append(x[-1] + 1)
                    y.append(y[-1] + direction)
                    step_count += 1
            plt.plot(x, y, marker='o', linestyle='--', color=color, markersize=node_size)

    if any(v is not None for v in [x_min, x_max, y_min, y_max]):
        plt.xlim(x_min, x_max)
        plt.ylim(y_min, y_max)

    plt.title('Incremental Steps for Each Number in Sequences')
    plt.xlabel('Step')
    plt.ylabel('Position')
    plt.grid(True)
    plt.show()

# Example usage
input_numbers = list(range(1, 1000))  # Example range
sequences = [continued_fraction_sqrt(n) for n in input_numbers]

# Including multiple custom sequences
custom_sequences = [
    [1, 2941167820, 10, 1, 1, 3, 3],
    [2941167820, 10, 1, 1, 3, 3],  # Another example custom sequence
    [3, 1, 4, 1, 5, 9, 2, 6]  # And another
]

# Example of customizing plot features
plot_incremental_steps(sequences, custom_sequences, node_size=0.2, target_x=2000)

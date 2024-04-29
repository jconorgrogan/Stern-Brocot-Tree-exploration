from typing import List, Tuple
import plotly.graph_objects as go

def generate_stern_brocot_tree_iterative(basis: List[Tuple[int]], generations: int, dimensions: int) -> List[Tuple[int]]:
    """
    Generate an n-dimensional Stern-Brocot tree iteratively.
    
    :param basis: Initial basis vectors of the tree, typically unit vectors in each dimension.
    :param generations: Number of generations to evolve the tree.
    :param dimensions: Dimension of the space (number of elements in each tuple).
    :return: List of vectors generated in the tree.
    """
    current_vectors = basis
    for _ in range(generations):
        next_vectors = []
        for i in range(len(current_vectors) - 1):
            next_vectors.extend([
                current_vectors[i],
                tuple(current_vectors[i][j] + current_vectors[i + 1][j] for j in range(dimensions))
            ])
        next_vectors.append(current_vectors[-1])
        current_vectors = next_vectors
    return current_vectors

def visualize_vectors(points: List[Tuple[int]], dimensions: int):
    """
    Visualize n-dimensional points projected down to 2D using Plotly, suitable for Stern-Brocot trees.
    
    :param points: Points to plot, assumed to be tuples of integers.
    :param dimensions: Dimension of the points.
    """
    if dimensions < 2:
        raise ValueError("Dimension must be at least 2 to visualize.")
    
    if dimensions == 2:
        x_values, y_values = zip(*points)
    else:
        x_values, y_values = zip(*[(p[0], p[1]) if dimensions > 2 else (p[0], sum(p[1:])) for p in points])

    # Create a scatter plot
    fig = go.Figure(data=go.Scatter(x=x_values, y=y_values, mode='markers',
                                    marker=dict(size=5, color='blue')))
    fig.update_layout(
        title=f'{dimensions}-Dimensional Stern-Brocot Tree Visualization',
        xaxis_title='X Coordinate',
        yaxis_title='Y Coordinate',
        template="plotly_white"
    )
    fig.show()

# Example usage
dimensions = 3
tree_depth = 5
initial_basis = [tuple(int(i == j) for i in range(dimensions)) for j in range(dimensions)]

generated_tree = generate_stern_brocot_tree_iterative(initial_basis, tree_depth, dimensions)
visualize_vectors(generated_tree, dimensions)

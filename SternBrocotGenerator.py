from typing import List, Tuple
import plotly.graph_objects as go

def sb_tree(rn: List[Tuple[int, int]], n: int) -> List[Tuple[int, int]]:
    if not n:
        return rn
    def new_rn():
        for i in range(len(rn) - 1):
            yield from (rn[i], tuple(map(sum, zip(rn[i], rn[i+1]))))
        yield rn[-1]
    return sb_tree(list(new_rn()), n-1)

def format_tree(tree: List[List[Tuple[int, int]]]) -> List[List[str]]:
    return [[f"{num}/{den}" for num, den in level if den != 0] for level in tree]

def unique_in_level(formatted_tree: List[List[str]]) -> List[List[str]]:
    unique_fractions = []
    seen = set()
    for level in formatted_tree:
        new_level = []
        for frac in level:
            if frac not in seen:
                seen.add(frac)
                new_level.append(frac)
        unique_fractions.append(new_level)
    return unique_fractions

# Generate the Stern-Brocot tree up to a specific level
tree_depth = 10
tree = [list(sb_tree([(0, 1), (1, 0)], i)) for i in range(tree_depth)]
formatted_tree = format_tree(tree)
unique_fractions = unique_in_level(formatted_tree)

# Vertical scale factor to adjust Y-axis scale
vertical_scale = 0.5

# Initialize Plotly figure
fig = go.Figure()

# Function to adjust y-value based on vertical scale
def adjust_y(level_index):
    return (level_index + 1) * vertical_scale

# Prepare data for nodes and edges
x_values, y_values, texts = [], [], []

for level_index, level in enumerate(unique_fractions, start=1):
    for fraction in level:
        num, den = map(int, fraction.split('/'))
        x_values.append(num / den if den != 0 else 0)  # Check to avoid division by zero
        y_values.append(adjust_y(level_index - 1))
        texts.append(fraction)

# Add edges (lines) between parent and child nodes
for level_index, level in enumerate(unique_fractions[:-1]):  # Exclude the last level
    for fraction in level:
        num, den = map(int, fraction.split('/'))
        x_parent, y_parent = num / den if den != 0 else 0, adjust_y(level_index)
        for child_fraction in unique_fractions[level_index + 1]:
            child_num, child_den = map(int, child_fraction.split('/'))
            if child_den == 0:  # Skip if child has a denominator of 0
                continue
            x_child = child_num / child_den
            # Only draw edges for valid parent-child relationships
            if child_num + child_den == num + den or num == child_num or den == child_den:
                fig.add_trace(go.Scatter(x=[x_parent, x_child], y=[y_parent, adjust_y(level_index + 1)],
                                         mode='lines', line=dict(color='gray', width=1)))

# Add nodes as markers+text
fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='markers+text', text=texts,
                         textposition="bottom center", marker=dict(size=5),
                         textfont=dict(size=10, family="Arial, bold")))

# Update layout
fig.update_layout(title='Interactive Stern-Brocot Tree Visualization',
                  xaxis_title='Fraction Value', yaxis_title='Level',
                  yaxis=dict(autorange='reversed'), template="plotly_white")

fig.show()

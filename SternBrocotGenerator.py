from typing import List, Tuple
import plotly.graph_objects as go

def sb_tree(rn: List[Tuple[int, int]], n: int) -> List[Tuple[int, int]]:
    if not n:
        return rn
    def new_rn():
        for i in range(len(rn) - 1):
            yield from (rn[i], tuple(map(sum, zip(rn[i], rn[i+1]))))
        yield rn[i+1]
    return sb_tree(list(new_rn()), n-1)

def format_tree(tree: List[List[Tuple[int, int]]]) -> List[List[str]]:
    return [[f"{num}/{den}" for num, den in level] for level in tree]

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
tree_depth = 10  # Adjust this value based on your computational constraints and needs
tree = [list(sb_tree([(0, 1), (1, 0)], i)) for i in range(tree_depth)]
formatted_tree = format_tree(tree)
unique_fractions = unique_in_level(formatted_tree)

# Prepare data for Plotly visualization
x_values = []
y_values = []
texts = []

for level, fractions in enumerate(unique_fractions, start=1):
    for fraction in fractions:
        num, den = map(int, fraction.split('/'))
        if den != 0:  # Avoid dividing by zero
            x_values.append(num / den)
            y_values.append(level)
            texts.append(f'{fraction}')

# Create Plotly figure for interactive visualization with enhanced text styles
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x_values, 
    y=y_values, 
    mode='markers+text', 
    text=texts, 
    textposition="bottom center", 
    marker=dict(size=5),
    textfont=dict(  # Enhancing text font properties
        size=10,  # Increased text size for better legibility
        color="black",
        family="Arial, bold"  # Making text bold
    )
))

# Update layout for readability and interactivity
fig.update_layout(
    title='Interactive Stern-Brocot Tree Visualization',
    xaxis_title='Fraction Value',
    yaxis_title='Level',
    yaxis=dict(autorange='reversed'),  # Reverse Y-axis to have the root at the top
    template="plotly_white",
)

fig.show()

import plotly.graph_objects as go
from fractions import Fraction
from math import atan2, degrees, sqrt

def generate_continued_fraction_of_e(limit):
    """ Generate the continued fraction expansion of e up to a given limit """
    e_cf = [2]  # First term of the continued fraction for e
    k = 1
    while len(e_cf) < limit:
        # The pattern of continued fraction terms for e: [2; 1, 2k, 1]
        e_cf.extend([1, 2 * k, 1])
        k += 1
    return e_cf[:limit]

def compute_fractions_from_cf(cf):
    """ Compute fractions from a continued fraction list """
    fractions = []
    for i in range(len(cf)):
        frac = Fraction(1)
        for j in range(i, -1, -1):
            frac = cf[j] + 1/frac if j < i else cf[j] + frac
        fractions.append(frac.limit_denominator())
    return fractions

# Generate and compute the fractions for e
cf_e = generate_continued_fraction_of_e(10)
fractions_e = compute_fractions_from_cf(cf_e)

# Prepare Plotly data
x_values = [float(frac) for frac in fractions_e]
y_values = [-i for i in range(len(fractions_e))]  # Negative depth
texts = [f"{frac.numerator}/{frac.denominator}" for frac in fractions_e]

# Calculate the angles and lengths for each point from the origin
angles = [degrees(atan2(y, x)) for x, y in zip(x_values, y_values)]
lengths = [sqrt(x**2 + y**2) for x, y in zip(x_values, y_values)]

# Create the figure
fig = go.Figure()

# Add points as markers with text
fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='markers+text', text=texts,
                         textposition="bottom center", marker=dict(size=5),
                         textfont=dict(size=10, family="Arial, bold")))

# Add rays from the origin to each point
for x, y in zip(x_values, y_values):
    fig.add_trace(go.Scatter(x=[0, x], y=[0, y], mode='lines', line=dict(color='grey', width=1)))

# Add annotations for angle and length
for x, y, angle, length in zip(x_values, y_values, angles, lengths):
    fig.add_annotation(x=x, y=y,
                       text=f"Angle: {angle:.2f}°, Length: {length:.2f}",
                       showarrow=True, arrowhead=1, font=dict(size=9))

# Update layout for better visualization
fig.update_layout(title='Approximations of e in the Stern-Brocot Tree with Rays',
                  xaxis_title='Fraction Value', yaxis_title='Negative Level',
                  yaxis=dict(autorange='reversed'), template="plotly_white")

# Display the figure
fig.show()

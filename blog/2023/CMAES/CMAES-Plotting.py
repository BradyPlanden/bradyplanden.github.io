import plotly.express as px
import plotly.graph_objects as go

import pandas as pd

# Read data from a csv
z_data = pd.read_csv("surface.csv", header=None)
line_cmaes = pd.read_csv("CMAES.csv", header=None)
line_gradient = pd.read_csv("GradientDescent.csv", header=None)

line_gradient[(line_gradient < 1e-5) & (line_gradient > -1e-5)] = 0
if len(line_gradient) <= 2:
    new_row = line_gradient.iloc[-1]
    line_gradient = pd.concat([line_gradient, new_row.to_frame().T], ignore_index=True)

fig = go.Figure(
    data=[
        go.Surface(
            z=z_data.values[1:-1, 1:-1],
            y=z_data.values[0, 1:-1],
            x=z_data.values[1:-1, 0],
            opacity=0.5,
        )
    ]
)

fig.add_scatter3d(
    x=line_cmaes.values[0:-1, 0],
    y=line_cmaes.values[0:-1, 1],
    z=line_cmaes.values[0:-1, 2],
    mode="lines",
    name="CMAES",
    line=dict(color="red", width=7),
)

fig.add_scatter3d(
    x=line_gradient.values[0:-1, 0],
    y=line_gradient.values[0:-1, 1],
    z=line_gradient.values[0:-1, 2],
    mode="lines",
    name="Gradient Descent",
    line=dict(color=px.colors.qualitative.Plotly[4], width=7),
)
fig.update_layout(
    template="ggplot2",
    autosize=False,
    width=800,
    height=600,
    margin=dict(l=65, r=50, b=65, t=0),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=0.3),
)

with open("surface-corrupt.json", "w") as f:
    f.write(fig.to_json())

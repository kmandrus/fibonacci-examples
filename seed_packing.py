import plotly.graph_objects as go
import math

phi = (math.sqrt(5) - 1) / 2
radii = [math.sqrt(x) for x in range(100)]
angles = [x * phi * 360 for x in range(100)]

fig = go.Figure(data=
    go.Scatterpolar(
        r=radii,
        theta=angles,
        mode = 'markers',
    ))

fig.update_layout(showlegend=False)
fig.show()
import plotly.graph_objs as go

x = [0, 1, 2, 3, 4]
y = [5, 2, 4, 5, 7]


diag = go.Scatter(x=x, y=y)
fig = go.Figure(data=[diag])
fig.update_yaxes(range=[-50, 50], zeroline=True, zerolinewidth=2, zerolinecolor='Black')
fig.update_xaxes(range=[-10, 10], zeroline=True, zerolinewidth=2, zerolinecolor='Black')
fig.write_html('just.html', auto_open=True)

import plotly.graph_objs as go

x = [0, 1, 2, 3, 4]
y = [5, 2, 4, 5, 7]

diag = go.Scatter(x=x, y=y)
fig = go.Figure(data=[diag])
fig.write_html('just.html', auto_open=True)

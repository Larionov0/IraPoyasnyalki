import plotly.graph_objs as go

lst_x = ['Саша', "Петя", "Катя", "Ира"]
lst_y = [10, 11, 5, 8]

diag = go.Bar(x=lst_x, y=lst_y)
fig = go.Figure(
    data=[diag]
)
fig.update_layout(
    title="Оценки класса",
    xaxis_title="дети",
    yaxis_title="оценки",
)

fig.write_html('first_diag.html', auto_open=True)

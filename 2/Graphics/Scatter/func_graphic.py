import plotly.graph_objs as go


def function1(x):
    return -2 * x + 2


def function2(x):
    return 0.5 * x ** 2 + 2


def build_lists_of_x_y(func, start=0, stop=10, step=0.1):
    x_list = []
    y_list = []

    x = start
    while x <= stop:
        y = func(x)
        x_list.append(x)
        y_list.append(y)
        x += step
    return x_list, y_list


start, stop, step = -10, 10, 0.1
x, y = build_lists_of_x_y(function1, start, stop, step)

diag = go.Scatter(x=x, y=y)

layout = go.Layout(
    xaxis=go.layout.XAxis(
        tickmode='linear',
        dtick=1,
        tick0=start,
        gridcolor='Gray',
        gridwidth=1,
        range=[start, stop],
        zeroline=True,
        zerolinewidth=2,
        zerolinecolor='black',
        title='x'
    ),
    yaxis=go.layout.YAxis(
        tickmode='linear',
        # tickvals=list(range(-50, 50)),
        # tickwidth=100,
        dtick=1,
        tick0=-10,
        gridcolor='Gray',
        gridwidth=1,
        range=[-5, 5],
        zeroline=True,
        zerolinewidth=2,
        zerolinecolor='black',
        title='y'
    ),
    plot_bgcolor='white',
    paper_bgcolor='rgb(255,246,212)',
    title='Графік лінійної функції однієї змінної'
)

fig = go.Figure(data=[diag], layout=layout)

fig.write_html('func_graphic.html', auto_open=True)

from math import sin, pi
from random import randint
import plotly.graph_objs as go
import plotly.subplots as plt


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


def gen_sinusoida(f):
    def sinusoida(t):
        """
        :param t: час
        :param f: частота
        :return:
        """
        k = 2 * pi * f
        return 1 * sin(k * t)

    return sinusoida


def main():
    layout = go.Layout(
        xaxis=go.layout.XAxis(
            gridcolor='Gray',
            gridwidth=1,
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='black',
            title='t'
        ),
        yaxis=go.layout.YAxis(
            gridcolor='Gray',
            gridwidth=1,
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='black',
            title='x'
        ),
        plot_bgcolor='white',
        paper_bgcolor='rgb(255,246,212)',
        title='Синусоїди'
    )

    x, y = build_lists_of_x_y(gen_sinusoida(1), 0, 1, 0.001)
    diag1 = go.Scatter(x=x, y=y, name='синусоїда 1')
    x, y = build_lists_of_x_y(gen_sinusoida(10), 0, 1, 0.001)
    diag2 = go.Scatter(x=x, y=y, name='синусоїда 2')
    x, y = build_lists_of_x_y(gen_sinusoida(50), 0, 1, 0.001)
    diag3 = go.Scatter(x=x, y=y, name='синусоїда 3')

    subplots = plt.make_subplots(rows=3, cols=1, subplot_titles=[
        '1',
        '2',
        '3'
    ])
    subplots.append_trace(diag1, 1, 1)
    subplots.append_trace(diag2, 2, 1)
    subplots.append_trace(diag3, 3, 1)
    subplots.update_xaxes(
        gridcolor='Gray',
        gridwidth=1,
        zeroline=True,
        zerolinewidth=2,
        zerolinecolor='black',
        title='t'
    )
    subplots.update_yaxes(
        gridcolor='Gray',
        gridwidth=1,
        zeroline=True,
        zerolinewidth=2,
        zerolinecolor='black',
        title='x'
    )
    subplots.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='rgb(255,246,212)',
        title='Синусоїди'
    )
    subplots.write_html('test.html', auto_open=True)


if __name__ == '__main__':
    main()

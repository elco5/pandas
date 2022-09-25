import numpy as np

import plotly.graph_objs as go

''' 
Class to create a line plot

Use:
import plotly_ploter as pp
plotter = pp.Plotly_Plotter()
plotter.plot(xvals, yvals)

'''

class Plotly_Plotter:

    def __init__(self) -> None:
        self.xvals = None
        self.yvals = None

    def plot(self, yvals: np.ndarray, xvals:np.ndarray):
        self.xvals = xvals
        self.yvals = yvals
        
        trace1 = go.Scatter(
                        name = "trace 1",
                        x = self.xvals,
                        y = self.yvals,
                        mode='lines',
                        marker = dict(color = 'rgb(102,255,255)'),
                        text = self.xvals)

        data = [trace1]
        layout = go.Layout(title = 'Line Plot',
                    xaxis= dict(title= 'xval',ticklen= 5,zeroline= False),
                    yaxis= dict(title= 'yval',ticklen= 5,zeroline= False)
                    )

        fig = go.Figure(data = data, layout = layout)
        fig.show()
        fig.write_html("plot.html")
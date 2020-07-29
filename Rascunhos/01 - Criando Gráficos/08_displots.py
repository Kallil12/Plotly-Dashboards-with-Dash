import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np
import pandas as pd


x = np.random.randn(1000)

hist_data = [x]
group_labels = ['distplot']

fig = ff.create_distplot(hist_data,group_labels)
pyo.plot(fig, filename='displot_test.html')

"""
Defines plotting functions used for the project
"""

import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


def plot_scatter_corr(x, y, data):
	"""Plot the scatter plot of x and y with
	Pearson correlation coefficients.

	:param x: string, variable on x axis
	:param y: string, variable on y axis
	:param data: dataframe containing x and y
	:return:
		fig: the scatter plot
		text: correlation coefficient in text

	Reference
	---------
	https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
	"""
	# sale_price vs daily_average_unit_sold for books that sale over 1000 copies
	fig = sns.scatterplot(x=x, y=y, data=data)

	# correlation
	corr = np.corrcoef(data[x], data[y])
	text = f'Correlation coefficient: {np.round(corr[0, 1], 2)}'

	# plot parameters
	return fig, text


def plot_scatter_corr_log(x, y, data):
	"""Plot the scatter plot of x and y in natural log scale
	with Pearson correlation coefficients.

	:param x: string, variable on x axis
	:param y: string, variable on y axis
	:param data: dataframe containing x and y
	:return:
		fig: the scatter plot in log scale
		text: correlation coefficient in text

	Reference
	---------
	https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
	https://en.wikipedia.org/wiki/Log%E2%80%93log_plot
	"""
	# sale_price vs daily_average_unit_sold for books that sale over 1000 copies
	fig = sns.scatterplot(
		x=np.log(data[x] + 1),
		y=np.log(data[y] + 1),
		data=data)

	# correlation
	corr = np.corrcoef(
		np.log(data[x] + 1),
		np.log(data[y] + 1)
	)
	text = f'Correlation coefficient: {np.round(corr[0, 1], 2)}'

	# plot parameters
	return fig, text

import math
import matplotlib.animation as animation
import matplotlib.colors as colors
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import pandas as pd
import sys

spawn = (28.5, 330.5)

def plot_path(filename, start_episode, episodes):
	fig, ax = plt.subplots()
	data = pd.read_csv(filename, sep=',')
	X, Z = data['x'].astype(int), data['z'].astype(int)
	# X = X[(data['episode'] >= start_episode) & (data['episode'] < start_episode + episodes)]
	# Z = Z[(data['episode'] >= start_episode) & (data['episode'] < start_episode + episodes)]
	x_min, x_max = min(X), max(X)
	z_min, z_max = min(Z), max(Z)
	X = X[(data['episode'] >= start_episode) & (data['episode'] < start_episode + episodes)]
	Z = Z[(data['episode'] >= start_episode) & (data['episode'] < start_episode + episodes)]
	x, z = [], []
	images = []

	divider = make_axes_locatable(ax)
	cax = divider.append_axes("right", size="5%", pad=0.05)
	norm = colors.Normalize()
	sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues, norm=norm)
	sm.set_array([])
	colorbar = fig.colorbar(sm, cax = cax)
	for i, v in X.items():
		x.append(X[i])
		z.append(Z[i])
		heatmap_data, x_edges, z_edges = np.histogram2d(x, z, 
			bins = (x_max - x_min, z_max - z_min),
			range = ((x_min, x_max), (z_min, z_max)))
		extent = [x_edges[0], x_edges[-1], z_edges[0], z_edges[-1]]
		# heatmap = ax.imshow(heatmap_data, extent = extent)
		heatmap = ax.pcolormesh(x_edges, z_edges, np.swapaxes(heatmap_data, 0, 1), cmap = plt.cm.Blues)
		start = ax.scatter([spawn[0]], [spawn[1]], c = 'red', marker = 'x', label = 'start')
		curr_pos = ax.scatter([data['x'][i]], [data['z'][i]], c = 'black', marker = '.', label = 'current position')
		ax.set_aspect('equal')
		# ax.axis('image')
		title = ax.text(0.5, 1.05, 'episode {}'.format(data['episode'][i]), 
			size = plt.rcParams['axes.titlesize'], ha = 'center', transform = ax.transAxes)
		images.append([heatmap, title, start, curr_pos])
	anim = animation.ArtistAnimation(fig, images, interval = 1)
	plt.show()
	# print(anim.to_jshtml())

def main():
	args = sys.argv
	if len(args) < 4:
		return
	filename = args[1]
	start_episode = int(args[2])
	episodes = int(args[3])
	plot_path(filename, start_episode, episodes)

if __name__ == '__main__':
	main()




import math
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
	fig, ax = plt.subplots()
	data = pd.read_csv('./data/moves_0_1.csv', sep=',')
	x_min, x_max = min(data['x']), max(data['x'])
	z_min, z_max = min(data['z']), max(data['z'])
	x, z = [], []
	images = []
	for i in range(500):
		x.append(data['x'][i])
		z.append(data['z'][i])
		heatmap_data, x_edges, z_edges = np.histogram2d(x, z, 
			bins = (x_max - x_min, z_max - z_min),
			range = ((x_min, x_max), (z_min, z_max)))
		extent = [x_edges[0], x_edges[-1], z_edges[0], z_edges[-1]]
		# heatmap = ax.imshow(heatmap_data, extent = extent)
		heatmap = ax.pcolormesh(x_edges, z_edges, np.swapaxes(heatmap_data, 0, 1), 
			cmap = plt.cm.Blues)
		scatter = ax.scatter([28], [330], c = 'black', marker = '.')
		ax.set_aspect('equal')
		# ax.axis('image')
		# colorbar = plt.colorbar(heatmap)
		title = ax.text(0.5, 1.05, 'episode {}'.format(data['episode'][i]), 
			size = plt.rcParams['axes.titlesize'], ha = 'center', transform = ax.transAxes)
		images.append([heatmap, title, scatter])
	anim = animation.ArtistAnimation(fig, images, interval = 1, repeat_delay = 1000)
	plt.show()
	# print(anim.to_jshtml())

if __name__ == '__main__':
	main()
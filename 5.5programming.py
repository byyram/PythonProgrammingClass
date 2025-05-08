import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.manifold import TSNE
from mpl_toolkits.mplot3d import Axes3D

digits = load_digits()
data = digits.data
target = digits.target

tsne = TSNE(n_components=3, random_state=42)
reduced_data = tsne.fit_transform(data)

figure = plt.figure(figsize=(9, 9))
axes = figure.add_subplot(111, projection='3d')

dots = axes.scatter(xs = reduced_data[:, 0], ys = reduced_data[:, 1], zs = reduced_data[:, 2], c = digits.target, cmap = plt.cm.get_cmap('nipy_spectral_r', 10))

colorbar = plt.colorbar(dots)
colorbar.set_label('Digit')

axes.set_xlabel('SNE side x')
axes.set_ylabel('SNE side y')
axes.set_zlabel('SNE side z')

plt.show()
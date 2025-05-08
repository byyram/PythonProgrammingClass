import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.manifold import TSNE
import pandas as pd

iris = load_iris()
data = iris.data
target = iris.target
target_names = iris.target_names

tsne = TSNE(n_components = 2, random_states = 42)
small_data = tsne.fit_transform(data)

tsne_df = pd.DataFrame(data = small_data, columns=['TSNE 1', 'TSNE 2'])
tsne_df['target'] = target
tsne_df['target_name'] = [target_names[i] for i in target]

plt.figure(figsize=(10, 8))
sns.scatterplot(x = 'TSNE 1', y = 'TSNE 2', data = tsne_df)
plt.title('SNE of Iris')
plt.xlabel('SNE 1')
plt.ylabel('SNE 2')
plt.grid(True)
plt.show()
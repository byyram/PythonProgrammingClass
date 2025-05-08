import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
import pandas as pd


digits = load_digits()
data = digits.data
target = digits.target
pca = PCA(n_components=2)
reduced_data_pca = pca.fit_transform(data)

pca_df = pd.DataFrame(data=reduced_data_pca, columns=['component 1', 'component 2'])
pca_df['target'] = target

plt.figure(figsize=(10, 8))
sns.scatterplot(x='component 1', y='component 2', hue='target', palette='rocket_r', data=pca_df)
plt.title('pca visualization')
plt.xlabel('component 1')
plt.ylabel('component 2')
plt.legend(title='Digit')
plt.grid(True)
plt.show()
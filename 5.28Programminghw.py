import statistics
import numpy as np
import matplotlib.pyplot as plt
import seaborn

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]
title = f'Frequency of Votes {len(responses):,} Times'

seaborn.set_style('whitegrid')

unique_responses, counts = np.unique(responses, return_counts=True)

plt.figure(figsize=(8, 6))
seaborn.barplot(x=unique_responses, y=counts)

plt.xlabel('Response Value')
plt.ylabel('Frequency')
plt.title(title)

plt.show()

print(f"Mean: {statistics.mean(responses)}")
print(f"Median: {statistics.median(responses)}")
print(f"Mode: {statistics.mode(responses)}")
print(f"Standard Deviation: {statistics.stdev(responses)}")
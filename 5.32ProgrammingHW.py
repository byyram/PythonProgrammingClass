"""Dynamically graphing frequencies of rolling two dice."""
from matplotlib import animation
import matplotlib.pyplot as plt
import random
import seaborn as sns
import sys

def roll_two_dice():
    """Rolls two six-sided dice and returns their sum."""
    return random.randrange(1, 7) + random.randrange(1, 7)

def update(frame_number, rolls, sums, frequencies):
    """Configures bar plot contents for each animation frame."""
    # roll dice and update frequencies
    for i in range(rolls):
        result = roll_two_dice()
        frequencies[result - 2] += 1  # Adjust index to start from 0

    # reconfigure and update plot for updated die frequencies
    plt.cla()  # clear old contents contents of current Figure
    axes = sns.barplot(x=sums, y=frequencies)  # new bars
    axes.set_title(f'Two Dice Sum Frequencies for {sum(frequencies):,} Rolls')
    axes.set(xlabel='Sum of Two Dice', ylabel='Frequency')
    axes.set_ylim(top=max(frequencies) * 1.10)  # scale y-axis by 10%

    # display frequency & percentage above each patch (bar)
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency / sum(frequencies):.3%}'
        axes.text(text_x, text_y, text, ha='center', va='bottom')

# read command-line arguments for number of frames and rolls per frame
# defaults
number_of_frames = 600
rolls_per_frame = 100

if len(sys.argv) > 2:
    number_of_frames = int(sys.argv[1])
    rolls_per_frame = int(sys.argv[2])
elif len(sys.argv) > 1:
    number_of_frames = int(sys.argv[1])

sns.set_style('whitegrid')  # white backround with gray grid lines
figure = plt.figure('Rolling Two Six-Sided Dice')  # Figure for animation
values = list(range(2, 13))  # sums of two dice
frequencies = [0] * 11  # eleven-element list of sum frequencies

# configure and start animation that calls function update
die_animation = animation.FuncAnimation(
    figure, update, repeat=False, frames=number_of_frames, interval=33,
    fargs=(rolls_per_frame, values, frequencies))

plt.show()  # display window

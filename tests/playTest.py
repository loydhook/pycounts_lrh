import matplotlib.pyplot as plt
from pycounts_lrh.pycounts_lrh import count_words
from pycounts_lrh.plotting import plot_words
counts = count_words("zen.txt")
fig = plot_words(counts, 10)
plt.show()
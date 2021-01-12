import matplotlib.pyplot as plt
#plot original and differenced series for comparison visually

def plot_series_and_difference(axs, series, title):
    diff = series.diff()
    axs[0].plot(series.index, series)
    axs[0].set_title("Raw Series: {}".format(title))
    axs[1].plot(series.index, diff)
    axs[1].set_title("Series of First Differences: {}".format(title))
    plt.tight_layout()

if __name__ == '__main__':
    pass
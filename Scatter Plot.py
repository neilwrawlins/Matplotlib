import matplotlib.pyplot as plt
import numpy as np

def scatterplot(x_data, y_data, x_label = "", y_label = "", title = "", color = "r", y_scale_log = False):

    _, ax = plt.subplots()

    ax.scatter(x_data, y_data, s = 10, color = color, alpha = .75)

    if y_scale_log == True:
        ax.set_yscale('log')

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

scatterplot(x_data = (1,2,3,4,5,6,7), y_data = (3, 4, 7, 12, 15, 65, 100))

plt.show()
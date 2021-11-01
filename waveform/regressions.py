import numpy as np
# import scipy.stats as stats
import matplotlib.pyplot as plt


def cuadratic(x, y):
    # # create scatterplot
    # plt.scatter(x, y)

    # # polynomial fit with degree = 2
    model = np.poly1d(np.polyfit(x, y, 2))

    # # add fitted polynomial line to scatterplot
    # polyline = np.linspace(0, max(x), 100)
    # plt.scatter(x, y)
    # plt.plot(polyline, model(polyline))
    # plt.show()
    return model


# define function to calculate r-squared
def polyfit(x, y, degree):
    results = {}
    coeffs = np.polyfit(x, y, degree)
    p = np.poly1d(coeffs)
    # calculate r-squared
    yhat = p(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)
    sstot = np.sum((y - ybar)**2)
    results['r_squared'] = ssreg / sstot
    return results

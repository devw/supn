import matplotlib.pyplot as plt
import numpy as np
import unittest

###


def get_plot_x_y():
    # Write a function called get_plot_x_y that returns the matplotlib.pyplot instance whitout showing the plot
    # The function must have two parameters.
    # The first parameter represents the x-coordinate
    # The second parameter represents the y-coordinate
    # TODO
    return plt


def get_plot_x_y_title():
    # Write a function called get_plot_x_y_title that returns the matplotlib.pyplot instance whitout showing the plot
    # The function must have three parameters.
    # The 1st parameter represents the x-coordinate of the matplotlib.pyplot instance
    # The 2nd parameter represents the y-coordinate of the matplotlib.pyplot instance
    # The 3rd parameter represents the plot title of the matplotlib.pyplot instance
    # TODO
    return plt

### Testing ### 


class TestGraphicalInterface(unittest.TestCase):

    def test_get_plot_x_y(self):
        x = [1, 2, 5]
        y = [3, 4, 7]
        gca = get_plot_x_y(x, y).gca()
        line = gca.lines[0]
        self.assertTrue((line.get_xdata() == x).all())
        self.assertTrue((line.get_ydata() == y).all())

    def test_get_plot_x_y_title(self):
        x = [1, 2, 5]
        y = [3, 4, 7]
        title = "plot title"
        gca = get_plot_x_y_title(x, y, title).gca()
        line = gca.lines[0]
        self.assertTrue((line.get_xdata() == x).all())
        self.assertTrue((line.get_ydata() == y).all())
        self.assertTrue((gca.get_title() == title))


if __name__ == '__main__':
    unittest.main()

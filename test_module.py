import unittest
import matplotlib as mpl
mpl.use('Agg')  # non-interactive backend for testing
from medical_data_visualizer import draw_cat_plot, draw_heat_map


class CatPlotTestCase(unittest.TestCase):

    def setUp(self):
        self.fig = draw_cat_plot()

    def test_line_chart_has_two_panels(self):
        # catplot returns a figure with 2 axes (one per cardio value)
        actual   = len(self.fig.axes)
        expected = 2
        self.assertEqual(actual, expected)

    def test_bar_chart_number_of_bars(self):
        # Each panel should have 6 groups (variables) × 2 bars (value 0 & 1) = 12
        actual = 0
        for ax in self.fig.axes:
            actual += len([p for p in ax.patches if p.get_height() > 0])
        self.assertEqual(actual, 24)


class HeatMapTestCase(unittest.TestCase):

    def setUp(self):
        self.fig = draw_heat_map()
        self.ax  = self.fig.axes[0]

    def test_heat_map_labels(self):
        actual   = [label.get_text() for label in self.ax.get_xticklabels()]
        expected = ['id', 'age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo',
                    'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio',
                    'overweight']
        self.assertEqual(actual, expected)

    def test_heat_map_values(self):
        # Check that the first annotated cell value is '0.0'
        actual   = self.ax.texts[0].get_text()
        expected = '0.0'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
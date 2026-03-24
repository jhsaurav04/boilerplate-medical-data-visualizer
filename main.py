from medical_data_visualizer import draw_cat_plot, draw_heat_map
import unittest
import test_module

print("=" * 60)
print("Generating Categorical Plot...")
print("=" * 60)
draw_cat_plot()
print("catplot.png saved ✅")

print()
print("=" * 60)
print("Generating Heatmap...")
print("=" * 60)
draw_heat_map()
print("heatmap.png saved ✅")

print()
print("=" * 60)
print("RUNNING UNIT TESTS")
print("=" * 60)
unittest.main(module=test_module, argv=[''], verbosity=2, exit=False)
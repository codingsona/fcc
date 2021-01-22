# This entrypoint file to be used in development. Start by reading README.md
from Numpy_mean_std_var_calculation import mean_var_std
from unittest import main

print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

# Run unit tests automatically
main(module='test_module', exit=False)
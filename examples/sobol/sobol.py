import sys
sys.path.append('../..')

from SALib.sample import saltelli
from SALib.analyze import sobol
from SALib.test_functions import Ishigami
from SALib.util import read_param_file

# Read the parameter range file and generate samples
problem = read_param_file('../../SALib/test_functions/params/Ishigami.txt')

# Generate samples
param_values = saltelli.sample(problem, 1000, calc_second_order=True)

# Run the "model" and save the output in a text file
# This will happen offline for external models
Y = Ishigami.evaluate(param_values)

# Perform the sensitivity analysis using the model output
# Specify which column of the output file to analyze (zero-indexed)
Si = sobol.analyze(problem, Y, calc_second_order=True, conf_level=0.95, print_to_console=False)
# Returns a dictionary with keys 'S1', 'S1_conf', 'ST', and 'ST_conf'
# e.g. Si['S1'] contains the first-order index for each parameter, in the same order as the parameter file
# The optional second-order indices are now returned in keys 'S2', 'S2_conf'
# These are both upper triangular DxD matrices with nan's in the duplicate
# entries.

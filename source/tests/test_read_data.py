# python 3.5.2

from basic_functions import *


## this is a test case to call read_file() with empty file_name input
## expected outcome is None
def test_empty_file_name_nonempty_cell_range_read_file():
    input_param_file_name = ""
    input_param_cell_range = "A5:A10"
    exp_output = None
    real_ouput = read_file(input_param_file_name,input_param_cell_range)
    assert exp_output == real_ouput

## this is a test case to call read_file() with empty cell_range input
# expected outcome is None
def test_empty_file_name_nonempty_file_name_read_file():
    input_param_file_name = "ram.xlsx"
    input_param_cell_range = ""
    exp_output = None
    real_output = read_file(input_param_file_name,input_param_cell_range)
    assert exp_output == real_output
# Importing Libraries
from .functions import fill_median, fill_mode, outlier, duplicate, standardization

# Default preset
def default(data_csv):
    duplicate(data_csv)

# AI preset
def AI(data_csv):
    fill_median(True, 30, data_csv)
    fill_mode(True, 30, data_csv)
    outlier(data_csv)
    duplicate(data_csv)
    standardization(data_csv)

# Bussiness preset
def bussinses(data_csv):
    fill_mode(False, 5, data_csv)
    duplicate(data_csv)

# Streaming preset
def streaming(data_csv):
    fill_mode(True, 50, data_csv)
    outlier(data_csv)
    duplicate(data_csv)
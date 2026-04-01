# Importing Libraries
from .functions import fill_median, fill_mode, outlier, duplicate, standardization

# Default preset
def default(data):
    duplicate(data)

# AI preset
def AI(data):
    fill_median(True, 30, data)
    fill_mode(True, 30, data)
    outlier(data)
    duplicate(data)
    standardization(data)

# Bussiness preset
def bussinses(data):
    fill_mode(False, 5, data)
    duplicate(data)

# Streaming preset
def streaming(data):
    fill_mode(True, 50, data)
    outlier(data)
    duplicate(data)
# Importing Libraries
from .functions import fill_median, fill_mode, outlier, duplicate, standardization

# Default preset
def default(data):
    duplicate(data)

# AI preset
def AI(data):
    fill_median(False, 30, data)
    fill_mode(False, 30, data)
    outlier(data)
    duplicate(data)
    standardization(data)

# Business preset
def business(data):
    fill_mode(False, 5, data)
    duplicate(data)

# Streaming preset
def streaming(data):
    fill_mode(False, 50, data)
    outlier(data)
    duplicate(data)
# Imports and things
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
pd.options.display.max_columns = None
    
    
def assign_age(Age):
    if Age >= 21 and Age <= 40:
        return "21-40"
    elif Age >= 41 and Age <= 60:
        return "41-60"
    elif Age >= 61:
        return "61+"
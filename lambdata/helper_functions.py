#These are helper functions 
import pandas as pd
import numpy as np


def null_count(df):
    df2 = df.isnull().sum()
    dfsum = df2.sum()
    return dfsum
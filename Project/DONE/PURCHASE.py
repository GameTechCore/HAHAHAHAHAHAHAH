import pandas as pd
import numpy as np

def PURCHASE():
    order=pd.read_csv("F:\\Project\\CSV\\ORDER")
    order=pd.concat([order,item], ignore_index=True)
    order.to_csv("F:\\Project\\CSV\\ORDER.csv", index=False)

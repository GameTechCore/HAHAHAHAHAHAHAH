import pandas as pd
import numpy as np

def LAPTOP():
    print(LAPTOP)
    print(LAPTOP[['serial_no','name','quantity_available']])
    q=int(input("Enter LAPTOP Serial No to SEE DESCRIPITION:"))
    for i in list(LAPTOP['serial_no']):
        if i==q:
            

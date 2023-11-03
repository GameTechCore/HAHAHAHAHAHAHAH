import pandas as pd
import numpy as np

def LAPTOP():
    print(LAPTOP)
    print(LAPTOP[['serial_no','name','quantity_available']])
    q=int(input("Enter LAPTOP Serial No to SEE DESCRIPITION:"))
    l=list(LAPTOP['serial_no'])
    for i in list(LAPTOP['serial_no']):
        if i==q:
            d=["8gb ram, 512 ssd, 1k amoled display, dedicated rtx 170, backlit keyboard, i5 10th GEN, WINDOWS 10","8gb ram, 1tb ssd, 1k amoled display, rtx 170, backlit keyboard, i5 11th GEN, WINDOWS 10","","","","","",""]
        else:
            print("INVALID RESPONCE")
            LAPTOP()

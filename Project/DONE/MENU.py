import pandas as pd
import numpy as np
#MENU FOR REVIEW OF ITEMS
def MENU():
    print("Welcome to our MENU")
    print("This is content we have right in here!!")
    #MAIN CSV
    main=pd.read_csv("F:\\Project\\CSV\\MAIN.csv")
    print(main[['serial_no','name']])
    m=int(input("To see more about any content, press the corresponding SERIAL NO.(Else leave empty for Main Menu):"))
    if m==1:
        LAPTOP()
    elif m==2:
        Processor()
    elif m==3:
        Graphics_Card()
    elif m==4:
        RAM()
    elif m==5:
        SSD()
    elif m==6:
        Mouse()
    elif m==7:
        Keyboard()
    elif m=="":
        HOME()
    else:
        print("INPUT NOT SASTISFISTESD")
    #CSVs
MENU()
#WORKING (:

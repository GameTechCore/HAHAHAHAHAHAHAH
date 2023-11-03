import pandas as pd
import numpy as np
name=input("ENTER YOUR NAME:")
user=pd.read_csv("F:\\Project\\CSV\\USER.csv")
#yaha par user.csv se data check kar ke login hoga
def USER():
    print(user[user['u_name']==name])
    print("TO CONTINUE TO HOME, PRESS H")
    print("FOR ACCOUNT SETTINGS, PRESS ENTER")
    opt=input("Enter :")
    if opt=="H" or opt=="h":
        HOME()
    elif opt=="":
        SETTINGS()
    else:
        print("INPUT INVALID!!!!!!!!")
USER()
#WORKING (:

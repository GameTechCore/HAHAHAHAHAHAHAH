import pandas as pd
import numpy as np
name=input("ENTER YOUR Name First:")
admin=pd.read_csv("F:\\Project\\CSV\\ADMIN.csv")
user=pd.read_csv("F:\\Project\\CSV\\USER.csv")
def LOGIN():
    if name in list(admin['a_name']):
        print("ENTER YOUR LOGIN CREDENTIALS!!")
        print("LOGIN AS ADMIN")
        #CHECK FROM USER DATABASE
        if name in list(admin['a_name']):
            passs=int(input("Enter your Passward:"))
            if  passs in list(admin['a_pass']):
                print("You've got access")
                ADMIN()
            else:
                print("WRONG PASSWORD")
                LOGIN()
        else:
            print("ADMIN NOT FOUND")
            print("RETRY")
    elif name in list(user['u_name']):
        print("Alright, You've Got Access!!")
        HOME()
    else:
        print("USER NOT FOUND")
        print("Register")
        REGISTRATION()
        
LOGIN()

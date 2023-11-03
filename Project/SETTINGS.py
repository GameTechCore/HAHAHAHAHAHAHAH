import pandas as pd
import numpy as np
name=input("Enter your name:")
user=pd.read_csv("F:\\Project\\CSV\\USER.csv")
def SETTINGS():
    user=pd.read_csv("F:\\Project\\CSV\\USER.csv")
    index=user[user['u_name']==name].index
    print("WELCOME TO SETTINGS")
    print("To edit ACCOUNT,press 1")
    print("To DELETE ACCOUNT,press 2")
    print("To return to HOME,press 0")
    u_input=input("ENTER INPUT:")
    if u_input=="1":
        print("To change Name,press 1")
        print("To change Age,press 2")
        print("To change Gender,press 3")
        print("To change City,press 4")
        i=input("Enter INPUT:")
        index=user[user['u_name']==name].index
        if i=="1":
            i=input("Enter NEW NAME:")
            user.loc[user['u_name'] == name, 'u_name'] = i
            user.to_csv("F:\\Project\\CSV\\USER.csv", index=False)
        elif i=="2":
            i=input("Enter NEW AGE:")
            user.loc[user['u_name'] == name, 'u_age'] = i
            user.to_csv("F:\\Project\\CSV\\USER.csv", index=False)
        elif i=="3":
            i=input("Enter NEW GENDER:")
            user.loc[user['u_name'] == name, 'u_gender'] = i
            user.to_csv("F:\\Project\\CSV\\USER.csv", index=False)
        elif i=="4":
            i=input("Enter NEW CITY:")
            user.loc[user['u_name'] == name, 'u_city'] = i
            user.to_csv("F:\\Project\\CSV\\USER.csv", index=False)
        else:
            print("INVALID RESPONSE!!!!")
    elif u_input=="2":
        print("ARE YOU SURE")
        i=input("TO DELETE YOUR ACCOUNT(y/n):")
        if i=="y" or i=="Y":
            user=user.drop(index=index)
            user.reset_index(drop=True, inplace=True)
            user.to_csv("F:\\Project\\CSV\\USER.csv", index=False)
    elif u_input=="":
        HOME()
    else:
        print("INVALID INPUT!!!!")
SETTINGS()

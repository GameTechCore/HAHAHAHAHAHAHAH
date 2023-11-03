import  pandas as pd
import numpy as np

#NEW USER ADDITION
def REGISTRATION():
    admin=pd.read_csv("F:\\Project\\CSV\\ADMIN.csv")
    print(admin)
    user=pd.read_csv("F:\\Project\\CSV\\USER.csv")
    print(user)
    r=input("Register yourself as Admin or User(A or U):")
    if r=="A" or r=="a":
        max_aid=admin['aid'].max()
        a_name=input("Let me know your name:") 
        a_age=int(input("How old are you:"))
        a_gender=input("Your Gender:")
        a_city=input("Your City:")
        print("Who are you: 1. Administrator","2.Account Holder","3.Manager")
        a_type=int(input("Enter(1,2,3):"))
        if a_type==1:
            a_type="Admintrator"
        elif a_type==2:
            a_type="Account Holder"
        elif a_type==3:
            a_type="Manager"
        else:
            print("Responce is not valid")
            REGISTRATION()
        a_pass1=int(input("ENTER YOUR SECURITY CODE:"))
        a_pass2=int(input("Re_Enter your security code:"))
        if a_pass1==a_pass2:
            a_pass=a_pass1
        new_data={'aid':max_aid+1,'a_name':a_name,'a_age':a_age,'a_gender':a_gender,'a_city':a_city,'a_type':a_type,'a_pass':a_pass}
        NEW_DATA=pd.DataFrame([new_data])
        admin=pd.concat([admin,NEW_DATA], ignore_index=True)
        admin.to_csv("F:\\Project\\CSV\\ADMIN.csv", index=False)
    elif r=="U" or r=="u":
        max_uid=user['uid'].max()
        u_name=input("Let me know your name:") 
        u_age=int(input("How old are you:"))
        u_gender=input("Your Gender:")
        u_city=input("Your City:")
        p=input("Have you purchased anything(y/n):")
        if p=="y" or p=="Y":
            p=int(input("How much item you have purchased:"))
        elif p=="n" or p=="N":
            p=0
        new_data={'uid':max_uid+1,'u_name':u_name,'u_age':u_age,'u_gender':u_gender,'u_city':u_city,'product_purchased':p}
        NEW_DATA=pd.DataFrame([new_data])
        user=pd.concat([user,NEW_DATA], ignore_index=True)
        user.to_csv("F:\\Project\\CSV\\USER.csv", index=False)
        print("Thank you to becoming our member!!")
        LOGIN()
        #ADD DATA IN USER DATABASE
    else:
        print("Sorry, Your responce is not acceptable, RETRY")
        REGISTRATION()
REGISTRATION()
#NOT WORKING
#HAVE A LOOK ):

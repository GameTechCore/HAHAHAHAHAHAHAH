import pandas as pd,numpy as np,sys
admin=pd.read_csv("F:\\Project\\CSV\\ADMIN.csv")
user=pd.read_csv("F:\\Project\\CSV\\USER.csv")
#MAIN SCREEN
def HOME():
    print("WELCOME TO Techno Youtuber STUDIO")
    print("AnAPPLE brought you to another level of experience!!")
    print("To Explore Our Devices and Accessories, Press 'O'.")
    print("Want to buy something diff'!! PRESS 'X' to shop.")
    print("To Know More About Us, Press'A'")
    print("To Access Your account Details, press 'U'")
    print("Want to exit, press ENTER :(")
    h=input("-->")
    if h=='O' or h=='o':
        MENU()
    elif h=='X' or h=='x':
        SHOP()
    elif h=='a' or h=='A':
        ABOUT()
    elif h=='u' or h=='U':
        USER()
    elif h=='r' or h=='R':
        REGISTRATION()
    elif h=='l' or h=='L':
        ENTRY()
    elif h=='':
        sys.exit()
    else:
        print("Sorry, Your responce is not acceptable")
        HOME()
#LOGIN ==LOGIN.py
def LOGIN():
    global name
    name=input("Enter your Name:")
    admin=pd.read_csv("F:\\Project\\CSV\\ADMIN.csv")
    user=pd.read_csv("F:\\Project\\CSV\\USER.csv")
    i=input("Enter(1 for Admin and 2 for User):")
    if i=="1":
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
                print("Register yourself!!")
                max_aid=admin['aid'].max()
                a_name=name
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
                    LOGIN()
                a_pass1=int(input("ENTER YOUR SECURITY CODE:"))
                a_pass2=int(input("Re_Enter your security code:"))
                if a_pass1==a_pass2:
                    a_pass=a_pass1
                new_data={'aid':max_aid+1,'a_name':a_name,'a_age':a_age,'a_gender':a_gender,'a_city':a_city,'a_type':a_type,'a_pass':a_pass}
                NEW_DATA=pd.DataFrame([new_data])
                admin=pd.concat([admin,NEW_DATA], ignore_index=True)
                admin.to_csv("F:\\Project\\CSV\\ADMIN.csv", index=False)
                ADMIN()
    elif i=='2':
        if name in list(user['u_name']):
            print("Alright, You've Got Access!!")
            HOME()
        else:
            print("USER NOT FOUND")
            print("Register yourself")
            max_uid=user['uid'].max()
            u_name=name 
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
            HOME()
        #ADD DATA IN USER DATABASE
    else:
        print("Sorry, TRY AGAIN!!")
        LOGIN()
    
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
#NEW USER ADDITION
def SETTINGS():
    user=pd.read_csv("F:\\Project\\CSV\\USER.csv")
    index=user[user['u_name']==name].index
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
            print("To modify more, press 0")
            print("Else, press ENTER")
            i=input("Enter INPUT:")
            if i=="0":
                SETTINGS()
            if i=="":
                HOME()
            else:
                print("INVALID RESPONCE!!!!")
        elif i=="2":
            i=input("Enter NEW AGE:")
            user.loc[user['u_name'] == name, 'u_age'] = i
            user.to_csv("F:\\Project\\CSV\\USER.csv", index=False)
            print("To modify more, press 0")
            print("Else, press ENTER")
            i=input("Enter INPUT:")
            if i=="0":
                SETTINGS()
            if i=="":
                HOME()
            else:
                print("INVALID RESPONCE!!!!")
        elif i=="3":
            i=input("Enter NEW GENDER:")
            user.loc[user['u_name'] == name, 'u_gender'] = i
            user.to_csv("F:\\Project\\CSV\\USER.csv", index=False)
            print("To modify more, press 0")
            print("Else, press ENTER")
            i=input("Enter INPUT:")
            if i=="0":
                SETTINGS()
            if i=="":
                HOME()
            else:
                print("INVALID RESPONCE!!!!")
        elif i=="4":
            i=input("Enter NEW CITY:")
            user.loc[user['u_name'] == name, 'u_city'] = i
            user.to_csv("F:\\Project\\CSV\\USER.csv", index=False)
            print("To modify more, press 0")
            print("Else, press ENTER")
            i=input("Enter INPUT:")
            if i=="0":
                SETTINGS()
            if i=="":
                HOME()
            else:
                print("INVALID RESPONCE!!!!")
        else:
            print("INVALID RESPONSE!!!!")
    elif u_input=="2":
        print("ARE YOU SURE")
        i=input("TO DELETE YOUR ACCOUNT(y/n):")
        if i=="y" or i=="Y":
            user=user.drop(index=index)
            user.reset_index(drop=True, inplace=True)
            user.to_csv("F:\\Project\\CSV\\USER.csv", index=False)
            print("Your account is completely deleted, press any key to  Continue to LOGIN!!")
            print("To exit,press 0")
            i=input("ENTER:")
            if i=="0":
                sys.exit()
            else:
                LOGIN()
        elif i=="n" or i=="N":
            print("Sure, Returning to SETTINGS")
            SETTINGS()
        else:
            print("INVALID RESPONSE!!!!")
    elif u_input=="":
        HOME()
    else:
        print("INVALID INPUT!!!!")
#yaha par user.csv se data check kar ke login hoga
def USER():
    admin=pd.read_csv("F:\\Project\\CSV\\ADMIN.csv")
    user=pd.read_csv("F:\\Project\\CSV\\USER.csv")
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
#ABOUT THE FAKE COMPANY
def ABOUT():
    print("OUR Company is Found by You and is situated in Cloud of  California")
    a=input("PRESS ENTER TO GO BACK or 'x' to EXIT!!")
    if a=="X" or a=="x":
        sys.exit()
    HOME()
LOGIN()

import pandas as pd,numpy as np

def ADMIN_ADD_ITEM():
    main=pd.read_csv("F:\\Project\\CSV\\MAIN.csv")
    LAPTOP=pd.read_csv("F:\\Project\\CSV\\LAPTOP.csv")
    PROCESSOR=pd.read_csv("F:\\Project\\CSV\\PROCESSOR.csv")
    GRAPHIC_CARD=pd.read_csv("F:\\Project\\CSV\\GRAPHICS_CARD.csv")
    RAM=pd.read_csv("F:\\Project\\CSV\\RAM.csv")
    SSD=pd.read_csv("F:\\Project\\CSV\\SSD.csv")
    MOUSE=pd.read_csv("F:\\Project\\CSV\\MOUSE.csv")
    KEYBOARD=pd.read_csv("F:\\Project\\CSV\\KEYBOARD.csv")
    print("Which type of item do you want to add?")
    print(main[['serial_no','name']])
    m=int(input("Press the corresponding SERIAL NO.:"))
    if m==1:
        max_s_no=LAPTOP['serial_no'].max()
        q=input("Enter LAPTOP Name:")
        w=int(input("Enter quantity build:"))
        new_data={'serial_no':max_s_no+1,'name':q,'quantity_available':w,'quantity_sold':0}
        NEW_DATA=pd.DataFrame([new_data])
        LAPTOP=pd.concat([LAPTOP,NEW_DATA], ignore_index=True)
        LAPTOP.to_csv("F:\\Project\\CSV\\LAPTOP.csv", index=False)
        main.loc[main['name'] == "LAPTOP", 'no_of_products'] =main.loc[main['name'] == "LAPTOP", 'no_of_products']+1
        main.to_csv("F:\\Project\\CSV\\MAIN.csv", index=False)
        print("You've successfully added new LAPTOP!!")
        print("To return to Home, press 0")
        print("Or to continue editing,press ENTER")
        i=input("Enter:")
        if i=="0":
            HOME()
        elif i=="":
            ADMIN()
        else:
            print("INVALID INPUT!!")
    elif m==2:
        max_s_no=PROCESSOR['serial_no'].max()
        q=input("Enter PROCESSOR Name:")
        w=int(input("Enter quantity build:"))
        new_data={'serial_no':max_s_no+1,'name':q,'quantity_available':w,'quantity_sold':0}
        NEW_DATA=pd.DataFrame([new_data])
        PROCESSOR=pd.concat([PROCESSOR,NEW_DATA], ignore_index=True)
        PROCESSOR.to_csv("F:\\Project\\CSV\\PROCESSOR.csv", index=False)
        main.loc[main['name'] == "PROCESSOR", 'no_of_products'] =main.loc[main['name'] == "PROCESSOR", 'no_of_products']+1
        main.to_csv("F:\\Project\\CSV\\MAIN.csv", index=False)
        print("You've successfully added new PROCESSOR!!")
        print("To return to Home, press 0")
        print("Or to continue editing,press ENTER")
        i=input("Enter:")
        if i=="0":
            HOME()
        elif i=="":
            ADMIN()
        else:
            print("INVALID INPUT!!")
    elif m==3:
        max_s_no=GRAPHIC_CARD['serial_no'].max()
        q=input("Enter Graphic Card Name:")
        w=int(input("Enter quantity build:"))
        new_data={'serial_no':max_s_no+1,'name':q,'quantity_available':w,'quantity_sold':0}
        NEW_DATA=pd.DataFrame([new_data])
        GRAPHIC_CARD=pd.concat([GRAPHIC_CARD,NEW_DATA], ignore_index=True)
        GRAPHIC_CARD.to_csv("F:\\Project\\CSV\\GRAPHIC_CARD.csv", index=False)
        main.loc[main['name'] == "Graphic Cards", 'no_of_products'] =main.loc[main['name'] == "Graphic Cards", 'no_of_products']+1
        main.to_csv("F:\\Project\\CSV\\MAIN.csv", index=False)
        print("You've successfully added new Graphic Card!!")
        print("To return to Home, press 0")
        print("Or to continue editing,press ENTER")
        i=input("Enter:")
        if i=="0":
            HOME()
        elif i=="":
            ADMIN()
        else:
            print("INVALID INPUT!!")
    elif m==4:
        max_s_no=RAM['serial_no'].max()
        q=input("Enter RAM Name:")
        w=int(input("Enter quantity build:"))
        new_data={'serial_no':max_s_no+1,'name':q,'quantity_available':w,'quantity_sold':0}
        NEW_DATA=pd.DataFrame([new_data])
        RAM=pd.concat([RAM,NEW_DATA], ignore_index=True)
        RAM.to_csv("F:\\Project\\CSV\\RAM.csv", index=False)
        main.loc[main['name'] == "RAM", 'no_of_products'] =main.loc[main['name'] == "RAM", 'no_of_products']+1
        main.to_csv("F:\\Project\\CSV\\MAIN.csv", index=False)
        print("You've successfully added new RAM!!")
        print("To return to Home, press 0")
        print("Or to continue editing,press ENTER")
        i=input("Enter:")
        if i=="0":
            HOME()
        elif i=="":
            ADMIN()
        else:
            print("INVALID INPUT!!")
    elif m==5:
        max_s_no=SSD['serial_no'].max()
        q=input("Enter SSD Name:")
        w=int(input("Enter quantity build:"))
        new_data={'serial_no':max_s_no+1,'name':q,'quantity_available':w,'quantity_sold':0}
        NEW_DATA=pd.DataFrame([new_data])
        SSD=pd.concat([SSD,NEW_DATA], ignore_index=True)
        SSD.to_csv("F:\\Project\\CSV\\SSD.csv", index=False)
        main.loc[main['name'] == "SSD", 'no_of_products'] =main.loc[main['name'] == "SSD", 'no_of_products']+1
        main.to_csv("F:\\Project\\CSV\\MAIN.csv", index=False)
        print("You've successfully added new SSD!!")
        print("To return to Home, press 0")
        print("Or to continue editing,press ENTER")
        i=input("Enter:")
        if i=="0":
            HOME()
        elif i=="":
            ADMIN()
        else:
            print("INVALID INPUT!!")
    elif m==6:
        max_s_no=MOUSE['serial_no'].max()
        q=input("Enter MOUSE Name:")
        w=int(input("Enter quantity build:"))
        new_data={'serial_no':max_s_no+1,'name':q,'quantity_available':w,'quantity_sold':0}
        NEW_DATA=pd.DataFrame([new_data])
        MOUSE=pd.concat([MOUSE,NEW_DATA], ignore_index=True)
        MOUSE.to_csv("F:\\Project\\CSV\\MOUSE.csv", index=False)
        main.loc[main['name'] == "MOUSE", 'no_of_products'] =main.loc[main['name'] == "MOUSE", 'no_of_products']+1
        main.to_csv("F:\\Project\\CSV\\MAIN.csv", index=False)
        print("You've successfully added new MOUSE!!")
        print("To return to Home, press 0")
        print("Or to continue editing,press ENTER")
        i=input("Enter:")
        if i=="0":
            HOME()
        elif i=="":
            ADMIN()
        else:
            print("INVALID INPUT!!")
    elif m==7:
        max_s_no=KEYBOARD['serial_no'].max()
        q=input("Enter KEYBOARD Name:")
        w=int(input("Enter quantity build:"))
        new_data={'serial_no':max_s_no+1,'name':q,'quantity_available':w,'quantity_sold':0}
        NEW_DATA=pd.DataFrame([new_data])
        KEYBOARD=pd.concat([KEYBOARD,NEW_DATA], ignore_index=True)
        KEYBOARD.to_csv("F:\\Project\\CSV\\KEYBOARD.csv", index=False)
        main.loc[main['name'] == "KEYBOARD", 'no_of_products'] =main.loc[main['name'] == "KEYBOARD", 'no_of_products']+1
        main.to_csv("F:\\Project\\CSV\\MAIN.csv", index=False)
        print("You've successfully added new KEYBOARD!!")
        print("To return to Home, press 0")
        print("Or to continue editing,press ENTER")
        i=input("Enter:")
        if i=="0":
            HOME()
        elif i=="":
            ADMIN()
        else:
            print("INVALID INPUT!!")
    else:
        print("INPUT NOT SASTISFISTESD")
        ADMIN_ADD_ITEM()

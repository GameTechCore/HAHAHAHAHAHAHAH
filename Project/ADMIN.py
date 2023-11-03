import pandas as pd
import numpy as np
name=input("Enter your name:")
#AUTHENTIC USER, CAN EDIT ITEMS AND USER
def ADMIN():
        main=pd.read_csv("F:\\Project\\CSV\\MAIN.csv")
        LAPTOP=pd.read_csv("F:\\Project\\CSV\\LAPTOP.csv")
        PROCESSOR=pd.read_csv("F:\\Project\\CSV\\PROCESSOR.csv")
        GRAPHIC_CARD=pd.read_csv("F:\\Project\\CSV\\GRAPHICS_CARD.csv")
        RAM=pd.read_csv("F:\\Project\\CSV\\RAM.csv")
        SSD=pd.read_csv("F:\\Project\\CSV\\SSD.csv")
        MOUSE=pd.read_csv("F:\\Project\\CSV\\MOUSE.csv")
        KEYBOARD=pd.read_csv("F:\\Project\\CSV\\KEYBOARD.csv")
        print("Hello",name)
        print("To add new ITEM, press 1")
        print("To Modify ITEM Details, press 2")
        print("To DELETE ITEM, press 3")
        print("See ORDERS, press 4")
        print("Modify or See Graph, press 5")
        print("Visit main page, press 0")
        i=input("Enter Input:")
        if i=="1":
                ADMIN_ADD_ITEM()
        elif i=="2":
                ADMIN_MODIFY_ITEM()
        elif i=="3":
            print("Which type of item do you want to delete?")
            print(main[['serial_no','name']])
            m=int(input("Press the corresponding SERIAL NO.:"))
            if m==1:
                    print(LAPTOP[['serial_no','name','quantity_available']])
                    q=int(input("Enter LAPTOP Serial No to DELETE:"))
                    LAPTOP=LAPTOP.drop(index=q-1)
                    LAPTOP.reset_index(drop=True, inplace=True)
                    LAPTOP.to_csv("F:\\Project\\CSV\\LAPTOP.csv", index=False)
                    main.loc[main['name'] == "LAPTOP", 'no_of_products'] =main.loc[main['name'] == "LAPTOP", 'no_of_products']-1
                    main.to_csv("F:\\Project\\CSV\\MAIN.csv", index=False)
                    print("You've successfully deleted the item!!")
            elif m==2:
                    print(PROCESSOR[['serial_no','name','quantity_available']])
                    q=int(input("Enter PROCESSOR Serial No to DELETE:"))
                    PROCESSOR=PROCESSOR.drop(index=q-1)
                    PROCESSOR.reset_index(drop=True, inplace=True)
                    PROCESSOR.to_csv("F:\\Project\\CSV\\PROCESSOR.csv", index=False)
                    main.loc[main['name'] == "PROCESSOR", 'no_of_products'] =main.loc[main['name'] == "PROCESSOR", 'no_of_products']-1
                    main.to_csv("F:\\Project\\CSV\\MAIN.csv", index=False)
                    print("You've successfully deleted the item!!")
            elif m==3:
                    print(GRAPHIC_CARD[['serial_no','name','quantity_available']])
                    q=int(input("Enter Graphic card Serial No to DELETE:"))
                    GRAPHIC_CARD=GRAPHIC_CARD.drop(index=q-1)
                    GRAPHIC_CARD.reset_index(drop=True, inplace=True)
                    GRAPHIC_CARD.to_csv("F:\\Project\\CSV\\GRAPHIC_CARD.csv", index=False)
                    main.loc[main['name'] == "GRAPHIC_CARD", 'no_of_products'] =main.loc[main['name'] == "GRAPHIC_CARD", 'no_of_products']-1
                    main.to_csv("F:\\Project\\CSV\\MAIN.csv", index=False)
                    print("You've successfully deleted the item!!")
            elif m==4:
                    print(RAM[['serial_no','name','quantity_available']])
                    q=int(input("Enter RAM Serial No to DELETE:"))
                    RAM=RAM.drop(index=q-1)
                    RAM.reset_index(drop=True, inplace=True)
                    RAM.to_csv("F:\\Project\\CSV\\RAM.csv", index=False)
                    main.loc[main['name'] == "RAM", 'no_of_products'] =main.loc[main['name'] == "RAM", 'no_of_products']-1
                    main.to_csv("F:\\Project\\CSV\\MAIN.csv", index=False)
                    print("You've successfully deleted the item!!")
            elif m==5:
                    print(SSD[['serial_no','name','quantity_available']])
                    q=int(input("Enter SSD Serial No to DELETE:"))
                    SSD=SSD.drop(index=q-1)
                    SSD.reset_index(drop=True, inplace=True)
                    SSD.to_csv("F:\\Project\\CSV\\SSD.csv", index=False)
                    main.loc[main['name'] == "SSD", 'no_of_products'] =main.loc[main['name'] == "SSD", 'no_of_products']-1
                    main.to_csv("F:\\Project\\CSV\\MAIN.csv", index=False)
                    print("You've successfully deleted the item!!")
            elif m==6:
                    print(MOUSE[['serial_no','name','quantity_available']])
                    q=int(input("Enter MOUSE Serial No to DELETE:"))
                    MOUSE=MOUSE.drop(index=q-1)
                    MOUSE.reset_index(drop=True, inplace=True)
                    MOUSE.to_csv("F:\\Project\\CSV\\MOUSE.csv", index=False)
                    main.loc[main['name'] == "MOUSE", 'no_of_products'] =main.loc[main['name'] == "MOUSE", 'no_of_products']-1
                    main.to_csv("F:\\Project\\CSV\\MAIN.csv", index=False)
                    print("You've successfully deleted the item!!")
            elif m==7:
                    print(KEYBOARD[['serial_no','name','quantity_available']])
                    q=int(input("Enter KEYBOARD Serial No to DELETE:"))
                    KEYBOARD=KEYBOARD.drop(index=q-1)
                    KEYBOARD.reset_index(drop=True, inplace=True)
                    KEYBOARD.to_csv("F:\\Project\\CSV\\KEYBOARD.csv", index=False)
                    main.loc[main['name'] == "KEYBOARD", 'no_of_products'] =main.loc[main['name'] == "KEYBOARD", 'no_of_products']-1
                    main.to_csv("F:\\Project\\CSV\\MAIN.csv", index=False)
                    print("You've successfully deleted the item!!")
            else:
                        print("INPUT NOT SASTISFISTESD")
        elif i=="4":
                print("")
        elif i=="5":
            print("")
        elif i=="0":
                HOME()
        else:
                print("INVALID INPUT!!!!")
                ADMIN()
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
def ADMIN_MODIFY_ITEM():
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
        print(LAPTOP[['serial_no','name','quantity_available']])
        q=int(input("Enter LAPTOP Serial No to MODIFY:"))
        i=input("What to edit(1 for name and 2 for quantity:)")
        if i=="1":
            w=input("Enter LAPTOP NEW Name to MODIFY:")
            LAPTOP.loc[LAPTOP['serial_no'] == q, 'name']= w
            LAPTOP.to_csv("F:\\Project\\CSV\\LAPTOP.csv", index=False)
            print("DONE, SUCCESSFULLY MODIFIED!!")
        elif i=="2":
            w=int(input("Enter new quantity:"))
            LAPTOP.loc[LAPTOP['serial_no'] == q, 'quantity_available'] = w
            LAPTOP.to_csv("F:\\Project\\CSV\\LAPTOP.csv", index=False)
            print("DONE, SUCCESSFULLY MODIFIED!!")
        else:
            print("INPUT INVALID!!")
    elif m==2:
        print(PROCESSOR[['serial_no','name','quantity_available']])
        q=int(input("Enter PROCESSOR Serial No to MODIFY:"))
        i=input("What to edit(1 for name and 2 for quantity:)")
        if i=="1":
            w=input("Enter PROCESSOR NEW Name to MODIFY:")
            PROCESSOR.loc[PROCESSOR['serial_no'] == q, 'name']= w
            PROCESSOR.to_csv("F:\\Project\\CSV\\PROCESSOR.csv", index=False)
            print("DONE, SUCCESSFULLY MODIFIED!!")
        elif i=="2":
            w=int(input("Enter new quantity:"))
            PROCESSOR.loc[PROCESSOR['serial_no'] == q, 'quantity_available'] = w
            PROCESSOR.to_csv("F:\\Project\\CSV\\PROCESSOR.csv", index=False)
            print("DONE, SUCCESSFULLY MODIFIED!!")
        else:
            print("INPUT INVALID!!")
    elif m==3:
        print(GRAPHIC_CARD[['serial_no','name','quantity_available']])
        q=int(input("Enter Graphic card Serial No to MODIFY:"))
        i=input("What to edit(1 for name and 2 for quantity:)")
        if i=="1":
            w=input("Enter Graphic card NEW Name to MODIFY:")
            GRAPHIC_CARD.loc[GRAPHIC_CARD['serial_no'] == q, 'name']= w
            GRAPHIC_CARD.to_csv("F:\\Project\\CSV\\GRAPHIC_CARD.csv", index=False)
            print("DONE, SUCCESSFULLY MODIFIED!!")
        elif i=="2":
            w=int(input("Enter new quantity:"))
            GRAPHIC_CARD.loc[GRAPHIC_CARD['serial_no'] == q, 'quantity_available'] = w
            GRAPHIC_CARD.to_csv("F:\\Project\\CSV\\GRAPHIC_CARD.csv", index=False)
            print("DONE, SUCCESSFULLY MODIFIED!!")
        else:
            print("INPUT INVALID!!")
    elif m==4:
        print(RAM[['serial_no','name','quantity_available']])
        q=int(input("Enter RAM Serial No to MODIFY:"))
        i=input("What to edit(1 for name and 2 for quantity:)")
        if i=="1":
            w=input("Enter RAM NEW Name to MODIFY:")
            RAM.loc[RAM['serial_no'] == q, 'name']= w
            RAM.to_csv("F:\\Project\\CSV\\RAM.csv", index=False)
            print("DONE, SUCCESSFULLY MODIFIED!!")
        elif i=="2":
            w=int(input("Enter new quantity:"))
            RAM.loc[RAM['serial_no'] == q, 'quantity_available'] = w
            RAM.to_csv("F:\\Project\\CSV\\RAM.csv", index=False)
            print("DONE, SUCCESSFULLY MODIFIED!!")
        else:
            print("INPUT INVALID!!")
    elif m==5:
        print(SSD[['serial_no','name','quantity_available']])
        q=int(input("Enter SSD Serial No to MODIFY:"))
        i=input("What to edit(1 for name and 2 for quantity:)")
        if i=="1":
            w=input("Enter SSD NEW Name to MODIFY:")
            SSD.loc[SSD['serial_no'] == q, 'name']= w
            SSD.to_csv("F:\\Project\\CSV\\SSD.csv", index=False)
            print("DONE, SUCCESSFULLY MODIFIED!!")
        elif i=="2":
            w=int(input("Enter new quantity:"))
            SSD.loc[SSD['serial_no'] == q, 'quantity_available'] = w
            SSD.to_csv("F:\\Project\\CSV\\SSD.csv", index=False)
            print("DONE, SUCCESSFULLY MODIFIED!!")
        else:
            print("INPUT INVALID!!")
    elif m==6:
        print(MOUSE[['serial_no','name','quantity_available']])
        q=int(input("Enter MOUSE Serial No to MODIFY:"))
        i=input("What to edit(1 for name and 2 for quantity:)")
        if i=="1":
            w=input("Enter MOUSE NEW Name to MODIFY:")
            MOUSE.loc[MOUSE['serial_no'] == q, 'name']= w
            MOUSE.to_csv("F:\\Project\\CSV\\MOUSE.csv", index=False)
            print("DONE, SUCCESSFULLY MODIFIED!!")
        elif i=="2":
            print(MOUSE[['serial_no','name','quantity_available']])
            w=int(input("Enter new quantity:"))
            print(w)
            MOUSE.loc[MOUSE['serial_no'] == q, 'quantity_available'] = w
            print(MOUSE[['serial_no','name','quantity_available']])
            MOUSE.to_csv("F:\\Project\\CSV\\MOUSE.csv", index=False)
            print("DONE, SUCCESSFULLY MODIFIED!!")
        else:
            print("INPUT INVALID!!")
    elif m==7:
        print(KEYBOARD[['serial_no','name','quantity_available']])
        q=int(input("Enter KEYBOARD Serial No to MODIFY:"))
        i=input("What to edit(1 for name and 2 for quantity:)")
        if i=="1":
            w=input("Enter KEYBOARD NEW Name to MODIFY:")
            KEYBOARD.loc[KEYBOARD['serial_no'] == q, 'name']= w
            KEYBOARD.to_csv("F:\\Project\\CSV\\KEYBOARD.csv", index=False)
            print("DONE, SUCCESSFULLY MODIFIED!!")
        elif i=="2":
            w=int(input("Enter new quantity:"))
            KEYBOARD.loc[KEYBOARD['name'] == q, 'quantity_available'] = w
            main.to_csv("F:\\Project\\CSV\\KEYBOARD.csv", index=False)
            print("DONE, SUCCESSFULLY MODIFIED!!")
        else:
            print("INPUT INVALID!!")
    else:
            print("INPUT NOT SASTISFISTESD")

ADMIN()

import pandas as pd,numpy as np

def ADMIN_ADD_ITEM():
    main=pd.read_csv("F:\\Project\\CSV\\MAIN.csv")
    LAPTOP="F:\\Project\\CSV\\LAPTOP.csv"
    PROCESSOR="F:\\Project\\CSV\\PROCESSOR.csv"
    GRAPHIC_CARD="F:\\Project\\CSV\\GRAPHICS_CARD.csv"
    RAM="F:\\Project\\CSV\\RAM.csv"
    SSD="F:\\Project\\CSV\\SSD.csv"
    MOUSE="F:\\Project\\CSV\\MOUSE.csv"
    KEYBOARD="F:\\Project\\CSV\\KEYBOARD.csv"
    print("Which type of item do you want to add?")
    print(main[['serial_no','name']])
    m=int(input("Press the corresponding SERIAL NO.:"))
    l=[LAPTOP,PROCESSOR,GRAPHIC_CARD,RAM,SSD,MOUSE,KEYBOARD]
    l1=["LAPTOP","PROCESSOR","GRAPHIC_CARD","RAM","SSD","MOUSE","KEYBOARD"]
    a=len(l)
    if m-1<=a:
        df=pd.read_csv(l[m-1])
        max_s_no=df['serial_no'].max()
        q=input("Enter Name:")
        w=int(input("Enter quantity build:"))
        new_data={'serial_no':max_s_no+1,'name':q,'quantity_available':w,'quantity_sold':0}
        NEW_DATA=pd.DataFrame([new_data])
        df=pd.concat([df,NEW_DATA], ignore_index=True)
        df.to_csv(l[m-1], index=False)
        main.loc[main['name'] == l1[m-1], 'no_of_products'] =main.loc[main['name'] == l1[m-1], 'no_of_products']+1
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
    
    else:
        print("INPUT NOT SASTISFISTESD")
        ADMIN_ADD_ITEM()

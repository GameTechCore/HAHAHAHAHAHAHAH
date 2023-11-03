def ADMIN_MODIFY_ITEM():
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

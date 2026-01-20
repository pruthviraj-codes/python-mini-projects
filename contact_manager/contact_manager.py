contact = []
 
while True:

    print("--Contact Manager---")
    print(" 1.Add contact: ")
    print(" 2.Remove Contact")
    print(" 3.search contact")
    print(" 4.Show all contact")
    print(" 5.Exit")

    try:
        choice = int(input("Enetr your choice: "))
    except ValueError:
        print("please enter vaalid number")
    
    if(choice == 1):
        name = input("ENter name : ")
        contact.append(name)

        print(contact)
    elif(choice == 2):
        name = input("Enter name ")
        if name in contact:
            contact.remove(name)
            print("Contact removed sucessfully")
        else:
            print("Contact not found ")
        
    elif(choice  == 3):
        name = input("Enter name:")
        if name in contact:
            print(f"Found:{name}")
        else:
            print("Contact not found")

    elif(choice == 4):
        print("All contact ",contact)
    elif(choice == 5):
        print("Exiting Contact Manager ")
        break

    else:
        print("Invalid choice. Please select 1-5 ")
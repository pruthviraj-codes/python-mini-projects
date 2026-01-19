contact = []
 
while True:

    print("--Contact Manager---")
    print(" 1.Add contact: ")
    print(" 2.Remove Contact")
    print(" 3.search contact")
    print(" 4.Show all contact")
    print(" 5.Exit")


    choice = int(input("Enetr your choice: "))

    if(choice == 1):
        name = input("ENter name : ")
        contact.append(name)

        print(contact)
    elif(choice == 2):
        name = input("Enter name ")
        if name in contact:
            contact.remove(name)
        print(contact)
    elif(choice  == 3):
        name = input("Enter name:")
        if name in contact:
            print("Found: ")
    elif(choice == 4):
        print("All contact ",contact)
    else:
        print("Exit the code: ")
        break

else:
    print("INvalid choice: ")
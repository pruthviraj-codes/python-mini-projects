student= {}

while True:
    print("--Studnet YSystem---")
    print(" 1.Add stduent: ")
    print(" 2.Remove student")
    print(" 3.search student")
    print(" 4.Show all studnet")
    print(" 5.Exit")

    choice = int(input("Enetr your choice: "))

    if(choice == 1):
        name = input("enter name : ")
        key = int(input("Enter value: "))
        student[name] = key

        print(student)

    elif(choice == 2):
        name = input("enter name : ")
         
        del student[name]

        print(student)

    elif(choice == 3):
        name = input("enter name : ")
         
        student[name]
        if name in student:
            print("Found ")
        else:
            print("not found")
        print(student)
    elif(choice == 4):
        print("Show all studet",student)
    elif(choice == 5):
        print("Done")
        break

    else:
        print("Invalid choice")
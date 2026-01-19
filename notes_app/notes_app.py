def notes_app():
    while True:
        print("\n--- NOTES APP ---")
        print("1. Write note")
        print("2. View notes")
        print("3.Append note")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            note = input("Enter your note: ")
            with open("notes.txt", "w") as f:
                f.write(note + "\n")
            print("Note saved")

        elif choice == 2:
            with open("notes.txt", "r") as f:
                print("\n--- Your Notes ---")
                print(f.read())

        elif choice == 3:
           with open("notes.txt", "a") as f:
                note = input("Append your note: ")
                f.write(note)
           
        elif choice == 4:
            print("Exited successfully")
            break
        else:
            print("Invalid choice")


notes_app()




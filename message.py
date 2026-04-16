try:
    file = open("message.txt", "x")
    print("File created successfully.")
    file.close()
except FileExistsError:
    print("Error: File already exists.")

while True:
    print("\nMenu:")
    print("1. Send a message")
    print("2. View all messages")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        message = input("Enter your message: ")
        try:
            file = open("message.txt", "a")
            file.write(message + "\n")
            file.close()
            print("Message saved.")
        except Exception as e:
            print("Error writing to file:", e)

    elif choice == "2":
        try:
            file = open("message.txt", "r")
            print("\nMessages:")
            print(file.read())
            file.close()
        except Exception as e:
            print("Error reading file:", e)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
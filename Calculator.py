def calculator():


    while True:
        try:
            first_number = int(input("Please enter your first number: "))
            second_number = int(input("Please enter your second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        print("1.plus")
        print("2.minus")
        print("3.divide")
        print("4.Multiplication")
        print("5.Exit")


        choice = input("please enter your choice: ")
        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice")
            continue

        if choice == "1":
            print(first_number + second_number)
        elif choice == "2":
            print(first_number - second_number)
        elif choice == "3":
            try:
                print(first_number / second_number)
            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")

        elif choice == "4":
            print(first_number * second_number)

        elif choice == "5":
            print("Thank you for using this program")
            break

        else:
            print("invalid choice")

        while True:
            again = input("Do you want to continue? (y/n): ").lower()

            if again == "y":
                break
            elif again == "n":
                print("Goodbye!")
                return
            else:
                print("Invalid choice. Please enter y or n.")


calculator()

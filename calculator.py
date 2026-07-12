def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def divide(a, b):
    return a / b


def multiplication(a, b):
    return a * b



def calculator():


    while True:
        try:
            first_number = float(input("Please enter your first number: "))
            second_number = float(input("Please enter your second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        print("1.plus")
        print("2.minus")
        print("3.divide")
        print("4.Multiplication")


        choice = input("please enter your choice: ")
        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice")
            continue

        if choice == "1":
            print(plus(first_number, second_number))

        elif choice == "2":
            print(minus(first_number, second_number))

        elif choice == "3":
            try:
                print(divide(first_number, second_number))
            except ZeroDivisionError:
                print("cannot divide by zero.")

        elif choice == "4":
            print(multiplication(first_number, second_number))



        while True:
            again = input("Do you want to continue? (y/n): ").lower()

            if again == "y":
                break
            elif again == "n":
                print("Goodbye!")
                return
            else:
                print("Invalid choice. Please enter y or n.")


if __name__ == "__main__":
    calculator()

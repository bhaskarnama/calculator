# ==========================================
#        PYTHON CALCULATOR
# ==========================================

def calculator():

    print("\n==============================")
    print("       PYTHON CALCULATOR")
    print("==============================")

    while True:

        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Power (**)")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        # Exit
        if choice == "7":
            print("\nThank you for using the calculator! 👋")
            break

        # Check valid choice
        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("❌ Invalid choice. Please try again.")
            continue

        # Get numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Please enter valid numbers.")
            continue

        # Perform calculation

        if choice == "1":
            result = num1 + num2
            operator = "+"

        elif choice == "2":
            result = num1 - num2
            operator = "-"

        elif choice == "3":
            result = num1 * num2
            operator = "*"

        elif choice == "4":
            if num2 == 0:
                print("❌ Cannot divide by zero.")
                continue

            result = num1 / num2
            operator = "/"

        elif choice == "5":
            if num2 == 0:
                print("❌ Cannot perform modulus by zero.")
                continue

            result = num1 % num2
            operator = "%"

        elif choice == "6":
            result = num1 ** num2
            operator = "**"

        print("\n------------------------------")
        print(f"Result: {num1:g} {operator} {num2:g} = {result:g}")
        print("------------------------------")


# Start calculator
calculator()


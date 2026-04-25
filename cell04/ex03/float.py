def main():
    try:
        user_input = input("Give me a number: ").strip()

        number = float(user_input)

        if number.is_integer():
            print("This number is an integer.")
            
        else:
            print("This number is a decimal.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
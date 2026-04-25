import math

def main():
    try:
        user_input = input("Give me a number: ").strip()
        number = float(user_input)

        # Round up to the nearest integer
        result = math.ceil(number)

        print(result)

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

#WIP

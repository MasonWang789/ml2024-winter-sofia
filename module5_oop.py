from module5_mod import NumberProcessor

def main():
    processor = NumberProcessor()

    # Read N
    processor.read_n()

    # Read N numbers
    processor.read_numbers()

    # Read X
    while True:
        try:
            x = int(input("Enter an integer X: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Search for X in the list of numbers
    result = processor.search_number(x)

    # Output result
    if result == -1:
        print("The number {} was not among the provided numbers.".format(x))
    else:
        print("The index of {} is: {}".format(x, result))

if __name__ == "__main__":
    main()

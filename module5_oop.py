class NumberProcessor:
    def __init__(self):
        self.numbers = []

    def read_n_numbers(self, n):
        for i in range(n):
            num = int(input(f"Enter number {i+1}: "))
            self.numbers.append(num)

    def find_index_of_x(self, x):
        try:
            index = self.numbers.index(x) + 1
            return index
        except ValueError:
            return -1

def main():
    try:
        N = int(input("Enter the number of elements (N): "))
        if N <= 0:
            print("N should be a positive integer.")
            return

        number_processor = NumberProcessor()
        number_processor.read_n_numbers(N)

        X = int(input("Enter the number to search (X): "))

        index = number_processor.find_index_of_x(X)
        if index == -1:
            print(f"The number {X} was not found among the provided numbers.")
        else:
            print(f"The index of {X} is: {index}")

    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()

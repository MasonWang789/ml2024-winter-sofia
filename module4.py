def find_index_of_x(n, numbers, x):
    for i in range(n):
        if numbers[i] == x:
            return i + 1
    return -1

def main():
    # Get input N
    n = int(input("Enter a positive integer N: "))
    
    # Get N numbers from the user
    numbers = []
    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    
    # Get input X
    x = int(input("Enter an integer X: "))
    
    # Find the index of X in the list of numbers
    result = find_index_of_x(n, numbers, x)
    
    # Output the result
    print(f"Result: {result}")

if __name__ == "__main__":
    main()

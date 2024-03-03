import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    # Ask the user for input N (positive integer)
    N = int(input("Enter the number of points (N): "))

    # Initialize arrays to store ground truth (X) and predicted class labels (Y)
    X = np.zeros(N, dtype=int)
    Y = np.zeros(N, dtype=int)

    # Read N (x, y) points from the user
    for i in range(N):
        x = int(input(f"Enter x value for point {i+1} (0 or 1): "))
        y = int(input(f"Enter y value for point {i+1} (0 or 1): "))
        X[i] = x
        Y[i] = y

    # Calculate Precision and Recall
    precision = precision_score(X, Y)
    recall = recall_score(X, Y)

    # Output the results
    print(f"\nPrecision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()

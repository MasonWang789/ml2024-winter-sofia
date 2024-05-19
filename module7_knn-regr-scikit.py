import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    # Step 1: Get input N (number of points)
    N = int(input("Enter the number of points (N): "))
    if N <= 0:
        print("N must be a positive integer.")
        return

    # Step 2: Get input k (number of neighbors)
    k = int(input("Enter the number of neighbors (k): "))
    if k <= 0:
        print("k must be a positive integer.")
        return

    # Step 3: Read N (x, y) points
    points = []
    for i in range(N):
        x = float(input(f"Enter x value for point {i+1}: "))
        y = float(input(f"Enter y value for point {i+1}: "))
        points.append((x, y))

    # Convert points to numpy array
    points = np.array(points)

    # Step 4: Get input X for prediction
    X_pred = float(input("Enter the X value for prediction: "))

    # Check if k <= N
    if k > N:
        print("Error: k should be less than or equal to N.")
        return

    # Separate the points into X (features) and y (labels)
    X = points[:, 0].reshape(-1, 1)
    y = points[:, 1]

    # Calculate variance of the labels in the training dataset
    variance = np.var(y)
    print(f"Variance of the labels in the training dataset: {variance}")

    # Step 5: Perform k-NN Regression
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X, y)

    # Predict the Y value for the given X_pred
    Y_pred = knn.predict(np.array([[X_pred]]))
    print(f"The predicted Y value for X = {X_pred} is: {Y_pred[0]}")

if __name__ == "__main__":
    main()

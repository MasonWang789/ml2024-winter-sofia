import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

# Function to get input from the user and perform k-NN Regression
def k_nn_regression():
    try:
        # Input N (number of points)
        N = int(input("Enter the number of points (N): "))
        if N <= 0:
            print("N should be a positive integer.")
            return

        # Input k (number of neighbors)
        k = int(input("Enter the value of k (positive integer): "))
        if k <= 0 or k > N:
            print("k should be a positive integer less than or equal to N.")
            return

        # Input (x, y) points
        points = []
        for i in range(N):
            x = float(input(f"Enter x value for point {i + 1}: "))
            y = float(input(f"Enter y value for point {i + 1}: "))
            points.append((x, y))

        # Convert points to NumPy array
        points_array = np.array(points)

        # Input X for prediction
        X_value = float(input("Enter the value of X for prediction: "))

        # Separate features (x values) and target (y values)
        X = points_array[:, 0].reshape(-1, 1)
        y = points_array[:, 1]

        # Perform k-NN Regression
        knn_reg = KNeighborsRegressor(n_neighbors=k)
        knn_reg.fit(X, y)
        y_pred = knn_reg.predict(np.array([[X_value]]))

        # Calculate coefficient of determination (R^2)
        r2 = r2_score(y, knn_reg.predict(X))

        # Output the result and coefficient of determination
        print(f"Result (Y) of k-NN Regression: {y_pred[0]}")
        print(f"Coefficient of Determination (R^2): {r2}")

    except ValueError as e:
        print(f"Error: {e}")

# Run the program
k_nn_regression()

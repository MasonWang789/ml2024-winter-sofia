import numpy as np
from sklearn.metrics import precision_score, recall_score

def get_user_input():
    N = int(input("Enter the number of points (N): "))
    points = np.zeros((N, 2), dtype=int)
    
    for i in range(N):
        x = int(input(f"Enter x value for point {i+1} (0 or 1): "))
        y = int(input(f"Enter y value for point {i+1} (0 or 1): "))
        points[i] = [x, y]
    
    return points

def main():
    points = get_user_input()
    x = points[:, 0]  # Ground truth labels
    y = points[:, 1]  # Predicted labels
    
    precision = precision_score(x, y)
    recall = recall_score(x, y)
    
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()

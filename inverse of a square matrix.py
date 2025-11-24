#to find the inverse of a square matrix of n x n dimensions from user input
import numpy as np
def inverse_matrix(matrix):
    try:
        inv_matrix = np.linalg.inv(matrix)
        return inv_matrix
    except np.linalg.LinAlgError:
        return "Matrix is singular and cannot be inverted."
if __name__ == "__main__":
    n = int(input("Enter the dimension n for an n x n matrix: "))
    print(f"Enter the elements of the {n} x {n} matrix row-wise:")
    elements = []
    for i in range(n):
        row = list(map(float, input().split()))
        if len(row) != n:
            print(f"Please enter exactly {n} elements for row {i + 1}.")
            exit(1)
        elements.append(row)
    matrix = np.array(elements)
    result = inverse_matrix(matrix)
    print("Inverse of the matrix:")
    print(result)
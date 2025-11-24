#to find the determinant of a n x n matrix from user input
import numpy as np
def determinant(matrix):
    """
    Calculate the determinant of a square matrix.

    Parameters:
    matrix (list of list of floats): A square matrix represented as a list of lists.

    Returns:
    float: The determinant of the matrix.
    """
    np_matrix = np.array(matrix)
    return np.linalg.det(np_matrix)
if __name__ == "__main__":
    n = int(input("Enter the size of the matrix (n x n): "))
    matrix = []
    print("Enter the elements of the matrix row by row:")
    for i in range(n):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        if len(row) != n:
            raise ValueError("Each row must have exactly n elements.")
        matrix.append(row)
    det = determinant(matrix)
    print(f"The determinant of the matrix is: {round(det,2)}")

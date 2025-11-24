#to find the result of a matrix multiplication from user input
import numpy as np
def matrix_multiplication():
    # Get the dimensions of the first matrix
    rows_a = int(input("Enter the number of rows for the first matrix: "))
    cols_a = int(input("Enter the number of columns for the first matrix: "))

    # Get the elements of the first matrix
    print("Enter the elements of the first matrix row-wise:")
    matrix_a = []
    for i in range(rows_a):
        row = list(map(int, input().split()))
        matrix_a.append(row)

    # Get the dimensions of the second matrix
    rows_b = int(input("Enter the number of rows for the second matrix: "))
    cols_b = int(input("Enter the number of columns for the second matrix: "))

    # Check if multiplication is possible
    if cols_a != rows_b:
        print("Matrix multiplication not possible with these dimensions.")
        return

    # Get the elements of the second matrix
    print("Enter the elements of the second matrix row-wise:")
    matrix_b = []
    for i in range(rows_b):
        row = list(map(int, input().split()))
        matrix_b.append(row)

    # Convert lists to numpy arrays
    a = np.array(matrix_a)
    b = np.array(matrix_b)

    # Perform matrix multiplication
    result = np.dot(a, b)

    # Print the result
    print("Resultant Matrix after multiplication:")
    print(result)
if __name__ == "__main__":
    matrix_multiplication()
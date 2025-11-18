#a python programme used to find the roots of a polynomial equation using the numpy library
import numpy as np
def find_roots(coefficients):
    """
    This function takes a list of coefficients of a polynomial equation
    and returns its roots.
    
    Parameters:
    coefficients (list): A list of coefficients [a_n, a_(n-1), ..., a_1, a_0]
                         representing the polynomial a_n*x^n + a_(n-1)*x^(n-1) + ... + a_1*x + a_0
    
    Returns:
    numpy.ndarray: An array of roots of the polynomial equation.
    """
    # Use numpy's roots function to find the roots of the polynomial
    roots = np.roots(coefficients)
    return roots
# Example usage
if __name__ == "__main__":
    # Coefficients for the polynomial equation x^3 - 6x^2 + 11x - 6
    coefficients = eval(input("Enter the coefficients of the polynomial as a list (e.g., [1, -6, 11, -6]): "))
    roots = find_roots(coefficients)
    print("The roots of the polynomial are:", roots)

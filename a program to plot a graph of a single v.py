#a program to plot a graph of a single variable function using matplotlib from user input
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import re
import sys
from sympy.parsing.sympy_parser import parse_expr
def is_valid_expression(expr):
    # Check for invalid characters
    if re.search(r'[^0-9a-zA-Z+\-*/^(). ]', expr):
        return False
    # Check for balanced parentheses
    stack = []
    for char in expr:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    return True
def main():
    x = sp.symbols('x')
    user_input = input("Enter a single variable function in terms of x (e.g., sin(x), x**2 + 3*x + 2): ")
    if not is_valid_expression(user_input):
        print("Invalid expression. Please use only valid mathematical expressions with variable x.")
        sys.exit(1)
    try:
        expr = parse_expr(user_input, evaluate=False)
    except Exception as e:
        print(f"Error parsing expression: {e}")
        sys.exit(1)
    func = sp.lambdify(x, expr, modules=['numpy'])
    x_vals = np.linspace(-10, 10, 400)
    try:
        y_vals = func(x_vals)
    except Exception as e:
        print(f"Error evaluating function: {e}")
        sys.exit(1)
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=f'y = {user_input}')
    plt.title('Graph of the function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.ylim(-10, 10)
    plt.show()
if __name__ == "__main__":
    main()

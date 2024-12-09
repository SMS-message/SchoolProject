import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def plot_function():
    equation_str = ...
    x = sp.symbols('x')
    try:
        equation = sp.sympify(equation_str)
    except sp.SympifyError:
        print("Ошибка: некорректное математическое выражение.")
        return
    f = sp.lambdify(x, equation, "numpy")
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f(x_vals)
    plt.plot(x_vals, y_vals, color='black', linestyle='-', linewidth=1)
    plt.title(f'График функции: {equation_str}')
    plt.xlabel('ось x')
    plt.ylabel('ось y')
    plt.title(f'график функции y = {equation_str}')
    plt.grid(True)
    plt.show()
plot_function()
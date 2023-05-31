import numpy as np
import matplotlib.pyplot as plt

def generate_knot_vector(num_control_points):
    """
    Generates a knot vector for cubic B-spline interpolation.

    Args:
        num_control_points (int): Number of control points.

    Returns:
        numpy.ndarray: The knot vector.
    """
    knot_vector = np.zeros(num_control_points + 4)
    knot_vector[2:-2] = np.linspace(0, 1, num_control_points)
    return knot_vector

def bspline_basis(i, degree, knot_vector, t):
    """
    Computes the value of a B-spline basis function at a given parameter value.

    Args:
        i (int): Index of the basis function.
        degree (int): Degree of the B-spline basis.
        knot_vector (numpy.ndarray): The knot vector.
        t (float): Parameter value at which to evaluate the basis function.

    Returns:
        float: The value of the B-spline basis function at the given parameter value.
    """
    if degree == 0:
        return 1.0 if knot_vector[i] <= t < knot_vector[i + 1] else 0.0

    numerator1 = t - knot_vector[i]
    denominator1 = knot_vector[i + degree] - knot_vector[i]

    if denominator1 == 0.0:
        coefficient1 = 0.0
    else:
        coefficient1 = numerator1 / denominator1 * bspline_basis(i, degree - 1, knot_vector, t)

    numerator2 = knot_vector[i + degree + 1] - t
    denominator2 = knot_vector[i + degree + 1] - knot_vector[i + 1]

    if denominator2 == 0.0:
        coefficient2 = 0.0
    else:
        coefficient2 = numerator2 / denominator2 * bspline_basis(i + 1, degree - 1, knot_vector, t)

    return coefficient1 + coefficient2

def evaluate_basis_functions(knot_vector, degree, t):
    """
    Evaluates the B-spline basis functions at a given parameter value.

    Args:
        knot_vector (numpy.ndarray): The knot vector.
        degree (int): Degree of the B-spline basis.
        t (float): Parameter value at which to evaluate the basis functions.

    Returns:
        list: List of values of the B-spline basis functions at the given parameter value.
    """
    basis_functions = []
    for i in range(len(knot_vector) - degree - 1):
        basis_functions.append(bspline_basis(i, degree, knot_vector, t))
    return basis_functions

def interpolate_points(control_points, knot_vector, data_points):
    """
    Performs cubic B-spline interpolation.

    Args:
        control_points (numpy.ndarray): Control points.
        knot_vector (numpy.ndarray): The knot vector.
        data_points (numpy.ndarray): Points at which to interpolate.

    Returns:
        tuple: Tuple containing interpolated x-coordinates and y-coordinates.
    """
    interpolated_values_x = []
    interpolated_values_y = []
    for t in data_points:
        basis_functions = evaluate_basis_functions(knot_vector, 3, t)
        weighted_sum = np.dot(basis_functions, control_points)
        interpolated_values_x.append(weighted_sum[0])
        interpolated_values_y.append(weighted_sum[1])
    return interpolated_values_x, interpolated_values_y


def plot_interpolated_curve(data_points, interpolated_values_x, interpolated_values_y):
    """
    Plots the interpolated curve.

    Args:
        data_points (numpy.ndarray): Points at which the curve is interpolated.
        interpolated_values_x (numpy.ndarray): Interpolated x-coordinates.
        interpolated_values_y (numpy.ndarray): Interpolated y-coordinates.
    """
    plt.scatter(data_points, interpolated_values_x, color='red', label='Interpolated')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()


def main():
    # Control points for interpolation
    control_points = np.array([[0, 0], [1, 3], [2, -1], [3, 2], [4, 0]])

    # Generate knot vector
    knot_vector = generate_knot_vector(len(control_points))

    # Points at which to interpolate the curve
    data_points = np.linspace(0, 4, 100)

    # Perform interpolation
    interpolated_values_x, interpolated_values_y = interpolate_points(control_points, knot_vector, data_points)

    # Plot the interpolated curve
    plot_interpolated_curve(data_points, interpolated_values_x, interpolated_values_y)

if __name__ == '__main__':
    main()

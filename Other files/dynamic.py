import requests
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import io

def generate_knot_vector(num_control_points):
    knot_vector = np.zeros(num_control_points + 4)
    knot_vector[2:-2] = np.linspace(0, 1, num_control_points)
    return knot_vector

def bspline_basis(i, degree, knot_vector, t):
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

def interpolate_image(control_points, knot_vector, image):
    width, height = image.size
    pixel_values = np.array(image)

    interpolated_image = np.zeros_like(pixel_values)

    for y in range(height):
        for x in range(width):
            t_x = x / (width - 1)  # Normalize x coordinate
            t_y = y / (height - 1)  # Normalize y coordinate

            basis_functions_x = evaluate_basis_functions(knot_vector, 3, t_x)
            basis_functions_y = evaluate_basis_functions(knot_vector, 3, t_y)

            for c in range(3):  # Iterate over RGB channels
                weighted_sum = 0.0
                for i in range(len(control_points)):
                    control_point_x = int(control_points[i][0] * (width - 1))
                    control_point_y = int(control_points[i][1] * (height - 1))
                    weighted_sum += basis_functions_x[i] * basis_functions_y[i] * pixel_values[min(control_point_y, height - 1), min(control_point_x, width - 1), c]

                interpolated_image[y, x, c] = weighted_sum

    return Image.fromarray(interpolated_image.astype(np.uint8))

def evaluate_basis_functions(knot_vector, degree, t):
    basis_functions = []
    for i in range(len(knot_vector) - degree - 1):
        basis_functions.append(bspline_basis(i, degree, knot_vector, t))
    return basis_functions

def generate_control_points(image_size):
    num_points = 5  # Number of control points in each dimension
    x_step = image_size[0] / (num_points - 1)
    y_step = image_size[1] / (num_points - 1)
    control_points = []
    for i in range(num_points):
        for j in range(num_points):
            control_points.append([i * x_step, j * y_step])
    return np.array(control_points)

def main():
    image_url = "https://yt3.googleusercontent.com/tPXs09w0guC3IZQHw7uvgU6EINaViTtQhFyR_qYYSoxU9DuKFvYklC4Gq2ymRtFf2zIouHW2AQ=s900-c-k-c0x00ffffff-no-rj"  # Replace with the actual image URL

    # Download the image
    response = requests.get(image_url)
    image = Image.open(io.BytesIO(response.content))

    control_points = generate_control_points(image.size)
    knot_vector = generate_knot_vector(len(control_points))

    interpolated_image = interpolate_image(control_points, knot_vector, image)

    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image)

    plt.subplot(1, 2, 2)
    plt.title('Interpolated Image')
    plt.imshow(interpolated_image)

    plt.show()


if __name__ == '__main__':
    main()

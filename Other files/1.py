import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def cox_de_boor(t, k, i, u):
    if k == 0:
        return 1.0 if t[i] <= u < t[i+1] else 0.0

    denominator1 = t[i+k] - t[i]
    term1 = 0.0 if denominator1 == 0.0 else (u - t[i]) / denominator1 * cox_de_boor(t, k-1, i, u)

    denominator2 = t[i+k+1] - t[i+1]
    term2 = 0.0 if denominator2 == 0.0 else (t[i+k+1] - u) / denominator2 * cox_de_boor(t, k-1, i+1, u)

    return term1 + term2

def interpolate_image(image, scale_factor):
    # Convert the image to grayscale
    image = image.convert('L')

    # Convert the image to a numpy array
    pixel_values = np.array(image)

    # Compute the new dimensions based on the scale factor
    new_width = int(pixel_values.shape[1] * scale_factor)
    new_height = int(pixel_values.shape[0] * scale_factor)

    # Generate the knots for the spline interpolation
    knots_x = np.linspace(0, pixel_values.shape[1] - 1, new_width)
    knots_y = np.linspace(0, pixel_values.shape[0] - 1, new_height)

    # Create the interpolated image
    interpolated_image = np.zeros((new_height, new_width), dtype=np.uint8)

    # Perform interpolation
    for j in range(new_height):
        for i in range(new_width):
            x = knots_x[i]
            y = knots_y[j]

            u = int(x)
            v = int(y)

            sum_value = 0.0

            for l in range(-1, 3):
                for m in range(-1, 3):
                    if 0 <= v + m < pixel_values.shape[0] and 0 <= u + l < pixel_values.shape[1]:
                        weight = cox_de_boor(knots_x, 3, u + l, x) * cox_de_boor(knots_y, 3, v + m, y)
                        sum_value += pixel_values[v + m, u + l] * weight

            interpolated_image[j, i] = int(round(sum_value))

    # Convert the interpolated values back to an image
    interpolated_image = Image.fromarray(interpolated_image)

    return interpolated_image

def main():
    # Load the original image
    image = Image.open('team.jpeg')

    # Adjust the scale factor
    scale_factor = 2.0

    # Perform interpolation and get the interpolated image
    interpolated_image = interpolate_image(image, scale_factor)

    # Display the original and interpolated images
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image, cmap='gray')

    plt.subplot(1, 2, 2)
    plt.title('Interpolated Image')
    plt.imshow(interpolated_image, cmap='gray')

    plt.show()

if __name__ == '__main__':
    main()

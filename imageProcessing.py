import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def interpolate_image(image, scale_factor):
    # Convert the image to a numpy array
    pixel_values = np.array(image)

    # Compute the new dimensions based on the scale factor
    new_width = int(pixel_values.shape[1] * scale_factor)
    new_height = int(pixel_values.shape[0] * scale_factor)

    # Create an array to store the interpolated image
    interpolated_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    # Compute the step size for the new grid
    step_x = pixel_values.shape[1] / new_width
    step_y = pixel_values.shape[0] / new_height

    # Perform cubic B-spline interpolation
    for j in range(new_height):
        for i in range(new_width):
            x = i * step_x
            y = j * step_y

            # Compute the grid indices
            x0 = int(x)
            y0 = int(y)
            x1 = x0 + 1 if x0 < pixel_values.shape[1] - 1 else x0
            y1 = y0 + 1 if y0 < pixel_values.shape[0] - 1 else y0

            # Compute the fractional part
            dx = x - x0
            dy = y - y0

            # Compute the weights
            w00 = (1 - dx) * (1 - dy)
            w01 = (1 - dx) * dy
            w10 = dx * (1 - dy)
            w11 = dx * dy

            # Compute the interpolated pixel values
            sum_r = w00 * pixel_values[y0, x0, 0] + w01 * pixel_values[y1, x0, 0] + w10 * pixel_values[y0, x1, 0] + w11 * pixel_values[y1, x1, 0]
            sum_g = w00 * pixel_values[y0, x0, 1] + w01 * pixel_values[y1, x0, 1] + w10 * pixel_values[y0, x1, 1] + w11 * pixel_values[y1, x1, 1]
            sum_b = w00 * pixel_values[y0, x0, 2] + w01 * pixel_values[y1, x0, 2] + w10 * pixel_values[y0, x1, 2] + w11 * pixel_values[y1, x1, 2]
            weight_sum = w00 + w01 + w10 + w11

            if weight_sum != 0:
                interpolated_image[j, i, 0] = int(round(sum_r / weight_sum))
                interpolated_image[j, i, 1] = int(round(sum_g / weight_sum))
                interpolated_image[j, i, 2] = int(round(sum_b / weight_sum))
            else:
                interpolated_image[j, i, 0] = 0
                interpolated_image[j, i, 1] = 0
                interpolated_image[j, i, 2] = 0

    # Convert the interpolated values back to an image
    interpolated_image = Image.fromarray(interpolated_image)

    return interpolated_image


def main():
    image_path = "photo.jpg"
    scale_factor = 8.0

    # Open the original image
    image = Image.open(image_path)

    # Perform interpolation and get the interpolated image
    interpolated_image = interpolate_image(image, scale_factor)

    # Display the input and output images side by side
    fig, axs = plt.subplots(1, 2)
    axs[0].imshow(image)
    axs[0].set_title('Input Image')
    axs[0].axis('off')
    axs[1].imshow(interpolated_image)
    axs[1].set_title('Interpolated Image')
    axs[1].axis('off')
    plt.show()


if __name__ == '__main__':
    main()

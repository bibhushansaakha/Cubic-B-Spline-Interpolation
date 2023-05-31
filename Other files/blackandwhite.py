import numpy as np
from PIL import Image
from scipy.interpolate import RectBivariateSpline
import requests
import io
import matplotlib.pyplot as plt

def interpolate_image(image, scale_factor):
    # Convert the image to grayscale
    image = image.convert('L')

    # Convert the image to a numpy array
    pixel_values = np.array(image)

    # Compute the new dimensions based on the scale factor
    new_width = int(pixel_values.shape[1] * scale_factor)
    new_height = int(pixel_values.shape[0] * scale_factor)

    # Create a grid of coordinates for the original image
    x = np.arange(pixel_values.shape[1])
    y = np.arange(pixel_values.shape[0])
    grid_x, grid_y = np.meshgrid(x, y)

    # Create a grid of coordinates for the interpolated image
    new_x = np.linspace(0, pixel_values.shape[1] - 1, new_width)
    new_y = np.linspace(0, pixel_values.shape[0] - 1, new_height)
    new_grid_x, new_grid_y = np.meshgrid(new_x, new_y)

    # Create a cubic B-spline interpolator
    spline = RectBivariateSpline(y, x, pixel_values, kx=3, ky=3)

    # Perform cubic B-spline interpolation on the grid
    interpolated_values = spline.ev(new_grid_y, new_grid_x)

    # Rescale the interpolated values to [0, 255]
    interpolated_values = np.clip(interpolated_values, 0, 255).astype(np.uint8)

    # Convert the interpolated values back to an image
    interpolated_image = Image.fromarray(interpolated_values)

    return interpolated_image


def main():
    image_url = "https://yt3.googleusercontent.com/tPXs09w0guC3IZQHw7uvgU6EINaViTtQhFyR_qYYSoxU9DuKFvYklC4Gq2ymRtFf2zIouHW2AQ=s900-c-k-c0x00ffffff-no-rj"

    # Download the image
    response = requests.get(image_url)
    image = Image.open(io.BytesIO(response.content))

    # Adjust the scale factor for blurring
    scale_factor = 0.5

    # Perform interpolation and get the interpolated image
    interpolated_image = interpolate_image(image, scale_factor)

    # Display the original and interpolated images
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image, cmap='gray')

    plt.subplot(1, 2, 2)
    plt.title('Interpolated Image (Cubic B-spline)')
    plt.imshow(interpolated_image, cmap='gray')

    plt.show()


if __name__ == '__main__':
    main()

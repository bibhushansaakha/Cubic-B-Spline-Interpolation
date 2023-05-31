import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.ndimage import zoom
import requests
import io

def interpolate_image(image, scale_factor):
    # Convert the image to grayscale
    image = image.convert('L')

    # Convert the image to a numpy array
    pixel_values = np.array(image)

    # Compute the new dimensions based on the scale factor
    new_width = int(pixel_values.shape[1] * scale_factor)
    new_height = int(pixel_values.shape[0] * scale_factor)

    # Resize the image using cubic interpolation
    interpolated_values = zoom(pixel_values, (new_height / pixel_values.shape[0], new_width / pixel_values.shape[1]), order=3)

    # Rescale the interpolated values to [0, 255]
    interpolated_values = np.clip(interpolated_values, 0, 255).astype(np.uint8)

    # Convert the interpolated values back to an image
    interpolated_image = Image.fromarray(interpolated_values)

    return interpolated_image


def main():
    image_url = "https://www.travelandleisure.com/thmb/gs7Gj12SUw2hy0F0MM9AMmYV0AU=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/corgi-dog-name-POPDOGS0819-1ebb8efb2c68499eab1c76411c9d1c15.jpg"

    # Download the image
    response = requests.get(image_url)
    image = Image.open(io.BytesIO(response.content))

    # Adjust the number of interpolation points (control points)
    num_points = 10

    # Perform interpolation and get the interpolated image
    interpolated_image = interpolate_image(image, num_points)

    # Display the original and interpolated images
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image)

    plt.subplot(1, 2, 2)
    plt.title('Interpolated Image')
    plt.imshow(interpolated_image)

    plt.show()


if __name__ == '__main__':
    main()

import numpy as np
from PIL import Image
from scipy.ndimage import zoom
import requests
import io
import matplotlib.pyplot as plt

def interpolate_image(image, scale_factor):
    # Separate color channels
    red, green, blue = image.split()

    # Convert color channels to numpy arrays
    red_values = np.array(red)
    green_values = np.array(green)
    blue_values = np.array(blue)

    # Compute the new dimensions based on the scale factor
    new_width = int(red_values.shape[1] * scale_factor)
    new_height = int(red_values.shape[0] * scale_factor)

    # Perform cubic B-spline interpolation on each color channel
    interpolated_red = zoom(red_values, (scale_factor, scale_factor), order=3)
    interpolated_green = zoom(green_values, (scale_factor, scale_factor), order=3)
    interpolated_blue = zoom(blue_values, (scale_factor, scale_factor), order=3)

    # Stack the interpolated color channels back together
    interpolated_values = np.dstack((interpolated_red, interpolated_green, interpolated_blue))

    # Apply increased Gaussian blur to the interpolated image
    blurred_values = interpolated_values.astype(np.float32)
    for _ in range(10):
        blurred_values = (blurred_values + np.roll(blurred_values, 1, axis=0) +
                          np.roll(blurred_values, -1, axis=0) + np.roll(blurred_values, 1, axis=1) +
                          np.roll(blurred_values, -1, axis=1)) / 5
    blurred_values = np.clip(blurred_values, 0, 255).astype(np.uint8)

    # Convert the blurred values back to an image
    blurred_image = Image.fromarray(blurred_values)

    return blurred_image


def main():
    image_url = "https://scontent.fbhr4-1.fna.fbcdn.net/v/t39.30808-6/308625301_5709536169092562_6534222441809001961_n.jpg?stp=cp6_dst-jpg&_nc_cat=104&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=QH1_J0WrANUAX8w-UkQ&_nc_ht=scontent.fbhr4-1.fna&oh=00_AfCmcGxRmegAKB_ot-Hmmu6jPpAI-XTQB8Sc_raLwrrF6A&oe=647968CF"

    # Download the image
    response = requests.get(image_url)
    image = Image.open(io.BytesIO(response.content))

    # Adjust the scale factor for interpolation
    scale_factor = 0.5

    # Perform interpolation and apply increased blur
    blurred_image = interpolate_image(image, scale_factor)

    # Display the original and blurred images
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image)

    plt.subplot(1, 2, 2)
    plt.title('Blurred Image (Cubic B-spline)')
    plt.imshow(blurred_image)

    plt.show()


if __name__ == '__main__':
    main()

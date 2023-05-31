import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def interpolate_image(image, scale_factor):
  """
  Interpolates an image by a given scale factor.

  Args:
    image: The image to interpolate.
    scale_factor: The scale factor to interpolate by.

  Returns:
    The interpolated image.
  """

  # Get the height and width of the image.
  height, width = image.shape[:2]

  # Create a 1D array of pixel values.
  pixel_values = image.reshape(-1, 3)  # Reshape to (-1, 3) for RGB images

  # Create a cubic spline interpolator.
  interpolator = CubicSpline(np.arange(len(pixel_values)), pixel_values.T)

  # Calculate the new dimensions.
  new_height = int(height * scale_factor)

  # Interpolate the pixel values.
  interpolated_pixel_values = interpolator(np.linspace(0, len(pixel_values) - 1, new_height))

  # Reshape the interpolated pixel values into an image.
  interpolated_image = interpolated_pixel_values.T.reshape(new_height, width, 3)  # Reshape to (new_height, width, 3)

  return interpolated_image

if __name__ == "__main__":
  # Load the image.
  image = plt.imread("team.jpeg")

  # Interpolate the image by a factor of 2.
  interpolated_image = interpolate_image(image, 2)

  # Plot the original and interpolated images.
  plt.subplot(121)
  plt.imshow(image)
  plt.title("Original image")

  plt.subplot(122)
  plt.imshow(interpolated_image)
  plt.title("Interpolated image")

  plt.show()

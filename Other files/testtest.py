import numpy as np
from PIL import Image, ImageFilter
import requests
import io
import matplotlib.pyplot as plt

def interpolate_image(image, scale_factor):
    width, height = image.size
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    resized_image = image.resize((new_width, new_height), resample=Image.BICUBIC)
    return resized_image

def main():
    image_url = "https://yt3.googleusercontent.com/tPXs09w0guC3IZQHw7uvgU6EINaViTtQhFyR_qYYSoxU9DuKFvYklC4Gq2ymRtFf2zIouHW2AQ=s900-c-k-c0x00ffffff-no-rj"
    response = requests.get(image_url)
    image = Image.open(io.BytesIO(response.content))
    scale_factor = 0.5
    interpolated_image = interpolate_image(image, scale_factor)
    blurred_image = interpolated_image.filter(ImageFilter.GaussianBlur(radius=2))
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image)
    plt.subplot(1, 2, 2)
    plt.title('Blurred Image (Cubic B-spline Interpolation + Gaussian Blur)')
    plt.imshow(blurred_image)
    plt.show()

if __name__ == '__main__':
    main()

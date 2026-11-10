
from PIL import Image
import numpy as np

# Open the image
image = Image.open("myphoto.jpg")

# Display image dimensions
print("Image size:", image.size)

# Convert the image into a NumPy array
image_array = np.array(image)

# Display array information
print("Array shape:", image_array.shape)

# Display some pixel values
print("\nFirst 5 pixels:")
print(image_array[0, :5])



# STEP 2: Apply a brightness filter

brightness = 50

bright_image_array = np.clip(image_array.astype(np.int16) + brightness, 0, 255)

bright_image = Image.fromarray(bright_image_array.astype(np.uint8))

bright_image.save("brightened_photo.jpg")

print("\nBrightness filter applied!")
print("Saved as brightened_photo.jpg")



# STEP 3: Apply a negative filter

negative_array = 255 - image_array

negative_image = Image.fromarray(negative_array.astype(np.uint8))

negative_image.save("negative_photo.jpg")

print("\nNegative filter applied!")
print("Saved as negative_photo.jpg")

# STEP 4: Apply a contrast filter

contrast_factor = 1.5

contrast_array = 128 + contrast_factor * (image_array.astype(np.float32) - 128)

contrast_array = np.clip(contrast_array, 0, 255)

contrast_image = Image.fromarray(contrast_array.astype(np.uint8))

contrast_image.save("contrast_photo.jpg")

print("\nContrast filter applied!")
print("Saved as contrast_photo.jpg")
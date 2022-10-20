from PIL import Image, ImageEnhance
import cv2
# Opens the image file
image = Image.open('less_brgt.png')

# shows image in image viewer
image.show()


# Enhance Brightness
curr_bri = ImageEnhance.Brightness(image)
new_bri = 2.5

# Brightness enhanced by a factor of 2.5
img_brightened = curr_bri.enhance(new_bri)

# shows updated image in image viewer
img_brightened.show()

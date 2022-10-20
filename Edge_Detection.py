import cv2
import matplotlib.pyplot as plt
# Open the image
img = cv2.imread('lenna.png')
# Apply Canny
edges = cv2.Canny(img, 100, 200, 3, L2gradient=True)
plt.figure()
plt.title('Output with edges')
plt.imsave('Edged_Lenna', edges, cmap='gray', format='png')
plt.imshow(edges, cmap='gray')
plt.show()
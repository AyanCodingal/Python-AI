import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian Blur
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Median Blur
median_blur = cv2.medianBlur(image, 5)

# Sobel Edge Detection
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Laplacian Edge Detection
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Canny Edge Detection
canny = cv2.Canny(image, 100, 200)

# Plot results
titles = ['Original', 'Gaussian Blur', 'Median Blur',
          'Sobel Combined', 'Laplacian', 'Canny']
images = [image, gaussian_blur, median_blur,
          sobel_combined, laplacian, canny]

plt.figure(figsize=(12, 8))
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()

import cv2
import numpy as np
from matplotlib import pyplot as plt

ref_image = cv2.imread('ref_220192J.jpg', cv2.IMREAD_GRAYSCALE)
test_image = cv2.imread('test6_220192J.jpg', cv2.IMREAD_GRAYSCALE)
# print(ref_image.shape)
# print(test_image.shape)

# print(ref_image.dtype)
# print(test_image.dtype)

# print(ref_image.min(), ref_image.max())
# print(test_image.min(), test_image.max())

# print(ref_image)
# print(test_image)
if(ref_image.shape == test_image.shape):
    ref_hist = np.zeros((256,), dtype=np.int32)
    test_hist = np.zeros((256,), dtype=np.int32)
    for i in range(ref_image.shape[0]):
        for j in range(ref_image.shape[1]):
            ref_hist[ref_image[i, j]] += 1
            test_hist[test_image[i, j]] += 1
else:
    print("Error: Images must have the same dimensions.")
    exit()   

ref_cdf = np.zeros((256,), dtype=np.int32)
test_cdf = np.zeros((256,), dtype=np.int32)
ref_cdf[0] = ref_hist[0]
test_cdf[0] = test_hist[0]
for i in range(1, 256):
    ref_cdf[i] = ref_cdf[i - 1] + ref_hist[i]
    test_cdf[i] = test_cdf[i - 1] + test_hist[i]

# print(ref_hist)
# print(test_hist)

plt.subplot(2, 2, 1)
plt.plot(ref_hist, color='r')
plt.title('Reference Image Histogram')
plt.subplot(2, 2, 2)
plt.plot(ref_cdf, color='g')
plt.title('Reference Image CDF')

plt.subplot(2, 2, 3)
plt.plot(test_hist, color='r')
plt.title('Test Image Histogram before editing')
plt.subplot(2, 2, 4)
plt.plot(test_cdf, color='g')
plt.title('Test Image CDF before editing')
plt.show()


import cv2
import numpy as np

lena_gray = cv2.imread('lena_gray.gif')
lena_color = cv2.imread('lena_color.gif')

lena_gray = lena_gray.astype("float64")
lena_color = lena_color.astype("float64")

print("lena gray size: ")
print(lena_gray.shape)

print("lena color size: ")
print(lena_color.shape)

if lena_gray.shape == lena_color.shape:
    dif = lena_gray - lena_color
    squared_dif = np.square(dif)
    sum_squared_dif = np.sum(squared_dif)
    MSE = sum_squared_dif / (lena_gray.shape[0] * lena_gray.shape[1])
    print(f"Mean Squared Error (MSE): {MSE}")
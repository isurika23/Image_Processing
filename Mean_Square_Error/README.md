# Mean Squared Error (MSE) Calculation

## Overview
This project demonstrates how to calculate the Mean Squared Error (MSE) between two images using Python and OpenCV. The implementation is provided in the `mse.py` script.

## Methodology
1. **Image Loading**: The script loads two images, `lena_gray.gif` (grayscale) and `lena_color.gif` (color), using OpenCV.

2. **Data Preparation**: Both images are converted to the `float64` data type to ensure accurate computation of differences.

3. **Shape Validation**: The script checks if the two images have the same dimensions. If not, MSE cannot be computed directly.

4. **MSE Calculation**:
	- The pixel-wise difference between the two images is computed.
	- The differences are squared and summed.
	- The sum is divided by the total number of pixels to obtain the Mean Squared Error.

5. **Output**: The MSE value is printed to the console. This value quantifies the average squared difference between the two images, providing a measure of similarity (lower MSE indicates higher similarity).

## Applications
MSE is widely used in image processing and computer vision to evaluate the quality of image transformations, compression, and restoration algorithms by comparing the processed image to a reference image.

# Image Processing Assignments Repository

## Overview
This repository contains assignments and experiments related to image processing, developed as part of academic coursework. The projects demonstrate fundamental techniques such as point operations and error metrics, using Python and popular libraries like OpenCV and Matplotlib.

## Folder Structure
- **Mean_Square_Error/**: Implements Mean Squared Error (MSE) calculation between two images to quantify similarity.
	- `mse.py`: Script to compute MSE between grayscale and color images.
	- `lena_gray.gif`, `lena_color.gif`: Sample images used for MSE calculation.
	- `README.md`: Documentation for the MSE calculation project.

- **Point_operations/**: Demonstrates point operations, especially histogram matching, to adjust the appearance of images.
	- `dev.py`: Script for histogram matching using the CDF of a reference image.
	- `submission.py`: Contains finalized code for assignment submission.
	- `ref_220192J.jpg`, `test5_220192J.jpg`: Reference and test images for processing.
	- `processed_image.jpg`: Output image after histogram matching.
	- `rhist_220192J.png`, `thist_220192J.png`: Histogram visualizations.
	- `README.md`: Documentation for point operations and histogram matching.
	- `Images_not_used/`: Additional images not used in the main workflow.

## Key Techniques Demonstrated
- **Mean Squared Error (MSE)**: Used to measure the average squared difference between two images, providing a quantitative assessment of similarity.
- **Histogram Matching**: Adjusts the histogram of a test image to match that of a reference image using cumulative distribution functions (CDFs), useful for normalization and visual consistency.


## Requirements
- Python 3.x
- OpenCV
- NumPy
- Matplotlib

## Setting Up a Virtual Environment
It is recommended to use a Python virtual environment to manage dependencies and avoid conflicts with system packages.

### Steps to Set Up (Windows)
1. **Open a terminal in the repository root directory.**
2. **Create a virtual environment:**
	```powershell
	python -m venv venv
	```
3. **Activate the virtual environment:**
	```powershell
	.\venv\Scripts\activate
	```
4. **Upgrade pip (optional but recommended):**
	```powershell
	python -m pip install --upgrade pip
	```
5. **Install required packages:**
	```powershell
	pip install opencv-python numpy matplotlib
	```
6. **Deactivate the environment when done:**
	```powershell
	deactivate
	```

You can now run the scripts in an isolated environment with all dependencies installed.


## How to Run the Code (Windows)

### 1. Run `mse.py` (Mean Squared Error Calculation)
1. Open a terminal and activate your virtual environment (see instructions above).
2. Navigate to the `Mean_Square_Error` folder:
	```powershell
	cd Mean_Square_Error
	```
3. Run the script:
	```powershell
	python mse.py
	```
4. The Mean Squared Error (MSE) value will be printed in the terminal.

### 2. Run `dev.py` (Histogram Matching)
1. Open a terminal and activate your virtual environment (see instructions above).
2. Navigate to the `Point_operations` folder:
	```powershell
	cd Point_operations
	```
3. Run the script:
	```powershell
	python dev.py
	```
4. The script will display plots comparing the histograms and images, and save the processed image as `processed_image.jpg` in the same folder.

## Applications
These assignments provide hands-on experience with core image processing concepts, useful for further study or practical applications in computer vision, medical imaging, and related fields.

import cv2
import numpy as np
from matplotlib import pyplot as plt

ref_image = cv2.imread('ref_220192J.jpg', cv2.IMREAD_GRAYSCALE)
test_image = cv2.imread('test5_220192J.jpg', cv2.IMREAD_GRAYSCALE)

def histogram_match(ref_cdf, test_cdf):
    
    # Build mapping (lookup table)
    mapping = np.zeros(256, dtype=np.uint8)
    ref_idx = 0
    for test_idx in range(256):
        while ref_idx < 255 and ref_cdf[ref_idx] < test_cdf[test_idx]:
            ref_idx += 1
        mapping[test_idx] = ref_idx
    return mapping

def histogram_pdf_cdf_calculator(image):
    hist, _ = np.histogram(image.flatten(), 256, [0,256])
    pdf = hist / hist.sum()
    cdf = np.cumsum(pdf)
    return pdf, cdf

def main():
    # Compute histograms
    _, test_cdf = histogram_pdf_cdf_calculator(test_image)
    ref_hist_norm, ref_cdf = histogram_pdf_cdf_calculator(ref_image)

    mapping = histogram_match(ref_cdf, test_cdf)
    processed_image = mapping[test_image]
    processed_hist_norm, processed_cdf = histogram_pdf_cdf_calculator(processed_image)
    cv2.imwrite('processed_image.jpg', processed_image)

    # Plot
    plt.figure(figsize=(12,5))

    plt.subplot(1,2,1)
    plt.fill_between(range(len(ref_hist_norm)), ref_hist_norm, label='Ref PDF')
    plt.title('Reference Image PDF')
    plt.legend()

    plt.subplot(1,2,2)
    plt.plot(ref_cdf, label='Ref CDF')
    plt.title('Reference Image CDF')
    plt.legend()

    plt.figure(figsize=(12,5))

    plt.subplot(1,2,1)
    plt.fill_between(range(len(processed_hist_norm)), processed_hist_norm, label='Processed PDF')
    plt.title('Processed Image PDF')
    plt.legend()

    plt.subplot(1,2,2)
    plt.plot(processed_cdf, label='Processed CDF')
    plt.title('Processed Image CDF')
    plt.legend()

    plt.show()

if __name__ == "__main__":
    main()
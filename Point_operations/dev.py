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
    test_hist_norm, test_cdf = histogram_pdf_cdf_calculator(test_image)
    ref_hist_norm, ref_cdf = histogram_pdf_cdf_calculator(ref_image)

    mapping = histogram_match(ref_cdf, test_cdf)
    processed_image = mapping[test_image]
    processed_hist_norm, processed_cdf = histogram_pdf_cdf_calculator(processed_image)
    cv2.imwrite('processed_image.jpg', processed_image)

    # Plot
    plt.figure(figsize=(12,7))

    plt.subplot(2,2,1)
    plt.fill_between(range(len(ref_hist_norm)), ref_hist_norm, alpha=0.7, label='Ref PDF')
    plt.fill_between(range(len(test_hist_norm)), test_hist_norm, alpha=0.7, label='Test PDF')
    plt.title('PDFs')
    plt.legend()

    plt.subplot(2,2,2)
    plt.plot(ref_cdf, label='Ref CDF')
    plt.plot(test_cdf, label='Test CDF')
    plt.title('Normalized CDFs')
    plt.legend()

    plt.subplot(2,2,3)
    plt.fill_between(range(len(ref_hist_norm)), ref_hist_norm, alpha=0.7, label='Ref PDF')
    plt.fill_between(range(len(processed_hist_norm)), processed_hist_norm, alpha=0.7, label='Processed PDF')
    plt.title('Processed PDF vs Ref PDF')
    plt.legend()

    plt.subplot(2,2,4)
    plt.plot(ref_cdf, label='Ref CDF')
    plt.plot(processed_cdf, label='Processed CDF')
    plt.title('Processed CDF vs Ref CDF')
    plt.legend()

    plt.figure(figsize=(15,5))   # wider since 3 images side by side

    plt.subplot(1,3,1)
    plt.imshow(ref_image, cmap='gray')
    plt.title("Reference Image")
    plt.axis("off")

    plt.subplot(1,3,2)
    plt.imshow(test_image, cmap='gray')
    plt.title("Test Image")
    plt.axis("off")

    plt.subplot(1,3,3)
    plt.imshow(processed_image, cmap='gray')
    plt.title("Processed Image")
    plt.axis("off")

    plt.show()

if __name__ == "__main__":
    main()
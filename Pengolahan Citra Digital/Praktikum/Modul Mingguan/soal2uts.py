import cv2
import numpy as np
from skimage.feature import local_binary_pattern
from matplotlib import pyplot as plt

# Fungsi untuk ekstraksi fitur bentuk
def extract_shape_features(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    hu_moments = cv2.HuMoments(cv2.moments(cnt)).flatten()
    return hu_moments

# Fungsi untuk ekstraksi fitur tekstur menggunakan Local Binary Pattern (LBP)
def extract_texture_features(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    lbp = local_binary_pattern(gray, P=8, R=1, method='uniform')
    n_bins = int(lbp.max() + 1)
    hist, _ = np.histogram(lbp, bins=n_bins, range=(0, n_bins), density=True)
    return hist

# Fungsi untuk ekstraksi fitur warna
def extract_color_features(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1, 2], None, [8, 8, 8], [0, 180, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    return hist

# Fungsi untuk segmentasi daun berdasarkan warna (asumsi daun cabai dan kaktus memiliki warna berbeda)
def segment_leaves(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Segmentasi daun cabai (misalnya hijau cerah)
    lower_cabai = np.array([35, 40, 40])
    upper_cabai = np.array([85, 255, 255])
    mask_cabai = cv2.inRange(hsv, lower_cabai, upper_cabai)
    segmented_cabai = cv2.bitwise_and(image, image, mask=mask_cabai)
    
    # Segmentasi daun kaktus (misalnya hijau tua atau warna lain yang sesuai)
    lower_kaktus = np.array([25, 40, 40])
    upper_kaktus = np.array([70, 255, 255])
    mask_kaktus = cv2.inRange(hsv, lower_kaktus, upper_kaktus)
    segmented_kaktus = cv2.bitwise_and(image, image, mask=mask_kaktus)
    
    return segmented_cabai, segmented_kaktus

# Path ke gambar yang berisi daun cabai dan kaktus (ganti dengan path yang sesuai)
image_path = 'cabekaktus.jpg'

# Baca gambar
image = cv2.imread(image_path)

# Segmentasi daun cabai dan kaktus
segmented_cabai, segmented_kaktus = segment_leaves(image)

# Fungsi untuk menampilkan fitur yang diekstraksi
def display_features(image):
    shape_features = extract_shape_features(image)
    texture_features = extract_texture_features(image)
    color_features = extract_color_features(image)
    
    print("Fitur Bentuk (Hu Moments):")
    print(shape_features)
    
    print("\nFitur Tekstur (LBP Histogram):")
    print(texture_features)
    
    print("\nFitur Warna (HSV Histogram):")
    print(color_features)
    
    # Tampilkan gambar asli
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Gambar Asli')
    plt.show()

# Ekstraksi dan tampilan fitur dari daun cabai
print("Fitur dari Daun Cabai:")
display_features(segmented_cabai)

# Ekstraksi dan tampilan fitur dari daun kaktus
print("Fitur dari Daun Kaktus:")
display_features(segmented_kaktus)


# Tampilkan hasil segmentasi
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(segmented_cabai, cv2.COLOR_BGR2RGB))
plt.title('Segmentasi Daun Cabai')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(segmented_kaktus, cv2.COLOR_BGR2RGB))
plt.title('Segmentasi Daun Kaktus')
plt.show()

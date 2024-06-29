import cv2
import numpy as np
import joblib
import os

# GARBAGE_TYPE = ["Kertas", "Kardus", "Biologis", "Plastik", "Botol/Gelas", "Pakaian", "Baterai", "Sampah"]
GARBAGE_TYPE = ["kertas", "kardus", "biologis", "plastik", "botol", "pakaian", "baterai", "limbah"]

# Feature Descriptor
def extract_features(image):
    win_size = (64, 128)
    block_size = (16, 16)
    block_stride = (8, 8)
    cell_size = (8, 8)
    nbins = 9
    hog = cv2.HOGDescriptor(win_size, block_size, block_stride, cell_size, nbins)

    # Compute HOG features
    features = hog.compute(image)
    return features.flatten()


# Load Classifier
svm = joblib.load("garbage_classifier.pkl")

# Image Source
image_source = os.listdir("test")

sama = 0
i = 0

for img in image_source:
    name = img
    img = cv2.imread(f"test/{img}")
    if img is None:
        print(f"Could not read image {img}")
        continue
    
    print("Mengecek Jenis Sampah...")

    # Resize image to HOG Window Size
    img_test = cv2.resize(img, (64, 128))

    # Extract HOG features
    hog_features = extract_features(img_test).reshape(1, -1).astype(np.float32)

    # Predict the class
    predicted_class = svm.predict(hog_features)[0]

    i += 1
    # Get garbage type
    garbage = GARBAGE_TYPE[predicted_class]
    garbage_type = ""
    if name.split("_")[0] == garbage:
        sama += 1
    if  garbage == "Biologis":
        garbage_type = "Organik"
    elif garbage in ["Kertas", "Kardus", "Plastik", "Botol/Gelas", "Pakaian", "Sampah"]:
        garbage_type = "Anorganik"
    else:
        garbage_type = "B3"

    print(f"Sampah {garbage}, Jenis {garbage_type}")

    img = cv2.resize(img, (500, 500))
    cv2.putText(img, f"Sampah: {garbage}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(img, f"Jenis: {garbage_type}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow(f"Hasil Deteksi {name}", img)

print(f"Gambar valid: {sama}")
print(f"Banyak Gambar: {i}")
print(f"Akurasi: {sama/i}")

cv2.waitKey(0)
cv2.destroyAllWindows()
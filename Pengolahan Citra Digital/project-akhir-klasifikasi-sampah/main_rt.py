import cv2
import numpy as np
import joblib
# # Load the trained SVM model
svm_model = joblib.load("garbage_classifier.pkl")

# Define garbage types (labels)
garbage_types = ["Kertas", "Kardus", "Organik", "Plastik", "Botol/Gelas", "Pakaian", "Baterai", "Sampah"]

def extract_hog_features(image):
    win_size = (64, 128)
    block_size = (16, 16)
    block_stride = (8, 8)
    cell_size = (8, 8)
    nbins = 9
    hog = cv2.HOGDescriptor(win_size, block_size, block_stride, cell_size, nbins)
    features = hog.compute(image)
    return features.flatten()

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert to grayscale and resize to the HOG descriptor window size
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height, width = gray_frame.shape
    crop_size = min(height, width)
    start_x = (width - crop_size) // 2
    start_y = (height - crop_size) // 2
    crop_frame = gray_frame[start_y:start_y+crop_size, start_x:start_x+crop_size]
    resized_frame = cv2.resize(crop_frame, (64, 128))

    # Extract HOG features
    hog_features = extract_hog_features(resized_frame).reshape(1, -1).astype(np.float32)

    # Predict the class
    predicted_class = svm_model.predict(hog_features)[0]
    garbage_type = garbage_types[predicted_class]

    # Display the label on the frame
    cv2.putText(frame, f"Jenis Sampah: {garbage_type}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.rectangle(frame, (start_x, start_y), (start_x+crop_size, start_y+crop_size), (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow("Garbage Classification", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
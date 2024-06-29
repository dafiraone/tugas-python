import cv2
import numpy as np
import joblib
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
import sys

# Tipe Sampah
GARBAGE_TYPE = ["Kertas", "Kardus", "Biologis", "Plastik", "Botol/Gelas", "Pakaian", "Baterai", "Limbah"]

# Feature Extraction dengan HOG
def extract_features(image):
    win_size = (64, 128) # ukuran fitur hog
    block_size = (16, 16) # ukuran blok
    block_stride = (8, 8) # langkah
    cell_size = (8, 8)
    nbins = 9
    hog = cv2.HOGDescriptor(win_size, block_size, block_stride, cell_size, nbins)

    # Compute HOG features
    return hog.compute(image)

# Load the pre-trained SVM classifier
svm = joblib.load("garbage_classifier.pkl")

# Define the main application class for the garbage classifier
class KlasifikasiSampah(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    # Initialize the user interface
    def initUI(self):
        self.setWindowTitle('Klasifikasi Sampah')
        self.layout = QVBoxLayout()

        # Label to prompt user to input an image
        self.label = QLabel('Masukkan Gambar Sampah', self)
        self.layout.addWidget(self.label)

        # Button to open file dialog for selecting an image
        self.button = QPushButton('Pilih di File', self)
        self.button.clicked.connect(self.openImage)
        self.layout.addWidget(self.button)

        # Label to display classification result
        self.resultLabel = QLabel('', self)
        self.layout.addWidget(self.resultLabel)

        # Set the layout for the application
        self.setLayout(self.layout)

    # Method to open file dialog and select an image
    def openImage(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.jpg *.jpeg *.png)", options=options)
        if fileName:
            self.classifyImage(fileName)
    
    # Method to classify the selected image
    def classifyImage(self, fileName):
        img = cv2.imread(fileName)
        if img is None:
            self.resultLabel.setText("Could not read image")
            return

        print("Mengecek Jenis Sampah...")

        # Resize image to match the HOG window size
        img_test = cv2.resize(img, (64, 128))

        # Extract HOG features from the image
        hog_features = extract_features(img_test).reshape(1, -1).astype(np.float32)

        # Predict the class of the garbage using the SVM classifier
        predicted_class = svm.predict(hog_features)[0]

        # Determine the type of garbage
        garbage = GARBAGE_TYPE[predicted_class]
        garbage_type = ""
        if  garbage == "Biologis":
            garbage_type = "Organik"
        elif garbage in ["Kertas", "Kardus", "Plastik", "Botol/Gelas", "Pakaian", "Limbah"]:
            garbage_type = "Anorganik"
        else:
            garbage_type = "B3"

        result_text = f"Sampah: {garbage}, Jenis: {garbage_type}"
        print(result_text)
        
        # Update the result label with the classification result
        self.resultLabel.setText(result_text)

        # Resize the image for display
        img = cv2.resize(img, (500, 500))
        # Overlay the classification result on the image
        cv2.putText(img, f"Sampah: {garbage}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(img, f"Jenis: {garbage_type}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Convert the image to a format suitable for display in PyQt5
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(qImg)
        
        # Display the image with the result in the label
        self.label.setPixmap(pixmap)

# Main entry point for the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = KlasifikasiSampah()
    ex.show()
    sys.exit(app.exec_())

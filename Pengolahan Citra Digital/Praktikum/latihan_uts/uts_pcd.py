import sys
import math
import cv2
import numpy as np
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import matplotlib.pyplot as plt

class ShowImage(QMainWindow):
    def __init__(self):
        super(ShowImage, self).__init__()
        loadUi('citra_app.ui', self)
        self.Image = None
        self.btn_load_citra.clicked.connect(self.loadClicked)
        # self.actionGrayscale.triggered.connect(self.grayscaling)
        self.actionGrayscale.triggered.connect(self.konvolusion)
        self.actionBrightness.triggered.connect(self.brightness)
        self.actionSimple_Contrast.triggered.connect(self.contrast)
        self.actionContrast_Stretching.triggered.connect(self.contrast_stretching)
        self.actionNegative.triggered.connect(self.negative)
        self.actionBiner.triggered.connect(self.biner)
        self.actionHistogram_Grayscale.triggered.connect(self.gray_histogram)
        self.actionHistogram_Grayscale.triggered.connect(self.gray_histogram)
        self.actionHistogram_RGB.triggered.connect(self.RGB_histogram)
        self.actionHistogram_Equalization.triggered.connect(self.eq_histogram)

    @pyqtSlot()
    def loadClicked(self):
        self.loadImage('teardown.jpg')

    def loadImage(self, image):
        self.Image = cv2.imread(image)
        self.displayImage()

    def addSelf(self, image):
        self.Image = image

    def displayImage(self, citra=None, windows=1):
        if citra is None:
            citra = self.Image
        
        qformat = QImage.Format_Indexed8
        if len(citra.shape) == 3:
            if (citra.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        
        img = QImage(citra, citra.shape[1], citra.shape[0], citra.strides[0],qformat)
        img = img.rgbSwapped()

        if windows==1:
            self.load_citra.setPixmap(QPixmap.fromImage(img))
            self.load_citra.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
            self.load_citra.setScaledContents(True)
        if windows==2:
            self.hasil_citra.setPixmap(QPixmap.fromImage(img))
            self.hasil_citra.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
            self.hasil_citra.setScaledContents(True)

    def grayscale(self):
        H, W = self.Image.shape[:2]
        grayscale = np.zeros((H, W), np.uint8)

        for i in range(H):
            for ii in range(W):
                grayscale[i, ii] = np.clip(0.299 * self.Image[i, ii, 0] +
                                           0.587 * self.Image[i, ii, 1] +
                                           0.114 * self.Image[i, ii, 2], 0, 255)
        return grayscale
    
    def grayscaling(self):
        grayimg = self.grayscale()
        self.displayImage(grayimg, 2)
    
    def brightness(self):
        grayimg = self.grayscale()
        H, W = grayimg.shape[:2]
        brightness = 80
        brightimg = np.zeros((H, W), np.uint8)

        for i in range(H):
            for ii in range(W):
                brightimg[i, ii] = np.clip(grayimg[i, ii] + brightness, 0, 255)
        
        self.displayImage(brightimg, 2)
        
    def contrast(self):
        grayimg = self.grayscale()
        H, W = grayimg.shape[:2]
        contrast = 1.6
        contrastimg = np.zeros((H, W), np.uint8)

        for i in range(H):
            for ii in range(W):
                contrastimg[i, ii] = np.clip(math.ceil(grayimg[i, ii] * contrast), 0, 255)
        
        self.displayImage(contrastimg, 2)

    def contrast_stretching(self):
        grayimg = self.grayscale()
        H, W = grayimg.shape[:2]
        min_v = np.min(grayimg)
        max_v = np.max(grayimg)
        stretchimg = np.zeros((H, W), np.uint8)

        for i in range(H):
            for ii in range(W):
                stretchimg[i, ii] = (grayimg[i, ii] - min_v) / (max_v - min_v) * 255
        
        self.displayImage(stretchimg, 2)

    def negative(self):
        grayimg = self.grayscale()
        H, W = grayimg.shape[:2]
        negativeimg = np.zeros((H, W), np.uint8)

        for i in range(H):
            for ii in range(W):
                negativeimg[i, ii] = np.clip(255 - grayimg[i, ii], 0, 255)

        self.displayImage(negativeimg, 2)

    def biner(self):
        grayimg = self.grayscale()
        H, W = grayimg.shape[:2]
        binerimg = np.zeros((H, W), np.uint8)
        threshold = 80

        for i in range(H):
            for ii in range(W):
                binerimg[i, ii] = 0 if grayimg[i, ii] == threshold else 1 if grayimg[i, ii] < threshold else 255

        self.displayImage(binerimg, 2)

    def gray_histogram(self):
        grayimg = self.grayscale()
        H, W = grayimg.shape[:2]
        
        self.displayImage(grayimg, 2)
        plt.title("Histogram Grayscale")
        plt.hist(grayimg.ravel(), 255, (0, 255))
        plt.show()

    def RGB_histogram(self):
        color = ('r', 'g', 'b')

        for i, col in enumerate(color):
            histo = cv2.calcHist([self.Image], [i], None, [256], [0, 256])
            plt.plot(histo, color=col)
            plt.xlim((0, 256))

        self.displayImage(windows=2)
        plt.title("Histogram RGB")
        plt.hist(self.Image.ravel(), 255, (0, 255))
        plt.show()
    
    def eq_histogram(self):
        # hist, bins = np.histogram(self.Image.flatten(), 256, [0, 256])
        # cdf = hist.cumsum()
        # cdf_normalized = cdf * float(hist.max()) / cdf.max()

        # cdf_m = np.ma.masked_equal(cdf, 0)
        # cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
        # cdf = np.ma.filled(cdf_m, 0).astype('uint8')
        
        # self.Image = cdf[self.Image]
        # self.displayImage(windows=2)

        # plt.plot(cdf_normalized, color='b')
        # plt.hist(self.Image.flatten(), 256, [0, 256], color='r')
        # plt.xlim([0, 256])
        # plt.legend(('cdf', 'histogram'), loc='upper left')
        # plt.show()

        self.Image = self.grayscale()
        equ = cv2.equalizeHist(self.Image)
        res = np.hstack((self.Image, equ))
        cv2.imshow('Histogram Equalization', equ)
    
    def konvolusi(self, citra, kernel):
        H_citra, W_citra = citra.shape[:2]
        H_kernel, W_kernel = kernel.shape[:2]
        out = np.zeros(citra.shape)
        print(out)
        print(type(out))

        H = H_kernel // 2
        W = W_kernel // 2

        for i in range(H, H_citra-H):
            for ii in range(W, W_citra-W):
                sum = 0
                for iii in range(H_kernel):
                    for iv in range(W_kernel):
                        # a = citra[i+iii, ii+1]
                        # b = kernel[H+iii, W+1]
                        sum += kernel[iii][iv]*citra[i-H+iii][ii-W+iv]
                out[i, ii] = sum
        
        self.displayImage(out, 2)
        
        # convolimg = cv2.filter2D(self.Image, -1, kernel)
        # self.displayImage(convolimg, 2)

    def konvolusion(self):
        kernel = (1.0 / 345) * np.array([[1, 5, 7, 5, 1],
                                         [5, 20, 33, 20, 5],
                                         [7, 33, 55, 33, 7],
                                         [5, 20, 33, 20, 5],
                                         [1, 5, 7, 5, 1]])
        self.konvolusi(self.Image, kernel)

app = QtWidgets.QApplication(sys.argv)
window = ShowImage()
window.setWindowTitle("UTS Praktikum PCD - 152022003")
window.show()
sys.exit(app.exec_())
import sys
import cv2
import numpy as np
import dlib
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import matplotlib.pyplot as plt

class ShowImage(QMainWindow):
    def __init__(self):
        super(ShowImage,self).__init__()
        loadUi('load_citra.ui',self)
        self.image=None
        self.btn_loadcitra.clicked.connect(self.loadClicked)
        self.btn_prosescitra.clicked.connect(self.grayscale)
        self.actionOperasi_Pencerahan.triggered.connect(self.brightness)
        self.actionSimple_Contrast.triggered.connect(self.contrast)
        self.actionContrast_Stretching.triggered.connect(self.contrast_stretching)
        self.actionNegative.triggered.connect(self.negative)
        self.actionBiner.triggered.connect(self.biner)
        self.actionHistogram_Grayscale.triggered.connect(self.gray_histogram)
        self.actionHistogram_RGB.triggered.connect(self.RGB_histogram)
        self.actionHistogram_Equalization.triggered.connect(self.equalization_histogram)
        self.actionTranslasi.triggered.connect(self.translasi)
        self.action45_Derajat.triggered.connect(self.rotasi_45)
        self.action90_Derajat.triggered.connect(self.rotasi_90)
        self.action180_Derajat.triggered.connect(self.rotasi_180)
        self.actionZoom_In.triggered.connect(self.zoom_in)
        self.actionCrop.triggered.connect(self.crop)
        self.actionTambah_Kurang.triggered.connect(self.tambah_kurang)
        self.actionBoolean.triggered.connect(self.op_boolean)
        self.actionKonvolusi_2D_2.triggered.connect(self.konvolusi_2d)
        self.actionMean_Filter.triggered.connect(self.mean_filter)
        self.actionGaussian_Filter.triggered.connect(self.gaussian_filter)
        self.actionKernel_1.triggered.connect(self.kernel1)
        self.actionKernel_2.triggered.connect(self.kernel2)
        self.actionKernel_3.triggered.connect(self.kernel3)
        self.actionKernel_4.triggered.connect(self.kernel4)
        self.actionKernel_5.triggered.connect(self.kernel5)
        self.actionKernel_6.triggered.connect(self.kernel6)
        self.actionLaplace.triggered.connect(self.laplace)
        self.actionMedian_Filter.triggered.connect(self.median_filter)
        self.actionMax_Filter.triggered.connect(self.max_filter)
        self.actionMin_Filter.triggered.connect(self.min_filter)
        self.actionDFT_LPF.triggered.connect(self.DFT_LPF)
        self.actionDFT_HPF.triggered.connect(self.DFT_HPF)
        self.actionSobel.triggered.connect(self.sobel)
        self.actionCanny_Edge.triggered.connect(self.canny_edge)
        self.actionDilasi.triggered.connect(self.dilasi)
        self.actionErosi.triggered.connect(self.erosi)
        self.actionOpening.triggered.connect(self.opening)
        self.actionClosing.triggered.connect(self.closing)
        self.actionClosing.triggered.connect(self.closing)
        self.actionBinary.triggered.connect(self.binary)
        self.actionBinary_Invers.triggered.connect(self.binary_invers)
        self.actionTrunc.triggered.connect(self.trunc)
        self.actionTo_Zero.triggered.connect(self.to_zero)
        self.actionTo_Zero_Invers.triggered.connect(self.to_zero_invers)
        self.actionMean_Threshold.triggered.connect(self.mean_threshold)
        self.actionGauss_Threshold.triggered.connect(self.gauss_threshold)
        self.actionOtsu_Threshold.triggered.connect(self.otsu_threshold)
        self.actionIdentifikasi_Bentuk.triggered.connect(self.contour)
        self.actionColor_Tracking.triggered.connect(self.color_tracking)
        self.actionColor_Picker.triggered.connect(self.color_picker)
        self.actionObject_Detection.triggered.connect(self.object_detection)
        self.actionAstronaut.triggered.connect(self.histogram_of_gradient_astro)
        self.actionPedestrian.triggered.connect(self.histogram_of_gradient_pedes)
        self.actionHaar_Face_Eye.triggered.connect(self.haar_face_eye)
        self.actionHaar_Pedestrian.triggered.connect(self.haar_pedestrian)
        self.actionCircle_Hough.triggered.connect(self.hough_circle)
        self.actionFacial_Landmark.triggered.connect(self.facial_landmark)
        self.actionFace_Swap.triggered.connect(self.face_swap)
        self.actionReal_Time_Face_Swap.triggered.connect(self.rt_face_swap)
        self.actionYawn_Detection.triggered.connect(self.yawn_detection)
    
    @pyqtSlot()
    def loadClicked(self):
        # self.loadImage('histogram.jpg')
        # self.loadImage('teardown-noise.jpg')
        self.loadImage('teardown.jpg')
        # self.loadImage('ipsc.jpg')
    
    def loadImage(self,flname):
        self.image=cv2.imread(flname)
        self.displayImage()

    def grayscale(self):
        H, W = self.image.shape[:2]
        gray = np.zeros((H, W), np.uint8)
        for i in range(H):
            for j in range(W):
                gray[i, j] = np.clip(0.299 * self.image[i, j, 0] +
                                     0.587 * self.image[i, j, 1] +
                                     0.114 * self.image[i, j, 2], 0, 255)
        self.image = gray
        self.displayImage(2)

    def brightness(self):
        # error handling grayscaling citra
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        H, W = self.image.shape[:2]
        brightness = 80
        for i in range(H):
            for j in range(W):
                a = self.image.item(i, j)
                b = np.clip(a + brightness, 0, 255)

                self.image[i, j] = b


        self.displayImage(2)

    def contrast(self):
        # error handling grayscaling citra
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        H, W = self.image.shape[:2]
        contrast = 1.7
        for i in range(H):
            for j in range(W):
                a = self.image.item(i, j)
                b = np.clip(a * contrast, 0, 255)

                self.image[i, j] = b

        self.displayImage(2)

    def contrast_stretching(self):
        # error handling grayscaling citra
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        H, W = self.image.shape[:2]
        min_v = np.min(self.image)
        max_v = np.max(self.image)
        
        for i in range(H):
            for j in range(W):
                a = self.image.item(i, j)
                b = float(a - min_v) / (max_v - min_v) * 255

                self.image[i, j] = b

        self.displayImage(2)

    def negative(self):
        # error handling grayscaling citra
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        H, W = self.image.shape[:2]
        maximum_intensity = 255
        
        for i in range(H):
            for j in range(W):
                a = self.image.item(i, j)
                b = np.clip(maximum_intensity - a, 0, 255)

                self.image[i, j] = b

        self.displayImage(2)

    def biner(self):
        # error handling grayscaling citra
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        H, W = self.image.shape[:2]

        def biner_validation(nilai):
            if nilai == 180:
                return 0
            elif nilai < 180:
                return 1
            elif nilai > 180:
                return 255
        
        for i in range(H):
            for j in range(W):
                a = self.image.item(i, j)
                b = np.clip(biner_validation(a), 0, 255)
                # b = np.clip(biner_validation(a), 0, 180)

                self.image[i, j] = b

        self.displayImage(2)
    
    def gray_histogram(self):
        H, W = self.image.shape[:2]
        gray = np.zeros((H, W), np.uint8)
        for i in range(H):
            for j in range(W):
                gray[i, j] = np.clip(0.299 * self.image[i, j, 0] +
                                     0.587 * self.image[i, j, 1] +
                                     0.114 * self.image[i, j, 2], 0, 255)
        self.image = gray
        print(self.image)
        self.displayImage(2)
        plt.hist(self.image.ravel(), 255, (0, 255))
        plt.show()

    def RGB_histogram(self):
        color = ('r', 'g', 'b')

        for i, col in enumerate(color):
            histo = cv2.calcHist([self.image], [i], None, [256], [0, 256])
            plt.plot(histo, color=col)
            plt.xlim((0, 256))
        
        self.displayImage(2)
        plt.show()

    def equalization_histogram(self):
        hist, bins = np.histogram(self.image.flatten(), 256, [0, 256])
        cdf = hist.cumsum()
        cdf_normalized = cdf * hist.max() / cdf.max()
        cdf_m = np.ma.masked_equal(cdf, 0)
        cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
        cdf = np.ma.filled(cdf_m, 0).astype('uint8')
        self.image = cdf[self.image]
        self.displayImage(2)

        plt.plot(cdf_normalized, color='b')
        plt.hist(self.image.flatten(), 256, [0, 256], color='r')
        plt.xlim([0, 256])
        plt.legend(('cdf', 'histogram'), loc='upper left')
        plt.show()

    def translasi(self):
        h,w=self.image.shape[:2]
        quarter_h,quarter_w=h/4,w/4
        T=np.float32([[1,0,quarter_w],[0,1,quarter_h]])
        img=cv2.warpAffine(self.image,T,(w,h))
        self.image = img
        self.displayImage(2)

    def rotasi(self, degree):
        h, w = self.image.shape[:2]
        rotationMatrix = cv2.getRotationMatrix2D((w / 2, h / 2), 
        degree, .7)
        cos = np.abs(rotationMatrix[0, 0])
        sin = np.abs(rotationMatrix[0, 1])
        nW = int((h * sin) + (w * cos))
        nH = int((h * cos) + (w * sin))
        rotationMatrix[0, 2] += (nW / 2) - w / 2
        rotationMatrix[1, 2] += (nH / 2) - h / 2
        rot_image = cv2.warpAffine(self.image, rotationMatrix, (h, w))
        self.image=rot_image
        self.displayImage(2)
    
    def rotasi_45(self):
        self.rotasi(45)
        
    def rotasi_90(self):
        self.rotasi(90)

    def rotasi_180(self):
        self.rotasi(180)

    def zoom_in(self):
        skala = 2
        resize_img=cv2.resize(self.image,None,fx=skala,fy=skala,interpolation=cv2.INTER_CUBIC)
        # resize_img=cv2.resize(self.image,None,fx=0.50, fy=0.50)
        # resize_img=cv2.resize(self.image,(900,400),interpolation=cv2.INTER_AREA)
        cv2.imshow('Original', self.image)
        cv2.imshow('Zoom In', resize_img)
        cv2.waitKey()

    def crop(self):
        start_row = 10
        start_col = 100
        end_row = 50
        end_col = 500
        crop_img = self.image[start_row:start_col, end_row:end_col]
        cv2.imshow('Original', self.image)
        cv2.imshow('Cropped', crop_img)
        cv2.waitKey()

    def tambah_kurang(self):
        img1 = cv2.imread('teardown.jpg', 0)
        img2 = cv2.imread('rdr.jpg', 0)
        add = img1 + img2
        subtract = img1 - img2
        cv2.imshow('Image 1 original', img1)
        cv2.imshow('Image 2 original', img2)
        cv2.imshow('Image tambah', add)
        cv2.imshow('Image kurang', subtract)
        cv2.waitKey()

    def op_boolean(self):
        img1 = cv2.imread('teardown.jpg', 0)
        img2 = cv2.imread('rdr.jpg', 0)
        img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        operasi=cv2.bitwise_and(img1,img2)
        cv2.imshow('Image 1 original', img1)
        cv2.imshow('Image 2 original', img2)
        cv2.imshow('Image Boolean', operasi)
        cv2.waitKey()

    def konvolusi(self, kernel):
        self.image = cv2.filter2D(self.image, -1, kernel)
        self.displayImage(2)

    def konvolusi_2d(self):
        kernel = np.array([
            # [1,1,1],
            # [1,1,1],
            # [1,1,1],
            [6,0,-6],
            [6,1,-6],
            [6,0,-6],
        ])

        self.konvolusi(kernel)

    def mean_filter(self):
        # kernel = (1/9)*np.array([
        #     [1,1,1],
        #     [1,1,1],
        #     [1,1,1],
        # ])
        kernel = (1/4)*np.array([
            [1,1],
            [1,1],
        ])

        self.konvolusi(kernel)

    def gaussian_filter(self):
        kernel = (1.0 / 345) * np.array([[1, 5, 7, 5, 1],
                                         [5, 20, 33, 20, 5],
                                         [7, 33, 55, 33, 7],
                                         [5, 20, 33, 20, 5],
                                         [1, 5, 7, 5, 1]])
                                         
        self.konvolusi(kernel)

    def kernel1(self):
        kernel = np.array([
            [-1, -1, -1],
            [-1, 8, -1],
            [-1, -1, -1]
        ])
        self.konvolusi(kernel)

    def kernel2(self):
        kernel = np.array([
            [-1, -1, -1],
            [-1, 9, -1],
            [-1, -1, -1]
        ])
        self.konvolusi(kernel)

    def kernel3(self):
        kernel = np.array([
            [0, -1 , 0],
            [-1, 5, -1],
            [0, -1,  0]
        ])
        self.konvolusi(kernel)

    def kernel4(self):
        kernel = np.array([
            [1, -2, 1],
            [-2, 5, -2],
            [1, -2, 1]
        ])
        self.konvolusi(kernel)

    def kernel5(self):
        kernel = np.array([
            [1, -2, 1],
            [-2, 4, -2],
            [1, -2, 1]
        ])
        self.konvolusi(kernel)

    def kernel6(self):
        kernel = np.array([
            [0, 1, 0],
            [1, -4, 1],
            [0, 1, 0]
        ])
        self.konvolusi(kernel)

    def laplace(self):
        kernel = (1.0 / 16) * np.array([[0, 0, -1, 0, 0],
                                        [0, -1, -2, -1, 0],
                                        [-1, -2, 16, -2, -1],
                                        [0, -1, -2, -1, 0],
                                        [0, 0, -1, 0, 0]])

        self.konvolusi(kernel)

    def median_filter(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass
        

        img_out = self.image.copy()
        H, W = self.image.shape

        for i in np.arange(3, H - 3):
            for j in np.arange(3, W - 3):
                neighbors = []
                for k in np.arange(-3, 4):
                    for l in np.arange(-3, 4):
                        a = self.image.item(i + k, j + l)
                        neighbors.append(a)
                neighbors.sort()
                median = neighbors[30]
                b = median
                img_out[i, j] = b
        self.image = img_out
        self.displayImage(2)

    def max_filter(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        img_out = self.image.copy()
        H, W = self.image.shape

        for i in range(3, H - 3):
            for j in range(3, W - 3):
                neighbors = []
                for k in range(-3, 4):
                    for l in range(-3, 4):
                        a = self.image[i + k, j + l]
                        neighbors.append(a)

                max_val = max(neighbors)
                img_out[i, j] = max_val
        self.image = img_out
        self.displayImage(2)

    def min_filter(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        img_out = self.image.copy()
        H, W = self.image.shape

        for i in range(3, H - 3):
            for j in range(3, W - 3):
                neighbors = []
                for k in range(-3, 4):
                    for l in range(-3, 4):
                        a = self.image[i + k, j + l]
                        neighbors.append(a)

                max_val = min(neighbors)
                img_out[i, j] = max_val
        self.image = img_out
        self.displayImage(2)
    
    def DFT_LPF(self):
        x=np.arange(256)
        y=np.sin(2*np.pi*x/3)
        
        y+=max(y)
        img=np.array([[y[j]*127 for j in range (256)] for i in range (256)], dtype=np.uint8)
        
        plt.imshow(img)
        img=cv2.imread('teardown-noise.jpg', 0)
        
        dft=cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
        dft_shift=np.fft.fftshift(dft)
        
        magnitude_spectrum = 20 * np.log ((cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1])))
        
        rows, cols = img.shape
        crow, ccol = int(rows/2), int(cols/2)
        mask = np.zeros((rows, cols, 2), np.uint8)
        r=50
        center = [crow, ccol]
        x, y =np.ogrid[:rows, :cols]
        mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r 
        mask [mask_area] = 1
        
        fshift = dft_shift * mask
        fshift_mask_mag = 20 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))
        f_ishift = np.fft.ifftshift(fshift)
        
        img_back = cv2.idft (f_ishift)
        img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
        
        fig = plt.figure(figsize=(12,12))
        ax1=fig.add_subplot(2,2,1)
        ax1.imshow(img, cmap='gray')
        ax1.title.set_text('input image')

        ax2=fig.add_subplot(2,2,2)
        ax2.imshow(magnitude_spectrum, cmap='gray')
        ax2.title.set_text('FFT of image')

        ax3=fig.add_subplot(2,2,3)
        ax3.imshow(fshift_mask_mag, cmap='gray')
        ax3.title.set_text('FFT + mask')
        
        ax4=fig.add_subplot(2,2,4)
        ax4.imshow(img_back, cmap='gray')
        ax4.title.set_text('inverse fourier')
        self.image = img_back
        self.displayImage(2)
        plt.show()
        
    def DFT_HPF(self):
        x=np.arange(256)
        y=np.sin(2*np.pi*x/3)
        
        y+=max(y)
        img=np.array([[y[j]*127 for j in range (256)] for i in range (256)], dtype=np.uint8)
        
        plt.imshow(img)
        img=cv2.imread('teardown.jpg', 0)
        
        dft=cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
        dft_shift=np.fft.fftshift(dft)
        
        magnitude_spectrum = 20 * np.log ((cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1])))
        
        rows, cols = img.shape
        crow, ccol = int(rows/2), int(cols/2)
        mask = np.ones((rows, cols, 2), np.uint8)
        r=80
        center = [crow, ccol]
        x, y =np.ogrid[:rows, :cols]
        mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r 
        mask [mask_area] = 0
        
        fshift = dft_shift * mask
        fshift_mask_mag = 20 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))
        f_ishift = np.fft.ifftshift(fshift)
        
        img_back = cv2.idft (f_ishift)
        img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
        
        fig = plt.figure(figsize=(12,12))
        ax1=fig.add_subplot(2,2,1)
        ax1.imshow(img, cmap='gray')
        ax1.title.set_text('input image')

        ax2=fig.add_subplot(2,2,2)
        ax2.imshow(magnitude_spectrum, cmap='gray')
        ax2.title.set_text('FFT of image')

        ax3=fig.add_subplot(2,2,3)
        ax3.imshow(fshift_mask_mag, cmap='gray')
        ax3.title.set_text('FFT + mask')
        
        ax4=fig.add_subplot(2,2,4)
        ax4.imshow(img_back, cmap='gray')
        ax4.title.set_text('inverse fourier')
        self.image = img_back
        self.displayImage(2)
        plt.show()
    
    def sobel(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        kernel_x = np.array([
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]
        ])

        kernel_y = np.array([
            [-1, -2, 1],
            [0, 0, 0],
            [1, 2, 1]
        ])

        Gx = cv2.filter2D(self.image, -1, kernel_x)
        Gy = cv2.filter2D(self.image, -1, kernel_y)
        # Gx = cv2.Sobel(self.image, cv2.CV_64F, 1, 0, kernel_x)
        # Gy = cv2.Sobel(self.image, cv2.CV_64F, 0, 1, kernel_y)

        gradien = np.sqrt(np.square(Gx) + np.square(Gy))
        normalisasi_gradien = (gradien / np.max(gradien)) * 255
        
        self.image = normalisasi_gradien
        self.displayImage(2)

        plt.imshow(normalisasi_gradien, cmap='gray', interpolation='bicubic')
        plt.axis('off')
        plt.show()

    def canny_edge(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        gauss = (1.0/57) * np.array(
            [[0, 1, 2, 1, 0],
            [1, 3, 5, 3, 1],
            [2, 5, 9, 5, 2],
            [1, 3, 5, 3, 1],
            [0, 1, 2, 1, 0]])
        
        konvol = cv2.filter2D(self.image, -1, gauss)

        kernel_x = np.array([
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]
        ])

        kernel_y = np.array([
            [-1, -2, 1],
            [0, 0, 0],
            [1, 2, 1]
        ])

        # konvolusi_x = cv2.Sobel(konvol, cv2.CV_64F, 1, 0, kernel_x)
        # konvolusi_y = cv2.Sobel(konvol, cv2.CV_64F, 0, 1, kernel_y)
        konvolusi_x = cv2.Sobel(konvol, cv2.CV_64F, 1, 0, ksize=3)
        konvolusi_y = cv2.Sobel(konvol, cv2.CV_64F, 0, 1, ksize=3)
        # konvolusi_x = cv2.filter2D(konvol, cv2.CV_64F, kernel_x)
        # konvolusi_y = cv2.filter2D(konvol, cv2.CV_64F, kernel_y)


        theta = np.arctan2(konvolusi_x, konvolusi_y)
        angle = theta * 180. / np.pi
        angle[angle < 0] += 180

        H, W = self.image.shape[:2]
        Z = np.zeros((H, W), dtype=np.uint8)
        img_out = np.copy(konvol)


        for i in range(1, H - 1):
            for j in range(1, W - 1):
                try:
                    q = 255
                    r = 255
                    # angle 0
                    if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i,j] <= 180):
                        q = img_out[i, j + 1]
                        r = img_out[i, j - 1]
                    # angle 45
                    elif (22.5 <= angle[i, j] < 67.5):
                        q = img_out[i + 1, j - 1]
                        r = img_out[i - 1, j + 1]
                    # angle 90
                    elif (67.5 <= angle[i, j] < 112.5):
                        q = img_out[i + 1, j]
                        r = img_out[i - 1, j]
                    # angle 135
                    elif (112.5 <= angle[i, j] < 157.5):
                        q = img_out[i - 1, j - 1]
                        r = img_out[i + 1, j + 1]
                        if (img_out[i, j] >= q) and (img_out[i, j] >= r):
                            Z[i, j] = img_out[i, j]
                        else:
                            Z[i, j] = 0
                except IndexError as e:
                    pass
        img_N = Z.astype("uint8")
        img_N_old = np.copy(img_N)

        weak = 50
        strong = 100

        for i in range(H):
            for j in range(W):
                a = img_N[i, j]
                if a > weak:
                    b = weak
                    if a > strong:
                        b = 255
                else:
                    b = 0
                img_N[i, j] = b

        # Eliminasi tepi lemah yang tidak terhubung dengan tepi kuat
        for i in range(1, H-1):
            for j in range(1, W-1):
                if img_N[i, j] == weak:
                    try:
                        if (img_N[i+1, j-1] == strong) or (img_N[i+1, j] == strong) or \
                        (img_N[i+1, j+1] == strong) or (img_N[i, j-1] == strong) or \
                        (img_N[i, j+1] == strong) or (img_N[i-1, j-1] == strong) or \
                        (img_N[i-1, j] == strong) or (img_N[i-1, j+1] == strong):
                            img_N[i, j] = strong
                        else:
                            img_N[i, j] = 0
                    except IndexError as e:
                        pass
        self.image = img_N
        
        # blurred = cv2.GaussianBlur(self.image, (5, 5), 0)
        # self.image = cv2.Canny(blurred, 50, 150)

        fig = plt.figure(figsize=(12,12))
        ax1=fig.add_subplot(2,2,1)
        ax1.imshow(konvol, cmap='gray')
        ax1.title.set_text('Reduksi noise')

        ax2=fig.add_subplot(2,2,2)
        ax2.imshow(theta, cmap='gray')
        ax2.title.set_text('Finding Gradien')

        ax3=fig.add_subplot(2,2,3)
        ax3.imshow(img_N_old, cmap='gray')
        ax3.title.set_text('Non maximum surpression')
        
        ax4=fig.add_subplot(2,2,4)
        ax4.imshow(self.image, cmap='gray')
        ax4.title.set_text('Hysterisis Tresholding')
        plt.show()

        self.displayImage(2)

    def dilasi(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        _, binary_img = cv2.threshold(self.image, 127, 255, 0)

        strel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

        dilated_img = cv2.dilate(binary_img, strel)
        cv2.imshow('Dilasi', dilated_img)
        cv2.waitKey()

    def erosi(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        _, binary_img = cv2.threshold(self.image, 127, 255, 0)

        strel1 = cv2.getStructuringElement(cv2.MORPH_ERODE, (1, 1))
        strel3 = cv2.getStructuringElement(cv2.MORPH_ERODE, (3, 3))
        strel5 = cv2.getStructuringElement(cv2.MORPH_ERODE, (5, 5))
        strel35 = cv2.getStructuringElement(cv2.MORPH_ERODE, (3, 5))
        strel510 = cv2.getStructuringElement(cv2.MORPH_ERODE, (5, 10))

        eroded_img1 = cv2.erode(binary_img, strel1)
        eroded_img3 = cv2.erode(binary_img, strel3)
        eroded_img5 = cv2.erode(binary_img, strel5)
        eroded_img35 = cv2.erode(binary_img, strel35)
        eroded_img510 = cv2.erode(binary_img, strel510)

        cv2.imshow('Gambar Biner', binary_img)
        cv2.imshow('Erosi 1', eroded_img1)
        cv2.imshow('Erosi 3', eroded_img3)
        cv2.imshow('Erosi 5', eroded_img5)
        cv2.imshow('Erosi 35', eroded_img35)
        cv2.imshow('Erosi 510', eroded_img510)
        cv2.waitKey()

    def opening(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        _, binary_img = cv2.threshold(self.image, 127, 255, 0)

        strel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

        opening_img = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, strel)

        cv2.imshow('Opening', opening_img)
        cv2.waitKey()

    def closing(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        _, binary_img = cv2.threshold(self.image, 127, 255, 0)

        strel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
        
        closing_img = cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, strel)

        cv2.imshow('Closing', closing_img)
        cv2.waitKey()

    def binary(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        T = 127
        MAX = 255

        ret, thresh = cv2.threshold(self.image, T, MAX, cv2.THRESH_BINARY)
        cv2.imshow('Binary', thresh)

    def binary_invers(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        T = 127
        MAX = 255

        ret, thresh = cv2.threshold(self.image, T, MAX, cv2.THRESH_BINARY_INV)
        cv2.imshow('Binary Invers', thresh)

    def trunc(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        T = 127
        MAX = 255

        ret, thresh = cv2.threshold(self.image, T, MAX, cv2.THRESH_TRUNC)
        cv2.imshow('Trunc', thresh)

    def to_zero(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        T = 127
        MAX = 255

        ret, thresh = cv2.threshold(self.image, T, MAX, cv2.THRESH_TOZERO)
        cv2.imshow('To Zero', thresh)

    def to_zero_invers(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        T = 127
        MAX = 255

        ret, thresh = cv2.threshold(self.image, T, MAX, cv2.THRESH_TOZERO_INV)
        cv2.imshow('To Zero Invers', thresh)

    def mean_threshold(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        imgh = cv2.adaptiveThreshold(self.image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 2)
        cv2.imshow('Mean Thresholding', imgh)

    def gauss_threshold(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        imgh = cv2.adaptiveThreshold(self.image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 2)
        cv2.imshow('Gaussian Thresholding', imgh)

    def otsu_threshold(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        T = 130

        ret, imgh = cv2.threshold(self.image, T, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        cv2.imshow('Otsu Thresholding', imgh)

    def contour(self):
        self.loadImage('shapes.png')
        # self.loadImage('shapes2.jpg')
        # self.loadImage('shapes3.jpg')
        # self.loadImage('histogram.jpg')
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except:
            pass

        T = 127

        # 3. Threshold citra dengan nilai T=127
        _, thresh_img = cv2.threshold(self.image, T, 255, cv2.THRESH_BINARY)

        # 4. Ekstrak kontur dengan menggunakan fungsi findcontour
        contours, _ = cv2.findContours(thresh_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

        for contour in contours:
            # Menghitung jumlah sisi kontur
            sides = len(cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True))
            
            # Menentukan titik tengah kontur
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                
                # Menentukan jenis objek berdasarkan jumlah sisi
                if sides == 3:
                    obj_name = "Segitiga"
                elif sides == 4:
                    x, y, w, h = cv2.boundingRect(contour)
                    aspect_ratio = float(w) / h
                    if aspect_ratio > 0.95 and aspect_ratio < 1.05:
                        obj_name = "Persegi"
                    else:
                        obj_name = "Persegi Panjang"
                elif sides > 4:
                    obj_name = "Bintang"
                else:
                    obj_name = "Lingkaran"
                
                # Menempatkan teks pada tengah objek
                cv2.putText(thresh_img, obj_name, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (127, 127, 127), 2)

        # Tampilkan hasil
        cv2.drawContours(thresh_img, contours, -1, (0,255,0), 3)
        cv2.imshow('Kontur', thresh_img)
        cv2.waitKey(0)

    def color_tracking(self):
        cam = cv2.VideoCapture(0)

        while True:
            _, frame = cam.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_color = np.array([20, 80, 50])
            upper_color = np.array([156, 232, 255])
            mask = cv2.inRange(hsv, lower_color, upper_color)
            result = cv2.bitwise_and(frame, frame,mask=mask)
            cv2.imshow("frame", frame)
            cv2.imshow("mask", mask)
            cv2.imshow("result", result)
            key = cv2.waitKey(1)
            if key == 27:
                break
        cam.release()
        cv2.destroyAllWindows()

    def color_picker(self):
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("Trackbars")

        def nothing(x): pass

        cv2.createTrackbar("L-H", "Trackbars", 0, 179, nothing)
        cv2.createTrackbar("L-S", "Trackbars", 0, 255, nothing)
        cv2.createTrackbar("L-V", "Trackbars", 0, 255, nothing)
        cv2.createTrackbar("U-H", "Trackbars", 179, 179, nothing)
        cv2.createTrackbar("U-S", "Trackbars", 255, 255, nothing)
        cv2.createTrackbar("U-V", "Trackbars", 255, 255, nothing)

        while True:
            _, frame = cam.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            l_h = cv2.getTrackbarPos("L-H", "Trackbars")
            l_s = cv2.getTrackbarPos("L-S", "Trackbars")
            l_v = cv2.getTrackbarPos("L-V", "Trackbars")
            u_h = cv2.getTrackbarPos("U-H", "Trackbars")
            u_s = cv2.getTrackbarPos("U-S", "Trackbars")
            u_v = cv2.getTrackbarPos("U-V", "Trackbars")

            lower_color = np.array([l_h, l_s, l_v])
            upper_color = np.array([u_h, u_s, u_v])
            mask = cv2.inRange(hsv, lower_color, upper_color)
            result = cv2.bitwise_and(frame, frame,mask=mask)

            cv2.imshow("frame", frame)
            cv2.imshow("mask", mask)
            cv2.imshow("result", result)

            key = cv2.waitKey(1)
            if key == 27:
                break
        
        cam.release()
        cv2.destroyAllWindows()

    def object_detection(self):
        # show cars video on camera
        cam = cv2.VideoCapture(0)
        car_cascade = cv2.CascadeClassifier('cars.xml')

        while True:
            ret, frame = cam.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            cars = car_cascade.detectMultiScale(gray, 1.1, 3)

            for (x, y, w, h) in cars:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)

            cv2.imshow("video", frame)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        
        cam.release()
        cv2.destroyAllWindows()

    def histogram_of_gradient_astro(self):
        from skimage.feature import hog
        from skimage import data, exposure

        # image = data.astronaut()
        image = cv2.imread('cabekaktus.jpg')

        fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True, channel_axis=2)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), sharex=True, sharey=True)

        ax1.axis("off")
        ax1.imshow(image, cmap=plt.cm.gray)
        ax1.set_title("Input Image")

        hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

        ax2.axis("off")
        ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
        ax2.set_title("Histogram of Oriented Gradients")
        plt.show()

    def histogram_of_gradient_pedes(self):
        import imutils
        
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        img = cv2.imread("pedestrian.jpg")

        img = imutils.resize(img, width=min(400, img.shape[0]))

        (regions, _) = hog.detectMultiScale(img, winStride=(4, 4), padding=(4, 4), scale=1.05)

        for (x, y, w, h) in regions:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

        cv2.imshow("image", img)
        cv2.waitKey()
    
    def haar_face_eye(self):
        face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        image = cv2.imread("face.jpg")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_classifier.detectMultiScale(gray, 1.1, 5)

        if faces is ():
            print("No faces found")

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (127, 0, 255), 2)
            cv2.imshow("Face Detection", image)
            cv2.waitKey(0)
        
        cv2.destroyAllWindows()

    def haar_pedestrian(self):
        body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

        cap = cv2.VideoCapture("pedestrian.avi")

        while cap.isOpened():
            ret, frame = cap.read()
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            bodies = body_classifier.detectMultiScale(gray, 1.1, 3)

            for (x, y, w, h) in bodies:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
                cv2.imshow("Pedestrian", frame)
            
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
    
    def hough_circle(self):
            img = cv2.imread('shapes4.jpg',0)
            img = cv2.medianBlur(img,5)
            cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
            circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=100,param2=120,minRadius=5,maxRadius=0)
            circles = np.uint16(np.around(circles))
            for i in circles[0,:]:
                # draw the outer circle
                cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
                # draw the center of the circle
                cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
            cv2.imshow('detected circles',cimg)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    
    def facial_landmark(self):
        PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
        predictor = dlib.shape_predictor(PREDICTOR_PATH)
        detector = dlib.get_frontal_face_detector()
        class TooManyFaces(Exception):
            pass
        class NoFaces(Exception):
            pass
        def get_landmarks(im):
            rects = detector(im, 1)
            if len(rects) > 1:
                raise TooManyFaces
            if len(rects) == 0:
                raise NoFaces
            return np.matrix([[p.x, p.y] for p in predictor(im,rects[0]).parts()])

        def annotate_landmarks(im, landmarks):
            im = im.copy()
            for idx, point in enumerate(landmarks):
                pos = (point[0, 0], point[0, 1])
                cv2.putText(im, str(idx), pos,fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,fontScale=0.4,color=(0, 0, 255))
                cv2.circle(im, pos, 3, color=(0, 255, 255))
            return im

        image = cv2.imread('emm.jpg')
        landmarks = get_landmarks(image)
        image_with_landmarks = annotate_landmarks(image, landmarks)
        cv2.imshow('Result', image_with_landmarks)
        cv2.imwrite('image_with_landmarks.jpg', image_with_landmarks)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def face_swap(self):
        PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
        SCALE_FACTOR = 1
        FEATHER_AMOUNT = 11
        FACE_POINTS = list(range(17, 68))
        MOUTH_POINTS = list(range(48, 61))
        RIGHT_BROW_POINTS = list(range(17, 22))
        LEFT_BROW_POINTS = list(range(22, 27))
        RIGHT_EYE_POINTS = list(range(36, 42))
        LEFT_EYE_POINTS = list(range(42, 48))
        NOSE_POINTS = list(range(27, 35))
        JAW_POINTS = list(range(0, 17))
        # Points used to line up the images.
        ALIGN_POINTS = (LEFT_BROW_POINTS + RIGHT_EYE_POINTS + LEFT_EYE_POINTS +
        RIGHT_BROW_POINTS + NOSE_POINTS + MOUTH_POINTS)
        
        # Points from the second image to overlay on the first. The convex hull ofeach
        # element will be overlaid.
        OVERLAY_POINTS = [
        LEFT_EYE_POINTS + RIGHT_EYE_POINTS + LEFT_BROW_POINTS +
        RIGHT_BROW_POINTS,
        NOSE_POINTS + MOUTH_POINTS,
        ]
        # Amount of blur to use during colour correction, as a fraction of the
        # pupillary distance.
        COLOUR_CORRECT_BLUR_FRAC = 0.6
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(PREDICTOR_PATH)
        class TooManyFaces(Exception):
            pass
        class NoFaces(Exception):
            pass
        def get_landmarks(im):
        # Returns facial landmarks as (x,y) coordinates
            rects = detector(im, 1)
            if len(rects) > 1:
                raise TooManyFaces
            if len(rects) == 0:
                raise NoFaces
            return np.matrix([[p.x, p.y] for p in predictor(im,rects[0]).parts()])
        def annotate_landmarks(im, landmarks):
        # Overlays the landmark points on the image itself
            im = im.copy()
            for idx, point in enumerate(landmarks):
                pos = (point[0, 0], point[0, 1])
                cv2.putText(im, str(idx), pos,
                fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
                fontScale=0.4,
                color=(0, 0, 255))
                cv2.circle(im, pos, 3, color=(0, 255, 255))
            return im
        def draw_convex_hull(im, points, color):
            points = cv2.convexHull(points)
            cv2.fillConvexPoly(im, points, color=color)
        def get_face_mask(im, landmarks):
            im = np.zeros(im.shape[:2], dtype=np.float64)

            for group in OVERLAY_POINTS:
                draw_convex_hull(im,
                landmarks[group],
                color=1)
                
                im = np.array([im, im, im]).transpose((1, 2, 0))
                im = (cv2.GaussianBlur(im, (FEATHER_AMOUNT, FEATHER_AMOUNT), 0) > 0) * 1.0
                im = cv2.GaussianBlur(im, (FEATHER_AMOUNT, FEATHER_AMOUNT), 0)
                return im

        def transformation_from_points(points1, points2):
            points1 = points1.astype(np.float64)
            points2 = points2.astype(np.float64)
            c1 = np.mean(points1, axis=0)
            c2 = np.mean(points2, axis=0)
            points1 -= c1
            points2 -= c2
            s1 = np.std(points1)
            s2 = np.std(points2)
            points1 /= s1
            points2 /= s2
            U, S, Vt = np.linalg.svd(points1.T * points2)
            R = (U * Vt).T
            return np.vstack([np.hstack(((s2 / s1) * R,c2.T - (s2 / s1) * R * c1.T)),np.matrix([0., 0., 1.])])
        def read_im_and_landmarks(image):
            im = image
            im = cv2.resize(im, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
            im = cv2.resize(im, (im.shape[1] * SCALE_FACTOR,
            im.shape[0] * SCALE_FACTOR))
            s = get_landmarks(im)
            return im, s
        def warp_im(im, M, dshape):
            output_im = np.zeros(dshape, dtype=im.dtype)
            cv2.warpAffine(im,
            M[:2],
            (dshape[1], dshape[0]),
            dst=output_im,
            borderMode=cv2.BORDER_TRANSPARENT,
            flags=cv2.WARP_INVERSE_MAP)
            return output_im
        def correct_colours(im1, im2, landmarks1):
            blur_amount = COLOUR_CORRECT_BLUR_FRAC * np.linalg.norm(np.mean(landmarks1[LEFT_EYE_POINTS], axis=0) -np.mean(landmarks1[RIGHT_EYE_POINTS], axis=0))
            blur_amount = int(blur_amount)
            if blur_amount % 2 == 0:
                blur_amount += 1
            im1_blur = cv2.GaussianBlur(im1, (blur_amount, blur_amount), 0)
            im2_blur = cv2.GaussianBlur(im2, (blur_amount, blur_amount), 0)
            # Avoid divide-by-zero errors.
            im2_blur += (128 * (im2_blur <= 1.0)).astype(im2_blur.dtype)
            return (im2.astype(np.float64) * im1_blur.astype(np.float64) /im2_blur.astype(np.float64))
            
        def swappy(image1, image2):
            im1, landmarks1 = read_im_and_landmarks(image1)
            im2, landmarks2 = read_im_and_landmarks(image2)
            M = transformation_from_points(landmarks1[ALIGN_POINTS],landmarks2[ALIGN_POINTS])
            mask = get_face_mask(im2, landmarks2)
            warped_mask = warp_im(mask, M, im1.shape)
            combined_mask = np.max([get_face_mask(im1, landmarks1),
            warped_mask],
            axis=0)
            warped_im2 = warp_im(im2, M, im1.shape)
            warped_corrected_im2 = correct_colours(im1, warped_im2, landmarks1)
            output_im = im1 * (1.0 - combined_mask) + warped_corrected_im2 *combined_mask
            cv2.imwrite('output.jpg', output_im)
            image = cv2.imread('output.jpg')
            return image
        ## Enter the paths to your input images here
        image1 = cv2.imread('emm.jpg')
        image2 = cv2.imread('atj.jpg')
        cv2.imshow('Emma Myers Face', image1)
        cv2.imshow('Anya Taylor-Joy Face', image2)
        swapped = swappy(image1, image2)
        cv2.imshow('Face Swap 1', swapped)
        swapped = swappy(image2, image1)
        cv2.imshow('Face Swap 2', swapped)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def rt_face_swap(self):
        PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
        SCALE_FACTOR = 1
        FEATHER_AMOUNT = 11
        FACE_POINTS = list(range(17, 68))
        MOUTH_POINTS = list(range(48, 61))
        RIGHT_BROW_POINTS = list(range(17, 22))
        LEFT_BROW_POINTS = list(range(22, 27))
        RIGHT_EYE_POINTS = list(range(36, 42))
        LEFT_EYE_POINTS = list(range(42, 48))
        NOSE_POINTS = list(range(27, 35))
        JAW_POINTS = list(range(0, 17))
        # Points used to line up the images.
        ALIGN_POINTS = (LEFT_BROW_POINTS + RIGHT_EYE_POINTS + LEFT_EYE_POINTS +
        RIGHT_BROW_POINTS + NOSE_POINTS + MOUTH_POINTS)
        # Points from the second image to overlay on the first. The convex hull ofeach
        # element will be overlaid.
        OVERLAY_POINTS = [
        LEFT_EYE_POINTS + RIGHT_EYE_POINTS + LEFT_BROW_POINTS +
        RIGHT_BROW_POINTS,
        NOSE_POINTS + MOUTH_POINTS,
        ]
        # Amount of blur to use during colour correction, as a fraction of the
        # pupillary distance.
        COLOUR_CORRECT_BLUR_FRAC = 0.6
        cascade_path = 'haarcascade_frontalface_default.xml'
        cascade = cv2.CascadeClassifier(cascade_path)
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(PREDICTOR_PATH)

        def get_landmarks(im, dlibOn):
            if (dlibOn == True):
                rects = detector(im, 1)
                if len(rects) > 1:
                    return "error"
                if len(rects) == 0:
                    return "error"
                return np.matrix([[p.x, p.y] for p in predictor(im,rects[0]).parts()])
            else:
                rects = cascade.detectMultiScale(im, 1.3, 5)
                if len(rects) > 1:
                    return "error"
                if len(rects) == 0:
                    return "error"
                x, y, w, h = rects[0]
                rect = dlib.rectangle(x, y, x + w, y + h)
                return np.matrix([[p.x, p.y] for p in predictor(im,rect).parts()])
            
        def annotate_landmarks(im, landmarks):
            im = im.copy()
            for idx, point in enumerate(landmarks):
                pos = (point[0, 0], point[0, 1])
                cv2.putText(im, str(idx), pos,
                fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
                fontScale=0.4,
                color=(0, 0, 255))
                cv2.circle(im, pos, 3, color=(0, 255, 255))
            return im
        def draw_convex_hull(im, points, color):
            points = cv2.convexHull(points)
            cv2.fillConvexPoly(im, points, color=color)
        def get_face_mask(im, landmarks):
            im = np.zeros(im.shape[:2], dtype=np.float64)
            for group in OVERLAY_POINTS:
                draw_convex_hull(im,
                landmarks[group],
                color=1)
            im = np.array([im, im, im]).transpose((1, 2, 0))
            im = (cv2.GaussianBlur(im, (FEATHER_AMOUNT, FEATHER_AMOUNT), 0) > 0) * 1.0
            im = cv2.GaussianBlur(im, (FEATHER_AMOUNT, FEATHER_AMOUNT), 0)
            return im

        def transformation_from_points(points1, points2):
            points1 = points1.astype(np.float64)
            points2 = points2.astype(np.float64)
            c1 = np.mean(points1, axis=0)
            c2 = np.mean(points2, axis=0)
            points1 -= c1
            points2 -= c2
            s1 = np.std(points1)
            s2 = np.std(points2)
            points1 /= s1
            points2 /= s2
            U, S, Vt = np.linalg.svd(points1.T * points2)
            R = (U * Vt).T
            return np.vstack([np.hstack(((s2 / s1) * R,c2.T - (s2 / s1) * R * c1.T)),np.matrix([0., 0., 1.])])

        def read_im_and_landmarks(fname):
            im = cv2.imread(fname, cv2.IMREAD_COLOR)
            im = cv2.resize(im, None, fx=0.35, fy=0.35,
            interpolation=cv2.INTER_LINEAR)
            im = cv2.resize(im, (im.shape[1] * SCALE_FACTOR,
            im.shape[0] * SCALE_FACTOR))
            s = get_landmarks(im, dlibOn)
            return im, s
        
        def warp_im(im, M, dshape):
            output_im = np.zeros(dshape, dtype=im.dtype)
            cv2.warpAffine(im,
            M[:2],
            (dshape[1], dshape[0]),
            dst=output_im,
            borderMode=cv2.BORDER_TRANSPARENT,
            flags=cv2.WARP_INVERSE_MAP)
            return output_im
        
        def correct_colours(im1, im2, landmarks1):
            blur_amount = COLOUR_CORRECT_BLUR_FRAC * np.linalg.norm(
            np.mean(landmarks1[LEFT_EYE_POINTS], axis=0) -
            np.mean(landmarks1[RIGHT_EYE_POINTS], axis=0))
            blur_amount = int(blur_amount)
            if blur_amount % 2 == 0:
                blur_amount += 1
            im1_blur = cv2.GaussianBlur(im1, (blur_amount, blur_amount), 0)
            im2_blur = cv2.GaussianBlur(im2, (blur_amount, blur_amount), 0)
            # Avoid divide-by-zero errors.
            im2_blur += (128 * (im2_blur <= 1.0)).astype(im2_blur.dtype)
            return (im2.astype(np.float64) * im1_blur.astype(np.float64) /
            im2_blur.astype(np.float64))

        def face_swap(img, name):
            s = get_landmarks(img, True)
            if isinstance(s, str) and s == "error":
                print("No or too many faces detected")
                return img  # Return the original image
            im1, landmarks1 = img, s
            im2, landmarks2 = read_im_and_landmarks(name)
            if isinstance(landmarks2, str) and landmarks2 == "error":
                print("No or too many faces detected in the filter image")
                return img  # Return the original image
            M = transformation_from_points(landmarks1[ALIGN_POINTS], landmarks2[ALIGN_POINTS])
            mask = get_face_mask(im2, landmarks2)
            warped_mask = warp_im(mask, M, im1.shape)
            combined_mask = np.max([get_face_mask(im1, landmarks1), warped_mask], axis=0)
            warped_im2 = warp_im(im2, M, im1.shape)
            warped_corrected_im2 = correct_colours(im1, warped_im2, landmarks1)
            output_im = im1 * (1.0 - combined_mask) + warped_corrected_im2 * combined_mask
            cv2.imwrite('output.jpg', output_im)
            image = cv2.imread('output.jpg')
            frame = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
            return image
        cap = cv2.VideoCapture(0)
        # Name is the image we want to swap onto ours
        # dlibOn controls if use dlib's facial landmark detector (better)
        # or use HAAR Cascade Classifiers (faster)
        filter_image = "emm.jpg" ### Put your image here!
        dlibOn = False
        while True:
            ret, frame = cap.read()
            # Reduce image size by 75% to reduce processing time and improve framerates
            frame = cv2.resize(frame, None, fx=0.75, fy=0.75,
            interpolation=cv2.INTER_LINEAR)
            # flip image so that it's more mirror like
            frame = cv2.flip(frame, 1)
            cv2.imshow('Our Amazing Face Swapper', face_swap(frame, filter_image))
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    
    def yawn_detection(self):
        PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
        predictor = dlib.shape_predictor(PREDICTOR_PATH)
        detector = dlib.get_frontal_face_detector()

        def get_landmarks(im):
            rects = detector(im, 1)
            if len(rects) > 1:
                return "error"
            if len(rects) == 0:
                return "error"
            return np.matrix([[p.x, p.y] for p in predictor(im, rects[0]).parts()])

        def annotate_landmarks(im, landmarks):
            im = im.copy()
            for idx, point in enumerate(landmarks):
                if not isinstance(point[0], (int, float)) or not isinstance(point[1], (int, float)):
                    continue
                pos = (int(point[0]), int(point[1]))
                cv2.putText(im, str(idx), pos,
                            fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
                            fontScale=0.4,
                            color=(0, 0, 255))
                cv2.circle(im, pos, 3, color=(0, 255, 255))
            return im

        def top_lip(landmarks):
            top_lip_pts = []
            indices = list(range(50, 53)) + list(range(61, 64))
            for i in indices:
                top_lip_pts.append(landmarks[i])
            top_lip_all_pts = np.squeeze(np.asarray(top_lip_pts))
            top_lip_mean = np.mean(top_lip_pts, axis=0)
            return int(top_lip_mean[:, 1])

        def bottom_lip(landmarks):
            bottom_lip_pts = []
            indices = list(range(65, 68)) + list(range(56, 59))
            for i in indices:
                bottom_lip_pts.append(landmarks[i])
            bottom_lip_all_pts = np.squeeze(np.asarray(bottom_lip_pts))
            bottom_lip_mean = np.mean(bottom_lip_pts, axis=0)
            return int(bottom_lip_mean[:, 1])

        def mouth_open(image):
            landmarks = get_landmarks(image)
            if isinstance(landmarks, str) or landmarks.shape[0] != 68:
                return image, 0
            image_with_landmarks = annotate_landmarks(image, landmarks)
            top_lip_center = top_lip(landmarks)
            bottom_lip_center = bottom_lip(landmarks)
            lip_distance = abs(top_lip_center - bottom_lip_center)
            return image_with_landmarks, lip_distance

        cap = cv2.VideoCapture(0)
        yawns = 0
        yawn_status = False

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            image_landmarks, lip_distance = mouth_open(frame)
            prev_yawn_status = yawn_status
            if lip_distance > 25:
                yawn_status = True
                cv2.putText(frame, "Subject is Yawning", (50, 450),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                output_text = " Yawn Count: " + str(yawns + 1)
                cv2.putText(frame, output_text, (50, 50),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 127), 2)
            else:
                yawn_status = False
            if prev_yawn_status == True and yawn_status == False:
                yawns += 1
            cv2.imshow('Live Landmarks', image_landmarks)
            cv2.imshow('Yawn Detection', frame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def displayImage(self, windows=1):
        qformat=QImage.Format_Indexed8
        if len(self.image.shape)==3: #row[0],col[1],channel[2]
            if (self.image.shape[2])==4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888
        
        img=QImage(self.image,self.image.shape[1],self.image.shape[0],
        self.image.strides[0],qformat)
        # cv membaca image dalam format BGR, PyQt membaca dalam format RGB
        img=img.rgbSwapped()

        if windows==1:
            self.img_label.setPixmap(QPixmap.fromImage(img))
            self.img_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
            self.img_label.setScaledContents(True)
        if windows==2:
            self.img_output.setPixmap(QPixmap.fromImage(img))
            self.img_output.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
            self.img_output.setScaledContents(True)

        # # menyimpan gambar hasil load di dalam imgLabel
        # self.img_label.setPixmap(QPixmap.fromImage(img))
        # # memposisikan gambar di center
        # self.img_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)


app=QtWidgets.QApplication(sys.argv)
window=ShowImage()
window.setWindowTitle('Praktikum PCD P6 Modul G1 - H3')
window.show()
sys.exit(app.exec_())
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import cv2
import numpy as np
from Ui_main_window import Ui_MainWindow
from dialogs.error import ErrorMessage
import zxingcpp
from matplotlib.image import imread

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        #UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.image_path = ""

        #Connect functions to buttons
        self.ui.Btn_open_image.clicked.connect(self.open_file)
        self.ui.Btn_decode.clicked.connect(self.decode_aztec_code)

    def open_file(self):
        file_filter = 'Image (*.bmp *.jpg *.png)'
        image_path = QFileDialog.getOpenFileName(
            parent=self,
            caption='Wybierz obraz',
            directory=os.getcwd(),
            filter=file_filter
        )
        self.image_path = image_path[0]
        self.set_image()
        

    def set_image(self, ):
        self.pixmap = QPixmap(self.image_path)
        pixmap_resized = self.pixmap.scaled(self.ui.Lb_Image.width(), self.ui.Lb_Image.height())
        self.ui.Lb_Image.setPixmap(pixmap_resized)

    def decode_aztec_code(self):
        # denoised_image = self.denoise_image_1()
        img = cv2.imread(self.image_path)
        found_aztec_codes = zxingcpp.read_barcodes(img)
        for code in found_aztec_codes:
            self.ui.Te_decoded_text.setText("Found barcode:\n Text:    '{}'\n Format:   {}\n Position: {}".format(code.text, code.format, code.position))
        if len(found_aztec_codes) == 0:
            self.ui.Te_decoded_text.setText("Could not find any barcodes.")
        cv2.imshow("image", img)

    def draw_aztec_codes_in_image(self):
        image = cv2.imread(self.image_path)
        grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(grey, 144, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)  
        
        kernel = np.ones((10, 10), np.uint8)
        thresh = cv2.dilate(thresh, kernel, iterations=1)
        
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        # cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
        bboxes = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            xmin, ymin, width, height = cv2.boundingRect(cnt)
            extent = area / (width * height)
        
             # filter non-rectangular objects and small objects
            if (extent > np.pi / 4) and (area > 800):
                bboxes.append((xmin, ymin, xmin + width, ymin + height))

        for xmin, ymin, xmax, ymax in bboxes:
            cv2.rectangle(image,(xmin,ymin),(xmax,ymax),(0,0,255),3)

        cv2.imshow("img", image)

    def denoise_image_1(self):
        img = cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)
        blur = cv2.GaussianBlur(img,(3,3),0)
        _,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        return th3
    
    def denoise_image_2(self):
        pass
    
    # def open_about_dialog(self):
    #     self.dialog = QDialog()
    #     self.ui = Ui_aboutDialog()
    #     self.ui.setupUi(self.dialog)
    #     self.dialog.exec_()

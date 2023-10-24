import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import cv2
from Ui_main_window import Ui_MainWindow
from dialogs.error import ErrorMessage
from PIL import Image
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

    #Otwarcie nowego obrazu
    def open_file(self):
        file_filter = 'Image (*.bmp *.jpg *.png)'
        image_path = QFileDialog.getOpenFileName(
            parent=self,
            caption='Wybierz obraz',
            directory=os.getcwd(),
            filter=file_filter
        )
        self.pixmap = QPixmap(image_path[0])
        pixmap_resized = self.pixmap.scaled(self.ui.Lb_Image.width(), self.ui.Lb_Image.height())
        self.ui.Lb_Image.setPixmap(pixmap_resized)
        self.image_path = image_path[0]

    def decode_aztec_code(self):
        img = cv2.imread(self.image_path)
        found_aztec_codes = zxingcpp.read_barcodes(img)
        for code in found_aztec_codes:
            self.ui.Te_decoded_text.setText("Found barcode:\n Text:    '{}'\n Format:   {}\n Position: {}".format(code.text, code.format, code.position))
        if len(found_aztec_codes) == 0:
            self.ui.Te_decoded_text.setText("Could not find any barcodes.")
        # barcode = reader.decode(self.image_path)
        # self.ui.Te_decoded_text.setText(barcode.raw)

    # def open_window(self, image_path):
    #     image = imageWindow(image_path)
    #     self.windows.append(image)
    #     imageWindow.last_active_window = image
    #     image.show()
    #     return image
    
    # def open_about_dialog(self):
    #     self.dialog = QDialog()
    #     self.ui = Ui_aboutDialog()
    #     self.ui.setupUi(self.dialog)
    #     self.dialog.exec_()

    #Zapisanie obrazu
    def save_image(self):
        if self.get_selected_image():
            file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                            "PNG(*.png);;JPEG(*.jpg *.jpeg);;")
        
            if file_path == "":
                return
            
            arr = self.get_selected_image().get_image()
            arr_to_image = Image.fromarray(arr)
            arr_to_image.save(file_path)
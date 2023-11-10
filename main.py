from PyQt5.QtWidgets import QApplication
import sys
from main_window import MainWindow
import zxingcpp
import cv2 as cv

if __name__ == "__main__":   
    app = QApplication(sys.argv)
    window = MainWindow() 
    window.show()
    sys.exit(app.exec())
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton)
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QGuiApplication

class Frontend(QWidget):

    def __init__(self):
        super().__init__()
        self.init_gui()
    
    def init_gui(self):
        self.setWindowTitle("WeatherApp")

        window = QGuiApplication.primaryScreen()
        window_geometry = window.geometry()

        width = int(window_geometry.width() * 0.8)
        height = int(window_geometry.height() * 0.8)
        pos_x = (window_geometry.width() - width) // 2
        pos_y = (window_geometry.height() - height) // 2
        self.setGeometry(pos_x, pos_y, width, height)

        

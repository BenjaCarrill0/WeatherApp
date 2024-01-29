from frontend.frontend import Frontend
from PyQt6.QtWidgets import QApplication
from sys import exit


if __name__ == "__main__":
    app = QApplication([])
    window = Frontend()
    window.show()
    exit(app.exec())
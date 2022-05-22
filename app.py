import sys
import PyQt6.QtWidgets as QtWidgets
from main import MainWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = MainWindow()
    
    Window.show()
    
    sys.exit(app.exec())
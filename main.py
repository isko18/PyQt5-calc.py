from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
import sys

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Python PyQt5")
    window.setGeometry(400, 400, 400, 400)

    main_text = QtWidgets.QLabel(window)
    main_text.setText("Hello world")
    main_text.move(100, 100)

    main_button = QtWidgets.QPushButton(window)
    main_button.setText("Нажми")
    main_button.move(135, 190)

    window.show()
    sys.exit(app.exec_())
application()
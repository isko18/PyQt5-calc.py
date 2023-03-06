from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys

class CustomCalculator(QMainWindow):
    def __init__(self):
        super(CustomCalculator, self).__init__()
        
        loadUi('calc.ui',self)

        self.add.clicked.connect(self.add_num)
        self.sub.clicked.connect(self.sub_num)
        self.mult.clicked.connect(self.mult_num)
        self.div.clicked.connect(self.div_num)

    def add_num(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())   
            self.result.setText(f"Ответ: {num1 + num2}")
        except:
            self.result.setText("Введите цифры")

    def sub_num(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            self.result.setText(f"Ответ: {num1,f'0' - num2,f'0'}")
        except:
            self.result.setText("Введите цифры")

    def mult_num(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            self.result.setText(f"Ответ: {num1 * num2}")
        except:
             self.result.setText("Введите цифры")
            
    def div_num(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
        
            self.result.setText(f"Ответ: {num1 / num2}")
        except: 
            ZeroDivisionError
            self.result.setText("На ноль делить нельзя")

        

            


app = QApplication(sys.argv)
calc = CustomCalculator()
calc.show()
app.exec_()
# .\ven
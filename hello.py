from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle("Hello")
		layout = QGridLayout()
		self.setLayout(layout)
		label = QLabel("Hello, World!, Minh la Thang")
		layout.addWidget(label, 0, 0)
app = QApplication(sys.argv)
screen = Window()
screen.show()
#print(sys.modules)
app.exec_()
#sys.exit(app.exec_())


from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
import sys
class window(QWidget,QWindow):
	"""docstring for window"""
	def __init__(self):
		QWidget.__init__(self)
		QWindow.__init__(self)
		self.resize(400,300)
		layout = QBoxLayout(QBoxLayout.LeftToRight) #khoi tao
		self.setLayout(layout)
		label = QLabel("Tran Thang")
		layout.addWidget(label, 0)
		label1 = QLabel("Hust")
		layout.addWidget(label1, )
		
app = QApplication(sys.argv)
screen = window()		
screen.show()
sys.exit(app.exec_())
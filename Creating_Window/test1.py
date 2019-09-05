from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
class Window(QWindow):
	def __init__(self):
		QWindow.__init__(self)
		self.setTitle("Window")
		self.resize(400, 300)
		self.showFullScreen()
app = QApplication(sys.argv)
screen = Window()
screen.show()
#screen.showFullScreen()
sys.exit(app.exec_())
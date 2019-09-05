#windown.py
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class window(QWindow):
	#docstring for window
	def __init__(self):
		#super(window, self).__init__() #khong co bien gi can ke thua
		QWindow.__init__(self)
		self.resize(400,300)
		self.setTitle("Tran Thang")

app = QApplication(sys.argv) #tra ve mot so danh sach lenh dc truyen cho tap lenh python
Thang = window()
Thang.setTitle("Tran Viet Thang_v1")
Thang.show()
Thang.setMinimumWidth(1000)
Thang.setMaximumWidth(500)  # ko dieu chinh dc khung cua so
Thang.show()
sys.exit(app.exec_()) # thoat ung dung
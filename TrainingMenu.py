# convert UI to Py command : pyuic5 -x TrainingMenu.ui -o TrainingMenuUI.py

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from TrainingMenuUI import Ui_Dialog
from Raw_DataCollector import RawDataCollector
import threading
import time
import threading


class TrainingMenu(Ui_Dialog):

	remainingSeconds = 30 # Training Time in seconds

	def __init__(self, dialog):

		global chooseDirectoryText,progressBar,timeRemainingLabel

		Ui_Dialog.__init__(self)
		self.setupUi(dialog)
		chooseDirectoryText = self.chooseDirectoryText
		timeRemainingLabel = self.timeRemainingLabel
		progressBar = self.progressBar
		self.startBtn.clicked.connect(self.startBtnClicked)
		self.endBtn.clicked.connect(self.endBtnClicked)
		self.chooseDirectoryBtn.clicked.connect(self.chooseDirectoryBtnClicked)
		self.rawDataCollector = RawDataCollector()
		
	def startBtnClicked(self):
		print("Start Button Clicked")
		self.rawDataCollector.setFileName(self.chooseDirectoryText.text())
		self.rawDataCollector.start()
		self.remainingSeconds = 30
		self.trainingTimer()
		self.changeTimer("0:30",30)
		self.startBtn.setEnabled(False)

	def endBtnClicked(self):
		print("End Button Clicked")
		self.remainingSeconds = 0
		progressBar.setProperty("value", 0)
		self.rawDataCollector.stop()
		self.startBtn.setEnabled(True)

	def chooseDirectoryBtnClicked(self):
		print("Choose Directory Button Clicked")
		
	def changeTimer(self,value,seconds):
		timeRemainingLabel.setText(value)
		#progressBar.setProperty("value", int(100*(300-seconds)/300))

	def trainingTimer(self):
		if(self.remainingSeconds > 0):
			threading.Timer(1.0, self.trainingTimer).start()
			self.remainingSeconds -= 1
			print(self.remainingSeconds)
			timeString = ""
			timeString +=  str( self.remainingSeconds / 60 ) + ":"
			if ((self.remainingSeconds % 60) < 10):
				timeString += "0"
			timeString += str( self.remainingSeconds % 60 )
			self.changeTimer(timeString,self.remainingSeconds)
		else:
			self.rawDataCollector.stop()
			self.startBtn.setEnabled(True)

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()

	prog = TrainingMenu(dialog)

	dialog.show()
	sys.exit(app.exec_()) 
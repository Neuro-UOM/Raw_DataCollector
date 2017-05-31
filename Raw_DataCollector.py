import platform
import time

from emokit.emotiv import Emotiv
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal)

class RawDataCollector(QThread):
    flag = False
    file_name = ""

    if platform.system() == "Windows":
        pass

    def setFileName(self,file_name):
        self.file_name = file_name

    def run(self):
        self.flag = True
        self.CollectRawData(self.file_name)

    def stop(self):
        self.flag = False

    def CollectRawData(self, file_name):
        with Emotiv(display_output=True, verbose=True, write=True, file_name = self.file_name) as headset:
            print("Serial Number: %s" % headset.serial_number)
            print("Exporting data... press control+c to stop.")

            while headset.running:
                try:
                    if not (self.flag):
                        break
                        headset.stop()
                    packet = headset.dequeue()
                except Exception:
                    headset.stop()
                time.sleep(0.001)
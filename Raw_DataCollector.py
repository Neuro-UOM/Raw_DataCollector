import platform
import time

from emokit.emotiv import Emotiv
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal)

class RawDataCollector(QThread):
    flag = False

    if platform.system() == "Windows":
        pass

    def run(self):
        self.flag = True
        self.CollectRawData()

    def stop(self):
        self.flag = False

    def CollectRawData(self):
        with Emotiv(display_output=True, verbose=True, write=True) as headset:
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
import platform
import time

from emokit.emotiv import Emotiv

if platform.system() == "Windows":
    pass


def CollectRawData():
    with Emotiv(display_output=True, verbose=True, write=True) as headset:
        print("Serial Number: %s" % headset.serial_number)
        print("Exporting data... press control+c to stop.")

        while headset.running:
            try:
                packet = headset.dequeue()
            except Exception:
                headset.stop()
            time.sleep(0.001)
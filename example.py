# -*- coding: utf-8 -*-
# This is an example of popping a packet from the Emotiv class's packet queue
# and printing the gyro x and y values to the console. 


import time

from emokit.emotiv import Emotiv

if __name__ == "__main__":
    with Emotiv(display_output=True, write=True, write_decrypted=True, verbose=True, output_path= "data") as headset:
        while True:
            packet = headset.dequeue()
            if packet is not None:
                pass
            time.sleep(4)

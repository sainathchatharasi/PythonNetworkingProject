#Author: Chatharasi Sainath

from scapy.all import *
import psutil
import os
from threading import Thread
import pandas as pd
import time

class Bandwidth:
    UPDATE_DELAY = 1

    def get_size(bytes):
        for unit in ['','K','M','G','T','P']:
            if bytes < 1024:
                return f"{bytes:.2f}{unit}B"
            bytes /=1024
    #used to get network input/output statistics in the form of a tuple
    io = psutil.net_io_counters(pernic = True)
    while True:
        #time.sleep(UPDATE_DELAY)
        io_2 = psutil.net_io_counters(pernic = True)
        data = []
        for iface, iface_io in io.items():
            upload_speed, download_speed = io_2[iface].bytes_sent - iface_io.bytes_sent, io_2[iface].bytes_recv - iface_io.bytes_recv
            data.append({
            "iface":iface, "Download": get_size(io_2[iface].bytes_recv),
            "upload" : get_size(io_2[iface].bytes_sent),
            "upload speed": f"{get_size(upload_speed / UPDATE_DELAY)}/s",
            "Download Speed":f"{get_size(download_speed/UPDATE_DELAY)}/S",
            })
        io = io_2
        df = pd.DataFrame(data)
        df.sort_values("Download", inplace = True, ascending = False)
        os.system("cls") if "nt" in os.name else os.system("clear")
        #to print output as console friendly tabular format
        print(df.to_string())
        
Get_Bandwidth = Bandwidth()
Get_Bandwidth()
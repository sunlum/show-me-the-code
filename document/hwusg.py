#!coding=utf-8
import socket
import time
import os
from datetime import datetime

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_port = ('10.65.133.133', 1600)

while True:
    count = 10000000
    while True:
        #time_with_year = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        time_with_year = datetime.now().strftime('%b %d %H:%M:%S')
        data = '''<145>2019-06-11 08:08:08 SVN5560 %%01AAA/3/AAA_MODIFY_PWD_FAIL(l): The user modify password failed. (User=username)'''
        data = data.format(time_with_year)
        client.sendto(data.encode(),ip_port)
        count = count -1
        #time.sleep(0.0001)
        time.sleep(0.01)
client.close()
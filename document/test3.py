#!coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import socket
import time
import os
from datetime import datetime

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_port = ('10.65.133.159', 2200)

while True:
    count = 10000000
    while True:
        #time_with_year = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        time_with_year = datetime.now().strftime('%b %d %H:%M:%S')
        data = '''<123>July 8 10:59:37 192.168.28.111 Nov 30 10:59:37 ips IPS: SerialNum=0113241512089995 GenTime=\"2017-11-30 10:59:37\" SrcIP=218.92.145.97 SrcIP6= SrcIPVer=4 DstIP=192.168.53.10 DstIP6= DstIPVer=4 Protocol=TCP SrcPort=33313 DstPort=80 InInterface=ge1/7 OutInterface=ge1/8 SMAC=ac:74:09:39:5c:44 DMAC=9c:06:1b:bd:c4:01 FwPolicyID=2 EventName=HTTP_XSS脚本注入 EventID=152526081 EventLevel=2 EventsetName=daytime SecurityType=注入攻击 SecurityID=28 ProtocolType=HTTP ProtocolID=10 Action=PASS Vsysid=0 Content=\"URL(1702)::r=%257B%2522dateTime%2522%253A1512010777339%252C%2522sId%2522%253A%2522bdca838cb9d461c4%2522%252C%2522msgType%2522%253A%2522unload%2522%252C%2522vsn%2522%253A%25221006%2522%252C%2522siteId%2522%253A%2522CM-Prod%2522%252C%2522pid%2522%253A%2522b9d461c47021bdd1%2522%252C%2522activities%2522%253A%255B%255B%2522%2522%252C%2522%2522%252C%2522A%253Alink%2522%252C%2522click%2522%252C%2522%257B%253CIM;HOST=www.chinamoney.com.cn;URL=/ulta.webtracker/?r=%257B%2522dateTime%2522%253A1512010777339%252C%2522sId%2522%253A%2522bdca838cb9d461c4\" CapToken= EvtCount=1'''
        client.sendto(data.encode(),ip_port)
        count = count -1
        #time.sleep(0.0001)
        time.sleep(0.01)
client.close()

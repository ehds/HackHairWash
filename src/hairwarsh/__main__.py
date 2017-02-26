#!/usr/bin/env python  
  
import sys;  
import getopt;  
from .ipget import *
from .Proxy import *
def usage():  
    a= """
        '''    '''    ''''      ''''    ''  ''
        ''     ''    ''  ''      ''     ''''  ''
        '''''''''    '''''''     ''     ''
        ''     ''   ''     ''    ''     ''
        '''    '''  ''      ''  ''''    ''
       """
    usage ="""
    
        [+] -h --help   :help
        [+] -i --ip     :set the ip adress you want to proxy 
        [+] -p --port   :set the port you want to proxy
    """   
    print(a+'\n'+"Usage:%s [options] " %('hair')+'\n'+usage);  
        

 	
def main():
    #lsArgs = [""];  
    shortopts = "hi:p:"
    longopts = ['help','ip=','port=']
    ip=get_ip_address()
    port ='8080'
    try:  
        opts,args = getopt.getopt(sys.argv[1:], shortopts, longopts);   
          
        #check all param  
        for opt,arg in opts:  
            if opt in ("-h", "--help"):  
                usage();  
                sys.exit(1);  
            elif opt in ("-i", "--ip"):
                ip = arg       
            elif opt in ("-p", "--port"):
                port =arg

        print "you set ip:%s,port=%s"%(ip,port)
        start_proxy(ip=ip,port=port)
    except getopt.GetoptError:  
        print("getopt error!");  
        usage();  
        sys.exit(1);
if __name__ == '__main__':
    main()
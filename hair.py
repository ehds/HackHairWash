#!/usr/bin/env python  

import os
import sys
_filepath =  os.path.dirname(os.path.realpath(__file__))
_srcpath = _filepath+"/src/"
print _srcpath
sys.path.insert(1,os.path.join(_srcpath))
if __name__ == '__main__':
    import hairwarsh
    hairwarsh.main()
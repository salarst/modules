#!/home/tops/bin/python
#****************************************************************#
# ScriptName: salarsM.py
# Author: LeiChengliang
# Create Date: 2017-10-14 13:25
# Modify Author: $SHTERM_REAL_USER@alibaba-inc.com
# Modify Date: 2017-10-14 15:14
# Function: LOG,FColors
#***************************************************************#
###############################################################################################
#LOG:                                                                                         #  
#   instance need two arguments,one is logfilename,another is logdir                          #          
#   cleanlog:delete the logfile when the size of logfile greater than 100M                    #
#   log:will create logfile on the path of scripts                                            #  
#       you must give level(like INFO/WARN/ERROR) and msg(log content) to this method         #
#       msg's type must be list/tuple/str,others will raise an Exception                      #  
###############################################################################################        
import os
import sys
import time

class LOG():
    def __init__(self,logFileName,path):
        self.logFileName = logFileName
        self.path = path
    def cleanlog(self):
        path = os.path.join(self.path,self.logFileName)
        if os.path.exists(path):
            size = os.path.getsize(path)/1024/1024
            if size > 100:
                os.remove(path)
        
    def log(self,msg,level):
        currentTime = time.strftime('%Y-%m-%d %X',time.localtime())
        if type(msg) in [tuple,list]:
            msg = ' '.join(msg)
        elif type(msg) == str:
            pass
        else:
            raise Exception('TypeError: only accept list/tuple or str paramters,please check your type of parameter')
            sys.exit()
        fd = open(os.path.join(self.path,self.logFileName),'ab+')
        fd.write('==[%s %s] %s\n'%(currentTime,level,msg))
        fd.close()
    def test(self):
        self.log('test','INFO')
        os.system('cat test.log')
        self.cleanlog()
        os.remove('test.log')

if __name__ == '__main__':
    path = os.path.dirname(__file__)
    LOG('test.log',path).test()

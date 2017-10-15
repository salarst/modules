# modules
###############################################################################################
#LOG:                                                                                         #  
#   instance need two arguments,one is logfilename,another is logdir                          #          
#   cleanlog:delete the logfile when the size of logfile greater than 100M                    #
#   log:will create logfile on the path of scripts                                            #  
#       you must give level(like INFO/WARN/ERROR) and msg(log content) to this method         #
#       msg's type must be list/tuple/str,others will raise an Exception                      #  
############################################################################################### 
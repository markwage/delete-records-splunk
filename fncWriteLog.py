from datetime import datetime

#=================================================
# Module to write logrecord
#=================================================

def writeLogRecord(arg1, arg2):
    currentTime = datetime.now()
    print ("%s %s %s" % (currentTime, arg1, arg2))

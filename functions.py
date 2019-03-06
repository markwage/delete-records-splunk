from datetime import datetime

#=================================================
# Function to write logrecord.
# 06-03 08:45 Test met git
#=================================================
def writeLogRecord(arg1, arg2):
    currentTime = datetime.now()
    print ("%s %s %s" % (currentTime, arg1, arg2))

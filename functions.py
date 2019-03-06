from datetime import datetime

#=================================================
# Function to write logrecord.
# 06-03 08:45 Test met git
# 06-03 09:26 Nogmaals een test
#=================================================
def writeLogRecord(arg1, arg2):
    currentTime = datetime.now()
    print ("%s %s %s" % (currentTime, arg1, arg2))

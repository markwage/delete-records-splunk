#===========================================================
# 
#===========================================================

from datetime import datetime
from functions import writeLogRecord

strDirectory = "C:\\Users\\Mark\\OneDrive\\Documenten\\eclipse-workspace\\"
strInputFile = strDirectory + "im006222113Debug.txt"
writeLogRecord("INFO", "Inputfile: " + strInputFile)
strOutputFile = strDirectory + "im006222113DebugFiltered.txt"
writeLogRecord("INFO", "Outputfile: " + strOutputFile)
strOutputFileRemoved = strDirectory + "im006222113DebugRemoved.txt"
writeLogRecord("INFO", "Removed records in: " + strOutputFileRemoved)

whatToDelete = ["MDC", "CookieFactory", "MultiFunctionsLoadMonitor", "printIfFound"]

writeLogRecord("INFO", "Start met inlezen van de file")

with open(strInputFile) as log, open(strOutputFile, "w") as outputFile, open(strOutputFileRemoved, "w") as outputFileRemoved :
    
    for line in log:
        for toDelete in whatToDelete:
            if toDelete in line:
                outputFileRemoved.write(line)
                break
            else:
                if toDelete == "printIfFound":
                    outputFile.write(line)
                    break

writeLogRecord("INFO", "Inputfile is weggeschreven en overbodige records zijn verwijderd")

#==========================================================================            
# Count number of lines in the files to see how many records are deleted
#==========================================================================

numLinesInput = sum(1 for line in open(strInputFile))
numLinesOutput = sum(1 for line in open(strOutputFile))
numLinesRemoved = sum(1 for line in open(strOutputFileRemoved))
print ("Aantal inputrecords : %d" % numLinesInput)
print ("Aantal outputrecords: %d" % numLinesOutput)
print ("Totaal aantal lines removed: %d" % numLinesRemoved)
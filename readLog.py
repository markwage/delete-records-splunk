#===========================================================
# import time
#===========================================================

from datetime import datetime
strDirectory = "C:\\Users\\Mark\\OneDrive\\Documenten\\eclipse-workspace\\"
strInputFile = "C:\\Users\\Mark\\OneDrive\\Documenten\\eclipse-workspace\\im006222113Debug.txt"
strOutputFile = strDirectory + "im006222113DebugFiltered.txt"
strOutputFileRemoved = strDirectory + "im006222113DebugRemoved.txt"

whatToDelete = ["MDC", "CookieFactory", "MultiFunctionsLoadMonitor", "printIfFound"]

currentTime = datetime.now()
print ("%s Start met inlezen van de file" % currentTime)

with open(strInputFile) as log, open(strOutputFile, "w") as outputFile, open(strOutputFileRemoved, "w") as outputFileRemoved :
    
    for line in log:
        for toDelete in whatToDelete:
        #if "MDC" in line or "CookieFactory" in line or "MultiFunctionsLoadMonitor" in line or line.count(';') <=2:
            if toDelete in line:
                outputFileRemoved.write(line)
                break
            else:
                if toDelete == "printIfFound":
                    outputFile.write(line)
                    break
            #if line.count(';') != 15:
                #print (line)
                #print (line.count(';'))

currentTime = datetime.now()
print ("%s File is gefilterd en weggeschreven" % currentTime)

#==========================================================================            
# Count number of lines in the files to see how many records are deleted
#==========================================================================

numLinesInput = sum(1 for line in open(strInputFile))
numLinesOutput = sum(1 for line in open(strOutputFile))
numLinesRemoved = sum(1 for line in open(strOutputFileRemoved))
print ("Aantal inputrecords : %d" % numLinesInput)
print ("Aantal outputrecords: %d" % numLinesOutput)
print ("Totaal aantal lines removed: %d" % numLinesRemoved)
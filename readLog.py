#===========================================================
# 
#===========================================================
from functions import writeLogRecord

strDirectory = "C:\\Users\\Mark\\OneDrive\\Documenten\\eclipse-workspace\\"
strInputFile = strDirectory + "im006222113Debug.txt"
writeLogRecord("INFO", "Inputfile: " + strInputFile)
strOutputFile = strDirectory + "im006222113DebugFiltered.txt"
writeLogRecord("INFO", "Outputfile: " + strOutputFile)
strOutputFileRemoved = strDirectory + "im006222113DebugRemoved.txt"
writeLogRecord("INFO", "Removed records in: " + strOutputFileRemoved)
# De waarde printIfFound altijd als laatste laten staan.
whatToDelete = ["MDC", "CookieFactory", "MultiFunctionsLoadMonitor", "printIfFound"]

writeLogRecord("INFO", "Start met inlezen van de file")

with open(strInputFile) as log, open(strOutputFile, "w") as outputFile, open(strOutputFileRemoved, "w") as outputFileRemoved :
    for record in log:
        for toDelete in whatToDelete:
            if toDelete in record:
                outputFileRemoved.write(record)
                break
            else:
                # Wanneer printIfFound, dan zijn geen van de voorgaande waarden tegen gekomen
                if toDelete == "printIfFound":
                    outputFile.write(record)
                    break

writeLogRecord("INFO", "Inputfile is weggeschreven en overbodige records zijn verwijderd")
writeLogRecord("INFO", "De strings die verwijderd zijn: %s " % whatToDelete)

#==========================================================================            
# Count number of lines in the files to see how many records are deleted
#==========================================================================

numLinesInput = sum(1 for line in open(strInputFile))
numLinesOutput = sum(1 for line in open(strOutputFile))
numLinesRemoved = sum(1 for line in open(strOutputFileRemoved))
writeLogRecord("INFO", "Aantal inputrecords: %d" % numLinesInput)
writeLogRecord("INFO", "Aantal outputrecords: %d" % numLinesOutput)
writeLogRecord("INFO", "Totaal aantal lines removed: %d" % numLinesRemoved)
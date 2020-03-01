#%%
import csv
import sys

if len(sys.argv) == 1:
    exit("\n no arguments supplied! \n")

if len(sys.argv) == 2:
    exit("\n must supply both input and output filenames ! \n")

inputFile = sys.argv[1]
outputFile = sys.argv[2]

tmp = open(inputFile, 'r')
fileIn = csv.DictReader(tmp)
data = list(fileIn)

portColumn = [ sub['Port Name'] for sub in data]
stateColumn = [ sub['State'] for sub in data]
codeColumn = [ sub['Port Code'] for sub in data]
borderColumn = [ sub['Border'] for sub in data]
dateColumn = [ sub['Date'] for sub in data]
measureColumn = [ sub['Measure'] for sub in data]
valueColumn = [ int(sub['Value']) for sub in data]

uniquePorts = sorted(list(set(portColumn)))
uniqueStates = sorted(list(set(stateColumn)))
uniqueCodes = sorted(list(set(codeColumn)))
uniqueBorders = sorted(list(set(borderColumn)))
uniqueDates = sorted(list(set(dateColumn)), reverse=True)
uniqueMeasures = sorted(list(set(measureColumn)))

# Boolean masks

def booleanMask(column):
    columnData = [ sub[column] for sub in data]
    uniqueValues = sorted(list(set(columnData)))
    mask = {key: None for key in uniqueValues}
    for i in uniqueValues:
        mask[i] = list(map(int, [x == i for x in columnData]))
    return mask

booleanMask('Measure')

def flooredMean(input):
    input = list(filter(lambda x: (x > 0), input))
    posCount = len(input)
    if posCount > 0:
        return round(sum(input)/ len(input))
    else:
        return 0

fileOut = open(outputFile, "w")


# aggregation 
for date in uniqueDates:
    for border in uniqueBorders:
        for measure in uniqueMeasures:
            combinedMask = [a * b * c for a, b, c in zip(booleanMask('Date')[date], booleanMask('Border')[border], booleanMask('Measure')[measure])]
            count = flooredMean([a * b for a, b in zip(combinedMask, valueColumn)])#print(date, measure, booleanMask('Date')[date], booleanMask('Measure')[measure], combinedMask, "\n")
            if count > 0:
                rowOut = border + "," + date + "," + measure + "," + str(count) + "\n"
                print(rowOut)
                fileOut.write(rowOut)

fileOut.close()

### running average 

### sorting
input_file, test_input_file = 'day13_input', 'day13_test_input'

test = False

file = test_input_file if(test) else input_file

with open(file, 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    
if(test):
    startTime = 1
else:
    startTime = 100000000000000
    
offsetDict = {}
busDepartures = {}
busList = []
offset = 0

lcm = 1

for l in lines[1].split(','):
    if l != 'x':
        offsetDict[int(l)] = offset
        busList.append(int(l))
        lcm *= int(l)
        
    offset += 1
    
maxBus, maxBusOffset = max(busList), offsetDict[max(busList)]

for k, v in offsetDict.items():
    offsetDict[k] = v - maxBusOffset
    
minBusOffset = min(offsetDict.values())

while True:
    if(startTime % maxBus == 0):
        break
    startTime += 1

print(offsetDict, lcm, startTime)

flag = 0 
multiplier = 0

while True:
    sum = 0
    
    #positiveStep = lcm + multiplier*maxBus
    negativeStep = lcm - multiplier*maxBus
    
#     for id in busList:
#         busDeparture = positiveStep + offsetDict[id]
#         sum += 1 if (busDeparture % id == 0) else 0
    
#     if sum == len(busList):
#         print(positiveStep+minBusOffset)
#         break

    sum = 0
    for id in busList:
        busDeparture = negativeStep + offsetDict[id]
        sum += 1 if (busDeparture % id == 0) else 0
    
    if sum == len(busList):
        print(negativeStep+minBusOffset)
        break

    multiplier += 1
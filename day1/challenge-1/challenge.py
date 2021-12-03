with open('input.txt') as f:
    increasedTotal = 0
    lastNum = None

    for line in f:
        line = int(line)
        if lastNum is not None and line > lastNum:
            increasedTotal += 1
        lastNum = line
        
print(increasedTotal)
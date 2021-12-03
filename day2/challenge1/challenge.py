with open('input.txt') as f:
    position = [0, 0]

    for line in f:
        print(line)
        instruction = line.split()[0]
        amount = int(line.split()[1])

        if instruction == 'forward':
            position[0] += amount
        elif instruction == 'down':
            position[1] += amount
        elif instruction == 'up':
            position[1] -= amount
    
    print(position)
    finalPosition = position[0] * position[1]
    print(finalPosition)

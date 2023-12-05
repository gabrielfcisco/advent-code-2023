
if __name__ == "__main__":
    
    fileInput = open("input.txt", "r")
    special_characters = "!@#$%^&*()-+?_=,<>/"

    matrix = [line for line in fileInput]

    adjacents = [[-1,-1], [-1, 0], [-1, 1],
                 [0, -1],          [0, 1],
                 [1, -1], [1, 0],  [1, 1],]
    
    fileInput.seek(0)

    symbolsPos = [[lineIndex,index] for lineIndex, line in enumerate(fileInput) for index, char in enumerate(line) if char in special_characters]

    totalSum = 0
    num = ""
    for symbol in symbolsPos:
        prevNumber = "0"
        for pos in adjacents:
            y = symbol[0]+pos[0]
            x = symbol[1]+pos[1]
            if(matrix[y][x].isdigit()):
                num = matrix[y][x]
                i = 1
                while(x-i >= 0 and matrix[y][x-i].isdigit()):
                    num = matrix[y][x-i]+num
                    i+=1

                i = 1
                while(x+i < len(matrix[y]) and matrix[y][x+i].isdigit()):
                    num = num + matrix[y][x+i]
                    i += 1
                if prevNumber != num:
                    totalSum += int(num)
                    prevNumber = num

    print(f'Soma dos valores: {totalSum}')

    special_characters = "*"
    fileInput.seek(0)
    matrix = [line for line in fileInput]
    adjacents = [[-1,-1], [-1, 0], [-1, 1],
                 [0, -1],          [0, 1],
                 [1, -1], [1, 0],  [1, 1],]
    fileInput.seek(0)
    symbolsPos = [[lineIndex,index] for lineIndex, line in enumerate(fileInput) for index, char in enumerate(line) if char in special_characters]

    totalSum = 0
    num = ""
    for symbol in symbolsPos:
        prevNumber = "0"
        for pos in adjacents:
            y = symbol[0]+pos[0]
            x = symbol[1]+pos[1]
            if(matrix[y][x].isdigit()):
                num = matrix[y][x]
                i = 1
                while(x-i >= 0 and matrix[y][x-i].isdigit()):
                    num = matrix[y][x-i]+num
                    i+=1

                i = 1
                while(x+i < len(matrix[y]) and matrix[y][x+i].isdigit()):
                    num = num + matrix[y][x+i]
                    i += 1
                if prevNumber != num:
                    totalSum += int(num)* int(prevNumber)
                    prevNumber = num
                    
    print(f'Soma dos valores: {totalSum}')
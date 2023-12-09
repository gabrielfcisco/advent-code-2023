if __name__ == "__main__":

    fileInput = open("input.txt", "r")

    cards = [numbers.split(None) for line in fileInput for card in [line.split(": ")] for numbers in card[1].split("| ")]
    totalSum = 0
    for index in range(0, len(cards), 2):
        point = len([value for value in cards[index] if value in cards[index+1]])
        if point > 0 :
            totalSum += 2 ** (point-1)

    print(f'Soma dos valores: {totalSum}')

    fileInput.seek(0)
    
    cards = [numbers.split(None) for line in fileInput for card in [line.split(": ")] for numbers in card[1].split("| ")]
    scratchcards = [1] * int(len(cards)/2)

    for index in range(0, len(cards), 2):
        points = len([value for value in cards[index] if value in cards[index+1]])
        for point in range(points):
            scratchcards[int(index/2)+point+1] += scratchcards[int(index/2)]

    totalSum = sum(scratchcards[:int(index/2)+1])    
    print(f'Soma dos valores: {totalSum}')


#ref:<https://prepfortech.io/leetcode-solutions/best-poker-hand>
from collections import Counter
if __name__ == "__main__":
    with open("test.txt", "r", encoding="utf-8") as f:
        fileInput = f.read()
        lines = fileInput.split('\n')
        hand = [line.split(" ") for line in lines]
        five = []
        four = []
        full = []
        three = []
        two = []
        one = []
        high = []
        print(hand)
        for i in hand:
            count = list(Counter(i[0]).values())
            print(count)
            if 5 in count:
                five.append(i)
            elif 4 in count:
                four.append(i)
            elif 3 in count and 2 in count:
                full.append(i)
            elif 3 in count:
                three.append(i)
            elif 2 in count:
                if count.count(2) > 1:
                    two.append(i)
                else:
                    one.append(i)
            else:
                high.append(i)

        print(five, four, full, three, two, one, high)

        if high:


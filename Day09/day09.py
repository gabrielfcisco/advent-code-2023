def part1(datas):
    aux = []
    sum_ext = 0
    for data in datas:
        result = []
        result.append(int(data[-1]))
        aux = data
        while len(set(aux)) > 1:
            aux1 = []
            for i in range(len(aux)-1):
                aux1.append(int(aux[i+1]) - int(aux[i]))
            aux = aux1
            result.append(aux[-1])
        sum_ext += sum(result)

    return (sum_ext)


def part2(datas):
    aux = []
    sum_ext = 0
    for data in datas:
        result = []
        result.append(int(data[0]))
        aux = data
        while len(set(aux)) > 1:
            aux1 = []
            for i in range(len(aux)-1):
                aux1.append(int(aux[i+1]) - int(aux[i]))
            aux = aux1
            result.append(aux[0])
        sum_aux = result[-2] - result[-1]
        for i in range(len(result)-3, -1, -1):
            sum_aux = result[i] - sum_aux
        sum_ext += sum_aux

    return (sum_ext)

if __name__ == "__main__":
    with open("test.txt", "r", encoding="utf-8") as f:
        fileInput = f.read()
        lines = fileInput.split('\n')
        datas = [line.split(" ") for line in lines]
        print(f'Part 1: {part1(datas)}')
        print(f'Part 2: {part2(datas)}')

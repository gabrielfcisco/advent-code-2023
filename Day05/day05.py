def convert_range(lines_to_convert: list, index_input: int):
    dic_prev = {}
    for index_convert, line in enumerate(lines_to_convert):
        line = line.strip()
        if not line:
            break
        range1 = [int(i) for i in line.split(None)]
        a = [a for a in range(range1[1], range1[1] + range1[2])]
        b = [b for b in range(range1[0], range1[0] + range1[2])]
        a_to_b = {a: b for a, b in zip(a, b)}
        dic_prev.update(a_to_b)

    print(dic_prev)

    return dic_prev, index_input + index_convert + 2


if __name__ == "__main__":
    with open("test.txt", "r") as fileInput:
        fileInput = fileInput.readlines()

        seeds = fileInput[0].split(":")[1].split(None)

        print(seeds)
        index = 3
        seedToSoil, index = convert_range(fileInput[index:], index)
        soilToFertilizer, index = convert_range(fileInput[index:], index)
        fertilizerToWater, index = convert_range(fileInput[index:], index)
        waterToLight, index = convert_range(fileInput[index:], index)
        lightToTemperature, index = convert_range(fileInput[index:], index)
        temperatureToHumidity, index = convert_range(fileInput[index:], index)
        humidityToLocation, index = convert_range(fileInput[index:], index)





def convert_range(lines_to_convert: list, index_input: int, seeds: list):
    dic_prev = {}
    aux_list = seeds.copy()
    for index_convert, line in enumerate(lines_to_convert):

        line = line.strip()
        
        if not line:
            break

        range1 = [int(i) for i in line.split(None)]

        for seed in seeds:
            if range1[1] <= seed <= range1[1]+range1[2]-1: 
                dic_prev[seed] = seed + range1[0] - range1[1]
                
                if seed in aux_list: aux_list.remove(seed)
    
    aux = {seed:seed for seed in aux_list}
    dic_prev.update(aux)

    return dic_prev, index_input + index_convert + 2

def convert_seeds(lines_to_convert: list, index_input: int, seeds: list):
    dic = []
    
    for index_convert, line in enumerate(lines_to_convert):

        line = line.strip()
        print(index_convert)
        if not line:
            break
        
        range1 = [int(i) for i in line.split(None)]
        print(range1)
        for seed in seeds:
            if seed[0] >= range1[1] and seed[1] <= range1[1]+range1[2]-1:
                dif1 = seed[0]-range1[1]
                dif2 = (range1[1]+range1[2]-1) - seed[1]
                dic.append([range1[0]+dif1, (range1[0]+range1[2]-1)-dif2])
            elif seed[0] < range1[1] and seed[1] <= range1[1]+range1[2]-1:
                dif2 = (range1[1]+range1[2]-1) - seed[1]
                dic.append([range1[0],(range1[0]+range1[2]-1)-dif2])
            elif seed[0] >= range1[1] and seed[1] > range1[1]+range1[2]-1:
                dif1 = seed[0]-range1[1] 
                dic.append([range1[0]+dif1, range1[1]+range1[2]-1])
        print(dic)
    return dic, index_input + 2

if __name__ == "__main__":
    with open("input.txt", "r") as fileInput:
        fileInput = fileInput.readlines()

        #Part 1:
        seeds = list(map(int, fileInput[0].split(":")[1].split(None)))

        print(seeds)

        index = 3

        #seedToSoil, index = convert_range(
	#    fileInput[index:], index, seeds)
#        print(seedToSoil)
#        soilToFertilizer, index = convert_range(
#            fileInput[index:], index, list(seedToSoil.values()))
#
#        fertilizerToWater, index = convert_range(
#            fileInput[index:], index, list(soilToFertilizer.values()))
#
#        waterToLight, index = convert_range(
#            fileInput[index:], index, list(fertilizerToWater.values()))
#
#        lightToTemperature, index = convert_range(
#            fileInput[index:], index, list(waterToLight.values()))
#
#        temperatureToHumidity, index = convert_range(
#            fileInput[index:], index, list(lightToTemperature.values()))
#
#        humidityToLocation, index = convert_range(
#           fileInput[index:], index, list(temperatureToHumidity.values()))
#        
#        print(min(humidityToLocation.values()))

        #Part 2:

        range_seeds = [[seeds[i],seeds[i]+seeds[i+1]-1] for i in range(0,len(seeds),2)]
        print(range_seeds)
        seedToSoil, index = convert_seeds(fileInput[index:], 3, range_seeds)
        print(seedToSoil)

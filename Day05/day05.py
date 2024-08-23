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

def convert_seeds(lines_to_convert: list, seeds: list):
    dic = []
    
    while seeds:

        seed = seeds.pop(0)

        for location in lines_to_convert.split('\n')[1:]:
            l, r1, r2 = map(int, location.split(None))
            diff = l - r1
            
            if seed[1] <= r1 or seed[0] >= r1+r2:
                continue
            if seed[0] < r1:
                dic.append([seed[0], r1])
                seed[0] = r1
            if seed[1] > r1+r2:
                dic.append([r1+r2, seed[1]])
                seed[1] = r1+r2
            dic.append([seed[0]+diff, seed[1]+diff])
            break
        else:
            dic.append([seed[0], seed[1]])
            
   
    return dic
    
if __name__ == "__main__":
    with open("input.txt", "r") as f:
        fileInput = f.read()

        lines = fileInput.split('\n\n')

        #Part 1:
        seeds = list(map(int, lines[0].split(":")[1].split(None)))

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
        seedsToSoil = convert_seeds(lines[1], range_seeds)
        print(seedsToSoil)
        soilToFertilizer = convert_seeds(lines[2], seedsToSoil)
        print(soilToFertilizer)
        fertilizerToWater = convert_seeds(lines[3], soilToFertilizer)
        print(fertilizerToWater)
        waterToLight = convert_seeds(lines[4], fertilizerToWater)
        print(waterToLight)
        lightToTemperature = convert_seeds(lines[5], waterToLight)
        print(lightToTemperature)
        temperatureToHumidity = convert_seeds(lines[6], lightToTemperature)
        print(temperatureToHumidity)
        humidityToLocation = convert_seeds(lines[7], temperatureToHumidity)
        print(humidityToLocation)

        minimum = float('inf')
        for x in humidityToLocation:
            minimum = min(x[0], minimum)

        print(minimum)

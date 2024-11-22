import math
if __name__ == "__main__":
    with open("test.txt", "r", encoding="utf-8") as f:
        fileInput = f.read()

        lines = fileInput.split('\n')
        times = list(map(int, lines[0].split(":")[1].split(None)))
        distances = list(map(int, lines[1].split(":")[1].split(None)))
        solutions = [0] * len(times)

        for i, _ in enumerate(times):
            for j in range(times[i]):
                distance_remaining = (times[i] - j) * j

                if distance_remaining > distances[i]:
                    # print(f'Time: {j}\n Distance: {distance_remaining}')
                    solutions[i] += 1

        print(math.prod(solutions))

        time = int(lines[0].split(":")[1].replace(" ", ""))
        distance = int(lines[1].split(":")[1].replace(" ", ""))
        time_break = 0

        for i in range(time):
            time_break = i
            if (time - i) * i > distance:
                break

        result = (time - 2 * time_break) + 1
        print(result)

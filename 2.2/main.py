import fileinput

def processInput(input_file):
    lines = []
    with(input_file) as f:
        for line in f:
            lines.append(line)
    return lines

def getInput(path:str):
    return fileinput.input(files=path, encoding="utf-8")

def getOutput(lines:list[str])->int:
    ribbonAmount = 0

    for line in lines:
        nums = line.split('x')
        dimensions = [int(nums[0]), int(nums[1]), int(nums[2])]
        totalVolume = dimensions[0] * dimensions[1] * dimensions[2]

        sortedDimensions = sorted(dimensions)
        smallest = sortedDimensions[0]
        secondSmallest = sortedDimensions[1]
        
        ribbonAmount += (smallest * 2 + secondSmallest *2) + totalVolume

    return ribbonAmount

def main():
    text = getInput("./input.txt")
    lines = processInput(text)
    print(getOutput(lines))

if __name__ == "__main__":
    main()

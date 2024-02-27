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
    totalSurfaceArea = 0

    for line in lines:
        nums = line.split('x')
        dimensions = [int(nums[0]), int(nums[1]), int(nums[2])]
        wrappingSides = [
            dimensions[0]*dimensions[1], #x 
            dimensions[1]*dimensions[2], #y
            dimensions[2]*dimensions[0]  #z
        ]
        smallest = min(wrappingSides)
        
        totalSurfaceArea += 2*wrappingSides[0] + 2*wrappingSides[1] + 2*wrappingSides[2] + smallest

    return totalSurfaceArea

def main():
    text = getInput("./input.txt")
    lines = processInput(text)
    print(getOutput(lines))

if __name__ == "__main__":
    main()

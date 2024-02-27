import fileinput

def processInput(input_file):
    lines = []
    with(input_file) as f:
        for line in f:
            lines.append(line)
    return lines

def getOutput(lines:list[str])->str:
    line = lines[0]
    floor = 0 
    pos = 1

    for c in line:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1

        if floor == -1:
            return pos

        pos += 1

    return floor

def getInput(path:str):
    return fileinput.input(files=path, encoding="utf-8")

def main():
    text = getInput("./input.txt")
    lines = processInput(text)
    print(getOutput(lines))

if __name__ == "__main__":
    main()

def readLine(lineNO):
    with open("qno6.txt") as f:
        lines = f.readlines()
        if lineNO >= len(lines):
            raise ValueError("Line number exceeded in file")
        return lines[lineNO-1].strip()
            
try:
    line = int(input("Enter the line to read text = "))
    ans = readLine(line)
    print(ans)
except ValueError as e:
    print(f"Error: {e}")

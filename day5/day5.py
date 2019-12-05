import fileinput
import time

lines = [int(line) for line in list(fileinput.input())[0].split(',')]

def execute(data, arg) -> int :
    def mread(pointer : int, immediateMode : bool) -> int : #read from memory
        return data[pointer] if immediateMode else data[data[pointer]]

    def mwrite(pointer : int, value : int) -> None : #write to memory
        data[data[pointer]] = value

    def getDigit(number, index) -> int : #get digit from number starting from right, return 0 if invalid index
        strNumber = str(number)
        return int(strNumber[-index - 1]) if index < len(strNumber) else 0
        
    pointer, output = 0, 0
    while True:
        op, val1, val2 = data[pointer], 0, 0 #init
        mode1 = getDigit(op, 2) #get readmode for param1
        mode2 = getDigit(op, 3) #get readmode for param2
        op = int(str(op)[-2:]) #get op from instruction
        if op == 99 : 
            break
        if not op == 3 and not op == 4 : #if its not a input or output op read values from memory
            val1 = mread(pointer + 1, mode1)
            val2 = mread(pointer + 2, mode2)
        if op == 1 :
            mwrite(pointer + 3, val1 + val2)
            pointer += 4
        elif op == 2 :
            mwrite(pointer + 3, val1 * val2)
            pointer += 4
        elif op == 3 :
            mwrite(pointer + 1, arg)
            pointer += 2
        elif op == 4 :
            output = mread(pointer + 1, False)
            pointer += 2
        elif op == 5 :
            pointer = val2 if val1 != 0 else pointer + 3
        elif op == 6 :
            pointer = val2 if val1 == 0 else pointer + 3
        elif op == 7 :
            mwrite(pointer + 3, 1 if val1 < val2 else 0)
            pointer += 4
        elif op == 8 :
            mwrite(pointer + 3, 1 if val1 == val2 else 0)
            pointer += 4
    return output

def executeWithInput() : 
    return execute(lines.copy(), int(input("Input > ")))

def part1() -> int : 
    return execute(lines.copy(), 1)

def part2() -> int : 
    return execute(lines.copy(), 5)
    
print(f"Part 1 result is {part1()}")
print(f"Part 2 result is {part2()}")

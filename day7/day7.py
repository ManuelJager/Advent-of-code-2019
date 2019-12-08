import fileinput
import time

lines = list(map(int, list(fileinput.input())[0].split(',')))

class Machine :
    pointer : int
    data : list
    args : list
    argCounter : int

    def __init__(self, data) :
        self.pointer = 0
        self.data = data
        self.args = []
        self.argCounter = 0

    def mread(self, offset : int, immediateMode : bool) -> int : #read from memory
        return self.data[self.pointer + offset] if immediateMode else self.data[self.data[self.pointer + offset]]

    def mwrite(self, pointer : int, value : int) -> None : #write to memory
        self.data[self.data[pointer]] = value

    def getDigit(self, number, index) -> int : #get digit from number starting from right, return 0 if invalid index
        strNumber = str(number)
        return int(strNumber[-index - 1]) if index < len(strNumber) else 0

    def runUntilFoundOutput(self) :
        while True:
            op, val1, val2 = self.data[self.pointer], 0, 0 #init
            mode1 = self.getDigit(op, 2) #get readmode for param1
            mode2 = self.getDigit(op, 3) #get readmode for param2
            op = int(str(op)[-2:]) #get op from instruction
            if op == 99 : 
                break
            if not op == 3 and not op == 4 : #if its not a input or output op read values from memory
                val1 = self.mread(1, mode1)
                val2 = self.mread(2, mode2)
            if op == 1 :
                self.mwrite(3, val1 + val2)
                self.pointer += 4
            elif op == 2 :
                self.mwrite(3, val1 * val2)
                self.pointer += 4
            elif op == 3 :
                self.mwrite(1, self.args[self.argCounter])
                self.argCounter += 1
                self.pointer += 2
            elif op == 4 :
                output = self.mread(1, False)
                self.pointer += 2
                print(output)
                return output
            elif op == 5 :
                self.pointer = val2 if val1 != 0 else self.pointer + 3
            elif op == 6 :
                self.pointer = val2 if val1 == 0 else self.pointer + 3
            elif op == 7 :
                self.mwrite(3, 1 if val1 < val2 else 0)
                self.pointer += 4
            elif op == 8 :
                self.mwrite(3, 1 if val1 == val2 else 0)
                self.pointer += 4
        return output


def execute_sequence(sequence: list):
    inputSignal = 0
    for phaseSetting in sequence :
        inputSignal = execute(lines.copy(), [phaseSetting, inputSignal])
    return inputSignal

def executeSequenceWithMemMap(sequence : list, startVal = 0) :
    inputSignal = startVal
    for phaseSetting in sequence :
        inputSignal = execute(lines.copy(), [phaseSetting, inputSignal])
    return inputSignal

def getUniqueSequences(seqSet, seqLength): 
    sequences = []
    def appendToSequence(seqSet, prefix, seqSetLength, remainingSeqLength): 
        if (remainingSeqLength == 0) : 
            sequences.append(prefix)
            return

        for i in range(seqSetLength): 
            char = seqSet[i]
            if char in prefix :
                continue
            newPrefix = prefix + char
            appendToSequence(seqSet, newPrefix, seqSetLength, remainingSeqLength - 1) 
    
    appendToSequence(seqSet, "", len(seqSet), seqLength) 
    return sequences

def part1() -> int : 
    #sequences = [list(map(int, list(seq))) for seq in getUniqueSequences(list(map(str,range(5,10))), 5)]
    #return max([executeSequence(seq) for seq in sequences])
    return 0

def part2() -> int :
    machines = [Machine(lines.copy()) for i in range(5)]
    for i, machine in enumerate(machines) :
        machine.args.append(i + 5)

    inputSignal = 5
    for machine in machines :
        machine.args.append(inputSignal)
        inputSignal = machine.runUntilFoundOutput()

    return inputSignal
    
    #sequences = [list(map(int, list(seq))) for seq in getUniqueSequences(list(map(str,range(5,10))), 5)]
    #return max([executeSequenceWithMemMap(seq, memMap) for seq in sequences])
    
print(f"Part 1 result is {part1()}")
print(f"Part 2 result is {part2()}")
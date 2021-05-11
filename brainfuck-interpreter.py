import numpy as np
import time

def execute_brainfuck(program: str):

    programpointer = 0  # The index of the current instruction

    data = np.full(100000000,0)
    datapointer = 0  # The number of the cell that is currently pointed to

    print("Now executing...\n\n")

    while(programpointer < len(program)):  # until the program ends, run its code
        currentInstruction = program[programpointer]
        if (currentInstruction == ">"):  # Move right
            datapointer = datapointer + 1
            programpointer += 1

        elif (currentInstruction == "<"):  # Move left
            datapointer -= 1
            programpointer += 1

        elif (currentInstruction == "+"):  # Increment
            data[datapointer] += 1
            programpointer += 1

        elif (currentInstruction == "-"):  # Decrement
            data[datapointer] -= 1
            programpointer += 1

        elif (currentInstruction == "."):  # Write
            print(chr(data[datapointer]),end="")
            programpointer += 1

        elif (currentInstruction == ","):  # Read
            userinput = input()
            if (userinput == ""):  # If no input is read, enter was inputted
                userinput = "\n"
            data[datapointer] = ord(userinput[0])
            programpointer += 1

        data[datapointer] %= 256  # Correct value to between 0 and 255

        if (currentInstruction == "["):  # Loops
            if(data[datapointer] == 0):
                # Now, find the next ] and jump to the command after it
                while (program[programpointer] != "]"):
                    programpointer += 1
                programpointer += 1
            else:
                # Just continue execution without jumping
                programpointer += 1

        elif (currentInstruction == "]"):
            if(data[datapointer] != 0):
                # Now find the last [ and jump to the command after it
                while(program[programpointer] != "["):
                    programpointer -= 1
                programpointer += 1
            else:
                # Just continue execution without jumping
                programpointer += 1

        if(currentInstruction not in "+-<>[].,"):
            print("Unknown Instruction:")
            print((currentInstruction+"Unicode"+ord(currentInstruction)))
            print("Stopping execution.")
            break

print("Please input your Brainfuck program:")

line = input()
program = ""
while(line != ""):
    program+=line
    line=input()

execute_brainfuck(program)

time.sleep(5)

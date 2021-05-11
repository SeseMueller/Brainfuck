import time #imports time to be able to sleep
import os

inputfile = "./mandelbrot.txt"

file = open(inputfile, "r")

content = file.read()

file.close()

output = "#include <stdio.h>\n#include <windows.h>\n\nvoid main(){\nchar array[100000]={0};\nchar *ptr = &array[0];\n"

while (len(content) != 0):
    currentInstruction = content[0]

    #Translation to C: see https://en.wikipedia.org/wiki/Brainfuck
    if(currentInstruction==">"):
        output+="++ptr;\n"
    elif(currentInstruction=="<"):
        output+="--ptr;\n"
    elif(currentInstruction=="+"):
        output+="++*ptr;\n"
    elif(currentInstruction=="-"):
        output+="--*ptr;\n"
    elif(currentInstruction=="."):
        output+="putchar(*ptr);\n"
    elif(currentInstruction==","):
        output+="scanf(\" %c\",ptr);\n"
    elif(currentInstruction=="["):
        output+="while(*ptr){\n"
    elif(currentInstruction=="]"):
        output+="}\n"
    elif(currentInstruction=="\n"):
        pass #skip the char if it is a newline
    else:
        print("The instruction: ",currentInstruction," is not supported, it was skipped.")
    content = content[1:] #Deletes the first symbol

output+="\nSleep(5000);\n\nreturn;\n}" #Adds the closing bracket of main

outfile = open("brainfuck.c","w")
outfile.write(output)
outfile.close()

time.sleep(1)

os.system("gcc -o result.exe brainfuck.c")


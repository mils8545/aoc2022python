import easygui
import time
import math


AOCDAY = "06"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    text = lines[0]
    for i in range(3,len(text)): # 3, 4, 5, 6, 7......
        dup = False
        for j in range(3): # 0, 1, 2
            for k in range(1, 4 - j): # 1, 2, 3
                if text[i+j] == text[i+j+k]:
                    dup = True
        if not dup:
            return (f"The first packet is at index {str(i + 4)}.")

    return(f"NOT FOUND") 

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    
    text = lines[0]
    for i in range(13,len(text)):
        dup = False
        for j in range(13):
            for k in range(1, 14 - j):
                if text[i+j] == text[i+j+k]:
                    dup = True
        if not dup:
            return (f"The first packet is at index {str(i + 14)}.")

    return(f"NOT FOUND") 

def main ():
    # Opens a dialog to select the input file
    # Times and runs both solutions
    # Prints the results
    fileName = easygui.fileopenbox(default=f"./"+AOCDAY+"/"+"*.txt")
    if fileName == None:
        print("ERROR: No file selected.")
        return
    lines = readFile(fileName)
    p1StartTime = time.perf_counter()
    p1Result = part1(lines)
    p1EndTime = time.perf_counter()
    p2StartTime = time.perf_counter()
    p2Result = part2(lines)
    p2EndTime = time.perf_counter()
    print("Advent of Code 2019 Day " + AOCDAY + ":")
    print("  Part 1 Execution Time: " + str(round((p1EndTime - p1StartTime)*1000,3)) + " milliseconds")
    print("  Part 1 Result: " + str(p1Result))
    print("  Part 2 Execution Time: " + str(round((p2EndTime - p2StartTime)*1000,3)) + " milliseconds")
    print("  Part 2 Result: " + str(p2Result))

main()
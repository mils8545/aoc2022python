import easygui
import time
import math


AOCDAY = "04"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines


def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    pairs = []

    for line in lines:
        pair = []
        pair.append(int(line.split(",")[0].split("-")[0]))
        pair.append(int(line.split(",")[0].split("-")[1]))
        pair.append(int(line.split(",")[1].split("-")[0]))
        pair.append(int(line.split(",")[1].split("-")[1]))
        pairs.append(pair)
    
    count = 0
    for pair in pairs:
        if pair[0] <= pair[2] and pair[1] >= pair[3]:
            count += 1
        elif pair[2] <= pair[0] and pair[3] >= pair[1]:
            count += 1

    return(f"There are {count} pairs that overlap fully.") 

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    pairs = []

    for line in lines:
        pair = []
        pair.append(int(line.split(",")[0].split("-")[0]))
        pair.append(int(line.split(",")[0].split("-")[1]))
        pair.append(int(line.split(",")[1].split("-")[0]))
        pair.append(int(line.split(",")[1].split("-")[1]))
        pairs.append(pair)
    
    count = 0
    for pair in pairs:
        if (pair[0] >= pair[2] and pair[0] <= pair[3]) or (pair[1] >= pair[2] and pair[0] <= pair[3]):
            count += 1
        elif (pair[2] >= pair[0] and pair[2] <= pair[1]) or (pair[3] >= pair[0] and pair[3] <= pair[1]):
            count += 1

    return(f"There are {count} pairs that overlap at least partially.") 

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
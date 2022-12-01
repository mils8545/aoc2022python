import easygui
import time
import math

AOCDAY = "01"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines



def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    total = 0
    cals = []
    for line in lines:
        if line != "":
            total += int(line)
        else:
            cals.append(total)
            total = 0
    cals.sort()

    return(f"The elf with the most calories has {cals[-1]} calories in his bag.") 

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    
    # Code the solution to part 1 here, returning the answer as a string
    total = 0
    cals = []
    for line in lines:
        if line != "":
            total += int(line)
        else:
            cals.append(total)
            total = 0
    cals.sort()
    top_three = cals[-1]+cals[-2]+cals[-3]

    return(f"The three elves with the most calories have {top_three} calories in their bags.") 

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
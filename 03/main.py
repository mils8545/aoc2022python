import easygui
import time
import math

AOCDAY = "03"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def compare(bag1, bag2):
    for x in bag1:
        for y in bag2:
            if x == y:
                return x
    return []

def compare3way(bag1, bag2, bag3):
    for x in bag1:
        for y in bag2:
            if x == y:
                for z in bag3:
                    if x == z:
                        return x
    return []


def value(chr):
    if ord(chr) >= 97:
        return ord(chr) - 96
    else:
        return ord(chr) - 64 + 26

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    score = 0
    matches = []
    for line in lines:
        matches += compare(line[:len(line)//2],line[len(line)//2:])
        print(line[:len(line)//2+1],line[len(line)//2+1:])

    for match in matches:
        score += value(match)
    return(f"The total score at the end is {score}.") 

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string

    score = 0
    matches = []
    for i in range(0, len(lines), 3):
        matches += compare3way(lines[i], lines[i+1], lines[i+2])
    for match in matches:
        score += value(match)
    return(f"The total score at the end is {score}.") 

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
import easygui
import time
import math

AOCDAY = "02"

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
    scores = {"X": 1, "Y": 2, "Z": 3}
    beats = {"X": "C", "Y": "A", "Z": "B"}
    loses = {"X": "B", "Y": "C", "Z": "A"}
    for line in lines:
        pairs.append(line.split(" "))
    score = 0
    for pair in pairs:
        score += scores[pair[1]]
        if beats[pair[1]] == pair[0]:
            score += 6
        elif loses[pair[1]] == pair[0]:
            score += 0
        else:
            score += 3 

    return(f"The total score at the end is {score}.") 

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    
    pairs = []
    scores = {"X": 1, "Y": 2, "Z": 3}

    beats = {"C": "X", "A": "Y", "B": "Z"}
    loses = {"B": "X", "C": "Y", "A": "Z"}
    ties = {"A": "X", "B": "Y", "C": "Z"}

    for line in lines:
        pairs.append(line.split(" "))
    score = 0
    for pair in pairs:
        if pair[1] == "X":
            choice = loses[pair[0]]
        elif pair[1] == "Y":
            choice = ties[pair[0]]
            score += 3
        else:
            choice = beats[pair[0]]
            score += 6
        score += scores[choice]

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
    print("Advent of Code 2022 Day " + AOCDAY + ":")
    print("  Part 1 Execution Time: " + str(round((p1EndTime - p1StartTime)*1000,3)) + " milliseconds")
    print("  Part 1 Result: " + str(p1Result))
    print("  Part 2 Execution Time: " + str(round((p2EndTime - p2StartTime)*1000,3)) + " milliseconds")
    print("  Part 2 Result: " + str(p2Result))

main()
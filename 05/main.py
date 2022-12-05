import easygui
import time
import math

AOCDAY = "05"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parse_lines(lines):
    index_line = 0
    for i, line in enumerate(lines):
        if line.split(" ")[1] == "1":
            index_line = i
            break;
    container_count = int(lines[index_line].split(" ")[-1])

    containers = []
    for i in range(container_count):
        containers.append([])

    for i in range(index_line - 1, -1, -1):
        for j in range(container_count):
            if lines[i][j*4+1] != " ":
                containers[j].append(lines[i][j*4+1])

    moves = []

    for line in lines[index_line+2:]:
        moves.append([int(line.split(" ")[1]), int(line.split(" ")[3]), int(line.split(" ")[5])])

    return containers, moves


def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    containers, moves = parse_lines(lines)

    for move in moves:
        for i in range(move[0]):
            if len(containers[move[1]-1]) == 0:
                break
            else:
                containers[move[2]-1].append(containers[move[1]-1].pop(-1))
    
    result = ""
    for stack in containers:
        result += stack[-1]

    return(f"The top containers are {result}.") 

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    containers, moves = parse_lines(lines)

    for move in moves:
        bottom_of_move = max(0, len(containers[move[1]-1]) - move[0])
        while (len(containers[move[1]-1]) > bottom_of_move):
            containers[move[2]-1].append(containers[move[1]-1].pop(bottom_of_move))
    
    result = ""
    for stack in containers:
        result += stack[-1]

    return(f"The top containers are {result}.") 

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
import easygui
import time
import math

AOCDAY = "07"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def dir_size(dir, dir_list):
    total = 0
    for entry in dir.keys():
        if type(dir[entry]) == int:
            total += dir[entry]
        elif entry != "..":
            sub_size, dir_list = dir_size(dir[entry], dir_list)
            total += sub_size
            dir_list.append(sub_size)
    return total, dir_list

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string

    dirs = {}
    current = dirs
    i = 0
    while i < len(lines):
        line = lines[i]
        if line[2:4] == "cd":
            if line[5] == "/":
                current = dirs
            else:
                current = current[line[5:]]
        else:
            while i + 1 < len(lines) and lines[i+1][0] != "$":
                i += 1
                line = lines[i]
                if line[0:3] == "dir":
                    current[line[4:]] = {"..": current}
                else:
                    current[line.split(" ")[1]] = int(line.split(" ")[0])
        i += 1

    total_size, dir_list = dir_size(dirs, [])
    dir_list.append(total_size)

    under_size = 0
    for dir in dir_list:
        if dir <= 100000:
            under_size += dir
    return(f"The total size of all folders under 100000 is {under_size}.") 

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    
    dirs = {}
    current = dirs
    i = 0
    while i < len(lines):
        line = lines[i]
        if line[2:4] == "cd":
            if line[5] == "/":
                current = dirs
            else:
                current = current[line[5:]]
        else:
            while i + 1 < len(lines) and lines[i+1][0] != "$":
                i += 1
                line = lines[i]
                if line[0:3] == "dir":
                    current[line[4:]] = {"..": current}
                else:
                    current[line.split(" ")[1]] = int(line.split(" ")[0])
        i += 1

    total_size, dir_list = dir_size(dirs, [])

    dir_list.sort()

    target_size = 30000000 - (70000000 - total_size)

    for dir in dir_list:
        if dir > target_size:
            return (f"The smallest folder that can be deleted is {dir} in size.")

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
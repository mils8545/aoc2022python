import easygui
import time
import math


AOCDAY = "08"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    seen_trees = []
    for y in range(len(lines)):
        highest_left = -1
        highest_right = -1
        for x in range(len(lines[0])):
            if int(lines[y][x]) > highest_left:
                highest_left = int(lines[y][x])
                tree = f"{x},{y}"
                if tree not in seen_trees:
                    seen_trees.append(tree)
        for x in range(len(lines[0])-1, -1, -1):
            if int(lines[y][x]) > highest_right:
                highest_right = int(lines[y][x])
                tree = f"{x},{y}"
                if tree not in seen_trees:
                    seen_trees.append(tree)
    for x in range(len(lines[0])):
        highest_left = -1
        highest_right = -1
        for y in range(len(lines)):
            if int(lines[y][x]) > highest_left:
                highest_left = int(lines[y][x])
                tree = f"{x},{y}"
                if tree not in seen_trees:
                    seen_trees.append(tree)
        for y in range(len(lines)-1, -1, -1):
            if int(lines[y][x]) > highest_right:
                highest_right = int(lines[y][x])
                tree = f"{x},{y}"
                if tree not in seen_trees:
                    seen_trees.append(tree)

    return(f"There are {len(seen_trees)} visible from the edge of the forest.") 

def tree_view(x, y, lines):
    height = int(lines[y][x])
    tree_score = 1
    tree_count = 0
    for new_x in range(x+1, len(lines[0])):
        if int(lines[y][new_x]) < height:
            tree_count += 1
        else:
            tree_count += 1
            break
    tree_score *= tree_count
    tree_count = 0
    for new_x in range(x-1, -1, -1):
        if int(lines[y][new_x]) < height:
            tree_count += 1
        else:
            tree_count += 1
            break
    tree_score *= tree_count
    tree_count = 0
    for new_y in range(y+1, len(lines)):
        if int(lines[new_y][x]) < height:
            tree_count += 1
        else:
            tree_count += 1
            break
    tree_score *= tree_count
    tree_count = 0
    for new_y in range(y-1, -1, -1):
        if int(lines[new_y][x]) < height:
            tree_count += 1
        else:
            tree_count += 1
            break
    tree_score *= tree_count
    return tree_score

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    highest_score = 0
    for y in range(len(lines)):
        for x in range(len(lines)):
            highest_score = max(highest_score, tree_view(x, y, lines))
    return(f"The score of the best placed spot is {highest_score}.")

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
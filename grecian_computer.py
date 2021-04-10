#!/usr/bin/python3

import pprint

#This program models the "True Genius Grecian Computer" puzzle. It 
#has five wheels which can be rotated independently stacked on top
#of each other, with higher wheels being smaller in size and 
#having holes in some positions. Each wheel has 12 numbers around
#1-4 rows, so in any given position the computer has 12 columns of
#4 numbers, and depending on where the holes are the numbers can be
#on different layers of disks. See the picture included in the files.
#The goal of the puzzle is to position the disks so that the numbers
#in each of the 12 columns adds to 42.

#Use a brute force algorithm to solve this. There are 12 positions on
#the wheel, and 5 wheels which can move independently, (but for 
#simplicity's sake we can consider the outermost wheel to be fixed,
#or else we will have 12 identical solutions which are related to
#each other by a rotation of the entire puzzle) so there's only 12**4
# = 20736 possible combinations. We will simply walk through all 
#permutations.

#In the below matrix representing the computer, each double list 
#contains a disk, with numbers arranged appropriately (numbers on
#the same disk obviously cannot move relative to each other). Each
#disk can be shifted left or right, which would correspond to a 
#rotation on the physical puzzle. 

original_computer = [[[ 2, 5,10, 7,16, 8, 7, 8, 8, 3, 4,12],
                      [ 3, 3,14,14,21,21, 9, 9, 4, 4, 6, 6],
                      [ 8, 9,10,11,12,13,14,15, 4, 5, 6, 7],
                      [14,11,14,14,11,14,11,14,11,11,14,11]],
                     [[ 1,-1, 9,-1,12,-1, 6,-1,10,-1,10,-1],
                      [ 3,26, 6,-1, 2,13, 9,-1,17,19, 3,12],
                      [ 9,20,12, 3, 6,-1,14,12, 3, 8, 9,-1],
                      [ 7,-1, 9,-1, 7,14,11,-1, 8,-1,16, 2]],
                     [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                      [ 5,-1,10,-1, 8,-1,22,-1,16,-1, 9,-1],
                      [21, 6,15, 4, 9,18,11,26,14, 1,12,-1],
                      [ 9,13, 9, 7,13,21,17, 4, 5,-1, 7, 8]],
                     [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                      [ 4,-1, 7,15,-1,-1,14,-1, 9,-1,12,-1],
                      [ 7, 3,-1, 6,-1,11,11, 6,11,-1, 6,17]],
                     [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                      [ 3,-1, 6,-1,10,-1, 7,-1,15,-1, 8,-1]]]

#todo: change the hardcoded values (4, 5, 11, 12, 42) to use arguments or len() something from the input

def get_computer_value(computer, row, column):
    for disk_counter in [4,3,2,1,0]:
        if computer[disk_counter][row][column] != -1:
            return computer[disk_counter][row][column]

def check_correctness(computer):
    for c in range(0,12):
        column_sum = 0
        for r in range(0,4):
            column_sum += get_computer_value(computer, r, c)
        if column_sum != 42:
            return False
    return True

#arguments: computer to shift (does not modify), 
#           array containing shifts to each disk of the computer
def computer_shift(computer,
                   disk_offsets):
    retval = [[[None for _ in range(12)] for _ in range(4)] for _ in range(5)]
    for disk in range(0,5):
        for r in range(0,4):
            retval[disk][r] = rotate_1d_array(computer[disk][r], disk_offsets[disk])
    return retval

def rotate_1d_array(arr, rotation):
    retval = [None] * len(arr)
    for i in range(0, len(arr)):
        retval[i] = arr[(i + rotation) % len(arr)]
    return retval

if __name__ == "__main__":
    #Need permutations on a 2d array in a smarty pants pythonic way.
    #some smarter way to do 0,0,0,0 0,0,0,1 ... 11,11,11,11
    for i in range(0,12**4):
        computer = computer_shift(original_computer, [0, i//(12**3)%12, i//(12**2)%12, i//(12)%12, i%12])
        if check_correctness(computer):
            pprint.pprint(computer)
            print("offsets: " + str([0, i//(12**3)%12, i//(12**2)%12, i//(12)%12, i%12]))

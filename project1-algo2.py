#!/usr/bin/python
# Patrick Kwong
# CS325 Analysis of Algorithms - Project 1 Group 31
# Algorithm 2: Better Enumeration
# October 10, 2016

# O(n^2) Better Enumeration - iteration for max subarray.
# Source: Based on Prof. Borradaile's Designing Poly-Time Algorithms lecture

import time

def Algorithm2(array):
<<<<<<< HEAD
		maxSum = float("-inf")
		maxArrayIndexLow = 0
		maxArrayIndexHigh = 0

		for i in range(0, len(array)):
			thisSum = 0
			for j in range(i, len(array)):
				thisSum = thisSum + array[j]
				
				if (thisSum > maxSum):
					maxSum = thisSum
					maxArrayIndexLow = i
					maxArrayIndexHigh = j

		maxArray = []
		maxArray = array[maxArrayIndexLow:maxArrayIndexHigh + 1]
		print array
		print maxArray
		print maxSum
=======
    maxSum = 0
    maxArrayIndexLow = 0
    maxArrayIndexHigh = 0

    for i in range(0, len(array)):
        thisSum = 0
        for j in range(i, len(array)):
            thisSum = thisSum + array[j]

            if (thisSum > maxSum):
                maxSum = thisSum
                maxArrayIndexLow = i
                maxArrayIndexHigh = j

    maxArray = []
    maxArray = array[maxArrayIndexLow:maxArrayIndexHigh+1]
    print array
    print maxArray
    print maxSum
>>>>>>> e0cfaf7c1f02ac0f843ad288627a762e23c869c0


#Here is the "main" function so far it just reads every line from a file and sends it to algorithm
with open('MSS_TestProblems.txt','r') as f:
    #parse each line in test file and store in array to send to the different functions

    num = 0
    for line in f:
        line = line.replace("[","")
        line = line.replace("]","")
        line = line.replace(" ","")
        array = [int(x) for x in line.split(',') if x not in '\n']

        cur_time = time.clock()
        Algorithm2(array) #call algorithm on each line in test file
        elapsed_time = time.clock() - cur_time
        print str(num) + ", " + str(round(elapsed_time, 7))
        num += 1

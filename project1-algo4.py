#!/usr/bin/python
# Patrick Kwong
# CS325 Analysis of Algorithms - Project 1 Group 31
# Algorithm 4: Linear-time
# October 14, 2016

# O(n) Linear-time - iteration for max subarray.
# Source: Based on Prof. Borradaile's Designing Poly-Time Algorithms lecture and the provided Algorithm 4 Pseudocode.pdf
def Algorithm4(array):
	n = len(array)
	maxSum = -10000
	endingHereSum = -10000

	for i in range(0, n):
		endingHereHigh= i

		if endingHereSum > 0:
			endingHereSum = endingHereSum + array[i]

		else:
			endingHereLow = i
			endingHereSum = array[i]

		if endingHereSum > maxSum:
			maxSum = endingHereSum
			maxArrayIndexLow = endingHereLow
			maxArrayIndexHigh = endingHereHigh

	maxArray = []
	maxArray = array[maxArrayIndexLow:maxArrayIndexHigh+1]
	print array
	print maxArray
	print maxSum


#Here is the "main" function so far it just reads every line from a file and sends it to algorithm
with open('MSS_TestProblems.txt','r') as f:
	#parse each line in test file and store in array to send to the different functions

	for line in f:
			line = line.replace("[","")
			line = line.replace("]","")
			line = line.replace(" ","")
			array = [int(x) for x in line.split(',') if x not in '\n']

			Algorithm4(array) #call algorithm on each line in test file
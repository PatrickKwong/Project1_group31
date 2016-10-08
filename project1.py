#!/usr/bin/python
#Cas Donoghue
#Project1 CS325 Analysis of Algorithms
#08OCT2016


#O(n^3) brute force solution for maximum sub array problem. takes an array to find max sub array of
def Algorithm1(array):
		maxSum = -10000  #initialize max sum to some arbitrarily low number
		maxArrayIndexLow = -1 #initialize to unreal index
		maxArrayIndexHigh = -1 #initialize to unreal index

		#This is the main logic. Basically the nested loops will find a sum for every.
		#The maximum value and the indices of the corresponding array will be saved. 
		for i in range(0,len(array)):
			for j in range(i,len(array)):
				thisSum = 0
				for k in range(i,j):
					thisSum += array[k]
				if (thisSum >= maxSum):
					maxSum = thisSum
					maxArrayIndexLow = i
					maxArrayIndexHigh = j
		maxArray = []
		maxArray = array[maxArrayIndexLow:maxArrayIndexHigh]
		print array
		print maxArray
		print maxSum


#Here is the "main" function so far it just reads every line from a file and sends it to Algorithm1
with open('MSS_TestProblems.txt','r') as f:
	#parse each line in test file and store in array to send to the different functions
	for line in f:
			line = line.replace("[","")
			line = line.replace("]","")
			array = [int(x) for x in line.split(',')]

			Algorithm1(array) #call algorithm1 on each line in test file
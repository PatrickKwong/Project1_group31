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
			#print 'i is ' + str(i)  #stub for testing
			for j in range(i,len(array)):
				thisSum = 0
				#print 'j is ' + str(j)   # stub for testing
				for k in range(i,j + 1):
					#print 'range is ' + str(i) + ' ' + str(j) # stub for testing
					thisSum += array[k]
				if (thisSum >= maxSum):
					maxSum = thisSum
					maxArrayIndexLow = i
					maxArrayIndexHigh = j+1
		maxArray = []
		maxArray = array[maxArrayIndexLow:maxArrayIndexHigh]
		print array
		print maxArray
		print maxSum

#O(n^2) slightly better enumeration. Based off Patricks algorithm. 

def Algorithm2(array):
		maxSum = -10000  #initialize max sum to some arbitrarily low number
		maxArrayIndexLow = -1 #initialize to unreal index
		maxArrayIndexHigh = -1 #initialize to unreal index

		#This is the main logic. Basically the nested loops will find a sum for every.
		#The maximum value and the indices of the corresponding array will be saved. 
		for i in range(0,len(array)):
			thisSum = 0
			#print 'i is ' + str(i) #stub for testing
			for j in range(i,len(array)):
				thisSum += array[j]
				#print 'this sum: ' + str(thisSum)  #this was a stub for testing
				if (thisSum >= maxSum):
					maxSum = thisSum
					maxArrayIndexLow = i
					maxArrayIndexHigh = j+1
		maxArray = []
		maxArray = array[maxArrayIndexLow:maxArrayIndexHigh]
		print array
		print maxArray
		print maxSum

#Here is the "main" function so far it just reads every line from a file, stores those lines (arrays)
#as an array and then stores those in an array of arrays (so you only have to get file contents once. )

#declare and array to hold the arrays from file. 
arrayOfArrays = []
with open('MSS_TestProblems.txt','r') as f:
	#parse each line in test file and store in array to send to the different functions
	for line in f:
			line = line.replace("[","")
			line = line.replace("]","")
			array = [int(x) for x in line.split(',')]
			#store every array in an array of arrays
			arrayOfArrays.append(array)
			
#this test algorithm led me to discover the range error in the original algorithms proposed
# testArray = [-2,4,3,1]

# print "alg1"
# Algorithm1(testArray)
# print "alg2"

# Algorithm2(testArray)

print "Algorithm 1 results:"
for k in arrayOfArrays:
	Algorithm1(k)
print "Algorithm 2 results"
for k in arrayOfArrays:
	Algorithm2(k)
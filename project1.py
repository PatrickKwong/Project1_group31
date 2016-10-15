#!/usr/bin/python
#Cas Donoghue
#Project1 CS325 Analysis of Algorithms
#08OCT2016


#O(n^3) brute force solution for maximum sub array problem. takes an array to find the MSS of
# return value is an array with MSS indices of input array as well as sum of the sub sequence
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
		# set up the return array
		maxArray = []
		maxArray.append(maxArrayIndexLow)  #this is start index in input array of MSS
		maxArray.append(maxArrayIndexHigh) #this is end index in input array of MSS
		maxArray.append(maxSum) # this is the MSS sum
		return maxArray


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
				# set up the return array
		maxArray = []
		maxArray.append(maxArrayIndexLow)  #this is start index in input array of MSS
		maxArray.append(maxArrayIndexHigh) #this is end index in input array of MSS
		maxArray.append(maxSum) # this is the MSS sum
		return maxArray

#O(n*lg(n)) recursive algorithm. Based off mycodeschool https://gist.github.com/mycodeschool/8b4bcff69427c8a6f2aa implementation
def Algorithm3(array,leftIndex,rightIndex):
	#base case
	if(leftIndex == rightIndex):
		return array[rightIndex]

	midPoint = int((rightIndex + leftIndex)/2)  #casting to int is same thing as floor function

	leftMSS = Algorithm3(array,leftIndex,midPoint)
	rightMSS = Algorithm3(array,midPoint + 1, rightIndex)

	leftMax = -10000
	rightMax = -100000
	tempSum = 0

	for i in range(midPoint,leftIndex -1,-1):
		tempSum += array[i]
		leftMax = max(leftMax,tempSum)

	tempSum = 0
	for i in range(midPoint + 1,rightIndex + 1):
		tempSum += array[i]
		rightMax = max(rightMax,tempSum)

	ans = max(leftMSS,rightMSS)

	return max(ans,leftMax+rightMax)

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
			

print "Algorithm 1 results:"
for k in arrayOfArrays:
	alg1results = []
	alg1results = Algorithm1(k)
	print k
	print k[alg1results[0]:alg1results[1]]
	print 'Sum of MSS = ' + str(alg1results[2])

print "Algorithm 2 results"
for k in arrayOfArrays:
	alg2results = []
	alg2results = Algorithm2(k)
	print k
	print k[alg2results[0]:alg2results[1]]
	print 'Sum of MSS = ' + str(alg2results[2])

# print "algorithm 3 results"
# for k in arrayOfArrays:
# 	lastIndex = len(k) - 1
# 	result = Algorithm3(k,0,lastIndex)
# 	print result



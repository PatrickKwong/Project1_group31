#!/usr/bin/python
#Cas Donoghue
#Patrick Kwong
#Nicholas Vrontakis
#Group 31
#Project1 CS325 Analysis of Algorithms
#OCT 6 2016


#O(n^3) brute force solution for maximum sub array problem. takes an array to find the MSS of
# return value is an array with MSS indices of input array as well as sum of the sub sequence
def Algorithm1(array):
		maxSum = float("-inf")   #initialize max sum to some arbitrarily low number

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
					maxArrayIndexHigh = j
		# set up the return array
		maxArray = [maxArrayIndexLow,maxArrayIndexHigh,maxSum] #start index, end index, MSS sum
		return maxArray


#O(n^2) slightly better enumeration.
# Source: Based on Prof. Borradaile's Designing Poly-Time Algorithms lecture
def Algorithm2(array):
		maxSum = float("-inf")  #initialize max sum to some arbitrarily low number

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
					maxArrayIndexHigh = j
				# set up the return array
		maxArray = [maxArrayIndexLow,maxArrayIndexHigh,maxSum] #start index, end index, MSS sum
		return maxArray

#O(n*lg(n)) recursive algorithm. Based off mycodeschool https://gist.github.com/mycodeschool/8b4bcff69427c8a6f2aa implementation
#key addition includes storing keeping track of the indices of the MSS in the recursive calls
def Algorithm3(array):
	#store the original input array w/o index prefix info (so that reference index work)
	workingArray = []
	for i in range(3,len(array)):
		workingArray.append(array[i])

	#base case, indicies are equal so it is a 1 element array.
	leftIndex = array[0] #could probably use these values directly but its easier to read w/left right index ithink
	rightIndex = array[1]
	if(leftIndex == rightIndex):
		array[2] = workingArray[leftIndex]
		return array

	midPoint = int((array[0] + array[1])/2)  #casting to int is same thing as floor function

	#deal with left MSS
	leftMSSinput = [array[0],midPoint,array[2]] # here is the prefix info, left index, right index, sum, then input array
	for i in range(3,len(array)):
		leftMSSinput.append(array[i])
	leftMSS = []
	leftMSS = Algorithm3(leftMSSinput) # recurse

	#deal with right MSS
	rightMSSinput = [midPoint + 1,array[1],array[2]] # set up prefix info for right just like left
	for i in range(3,len(array)):
		rightMSSinput.append(array[i])
	rightMSS = []
	rightMSS = Algorithm3(rightMSSinput)

	# now deal with the split case
	leftMax = workingArray[midPoint]
	rightMax = workingArray[midPoint + 1]
	lowIndexSplit = midPoint
	highIndexSplit = midPoint + 1
	tempSum = 0

	#work backward from midpoint
	for i in range(midPoint,array[0] -1,-1):
		tempSum += workingArray[i]
		if(tempSum >= leftMax):
			lowIndexSplit = i
			leftMax = tempSum

	#work forward from midpoint
	tempSum = 0
	for i in range(midPoint + 1,array[1] + 1):
		tempSum += workingArray[i]
		if(tempSum >= rightMax):
			highIndexSplit = i
			rightMax = tempSum

		#final bit of logic for finding max. Once max is found, update prefix (left index, right index, sum) and return to next level recursion

	if(leftMSS[2] >= rightMSS[2]):
		if(leftMSS[2] >= (leftMax + rightMax)):
			array[0] = leftMSS[0]
			array[1] = leftMSS[1]
			array[2] = leftMSS[2]

			return array
		else:
			array[0] = lowIndexSplit
			array[1] = highIndexSplit
			array[2] = leftMax + rightMax

			return array
	else:
		if(rightMSS[2] >= (leftMax + rightMax)):
			array[0] = rightMSS[0]
			array[1] = rightMSS[1]
			array[2] = rightMSS[2]

			return array
		else:
			array[0] = lowIndexSplit
			array[1] = highIndexSplit
			array[2] = leftMax + rightMax

			return array

# O(n) Linear-time - iteration for max subarray.
# Source: Based on Prof. Borradaile's Designing Poly-Time Algorithms lecture and the provided Algorithm 4 Pseudocode.pdf
def Algorithm4(array):
	n = len(array)
	maxSum = float("-inf")
	endingHereSum = float("-inf")

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

	maxArray = [maxArrayIndexLow,maxArrayIndexHigh,maxSum]

	return maxArray


#Here is the "main" function so far it just reads every line from a file, stores those lines (arrays)
#as an array and then stores those in an array of arrays (so you only have to get file contents once. )

#declare and array to hold the arrays from file.
arrayOfArrays = []
with open('MSS_Problems.txt','r') as f:
	#parse each line in test file and store in array to send to the different functions
	for line in f:
		#ignore blank lines
		if not line.strip():
			garbage = 1 #lol just for fun, keep track of if there is a blank line in the input file
		else:
			line = line.replace("[","")
			line = line.replace("]","")
			line = line.replace(" ","")
			line = line.replace('\n',"")
			#parsing on comma
			array = [int(x) for x in line.split(",")]
			#make array of arrays for use in all 4 algorithms.
			arrayOfArrays.append(array)


fo = open("MSS_Results.txt","w+") #open file object to print results

#output to MSS_results.txt file alg1 results
fo.write("Algorithm 1 results: \n")
for k in arrayOfArrays:
	alg1results = []
	alg1results = Algorithm1(k)
	fo.write(str(k) + '\n')
	fo.write(str(k[alg1results[0]:alg1results[1] + 1]) + '\n')
	fo.write(str(alg1results[2]) + '\n')

#output to MSS_results.txt file alg2 results
fo.write("Algorithm 2 results: \n")
for k in arrayOfArrays:
	alg2results = []
	alg2results = Algorithm2(k)
	fo.write(str(k) + '\n')
	fo.write(str(k[alg2results[0]:alg2results[1] + 1]) + '\n')
	fo.write(str(alg2results[2]) + '\n')
#output to MSS_results.txt file alg3 results
fo.write("Algorithm 3 results: \n")
for k in arrayOfArrays:

	lastIndex = len(k) - 1
	inputArray = [0,lastIndex,0]

	for i in range(0,len(k)):
		inputArray.append(k[i])

	alg3results = []
	alg3results = Algorithm3(inputArray)

	fo.write(str(k) + '\n')
	fo.write(str(k[alg3results[0]:alg3results[1] + 1]) + '\n')
	fo.write(str(alg3results[2]) + '\n')

fo.write("Algorithm 4 results: \n")
for k in arrayOfArrays:
	alg4results = []
	alg4results = Algorithm4(k)
	fo.write(str(k) + '\n')
	fo.write(str(k[alg4results[0]:alg4results[1] + 1]) + '\n')
	fo.write(str(alg4results[2]) + '\n')

print "done"
fo.close()

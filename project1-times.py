#!/usr/bin/python
#Cas Donoghue
#Patrick Kwong
#Nicholas Vrontakis
#Group 31
#Project1 CS325 Analysis of Algorithms - timing
#OCT 6 2016


from random import choice
from time import time

from project1final import Algorithm1
from project1final import Algorithm2
from project1final import Algorithm3
from project1final import Algorithm4

with open('algorithm_1_times.txt', 'w') as f:
	for n in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 125, 150, 175, 200]:
		total_time = 0
		for i in range(10):
			array = [choice(range(-100, 100)) for x in range(n)]
			start = time()
			Algorithm1(array)
			end = time()
			total_time += (end - start)
		average_time = total_time / 10
		f.write('{:6}\t{}\n'.format(n, average_time))

with open('algorithm_2_times.txt', 'w') as f:
	for n in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
		total_time = 0
		for i in range(10):
			array = [choice(range(-100, 100)) for x in range(n)]
			start = time()
			Algorithm2(array)
			end = time()
			total_time += (end - start)
		average_time = total_time / 10
		f.write('{:6}\t{}\n'.format(n, average_time))

with open('algorithm_3_times.txt', 'w') as f:
	for n in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
		total_time = 0
		for i in range(10):
			array = [choice(range(-100, 100)) for x in range(n)]
			prefixedArray = [0,len(array) - 1,0]
			for i in range(0,len(array)):
				prefixedArray.append(array[i])
			start = time()
			Algorithm3(prefixedArray)
			end = time()
			total_time += (end - start)
		average_time = total_time / 10
		f.write('{:6}\t{}\n'.format(n, average_time))

with open('algorithm_4_times.txt', 'w') as f:
	for n in [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]:
		total_time = 0
		for i in range(10):
			array = [choice(range(-100, 100)) for x in range(n)]
			start = time()
			Algorithm4(array)
			end = time()
			total_time += (end - start)
		average_time = total_time / 10
		f.write('{:6}\t{}\n'.format(n, average_time))
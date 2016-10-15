import csv
import random

array_sizes = [100, 1000, 10000, 100000]

with open("testarrays.txt", "w+") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for size in array_sizes:
        rand_nums = []
        for num in range(size):
            rand_nums.append(random.randint(-1000, 1000))
        csv_writer.writerow(rand_nums)

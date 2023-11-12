# read portfolio.csv file
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './portfolio.csv')

with open(filename, 'r') as file:
    for line in file:
        data = line.split(",")
        t = {data[0], int(data[1]), float(data[2])}


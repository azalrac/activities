import os
import csv

csvpath = os.path.join(".","resources","cereal_bonus.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    row = 2

    for row in csvreader:
        if float(row[7])>5:
            print(row)
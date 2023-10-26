import csv
import os


with open('profiles1.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["XXX", "XXX", "XXX"])




with open('profiles1.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)



# I want to read the file and find if there is any profil from Ukraine
# if there is any profil from Ukraine I want to print it

with open('profiles1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[2] == 'Ukraine':
            print(row)


data = []

with open('profiles1.csv', 'r') as input_file:
    data = list(csv.reader(input_file))

#remove last 2 rows
data = data[:-2]

with open('profiles1.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(data)


import csv


with open('resources/sample.csv', newline='') as file:
    reader = csv.reader(file, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(*row)



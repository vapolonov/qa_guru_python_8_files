# f = open('example.txt', 'w')
# f.write('abcd')
# f.close()

with open('resources/example.txt', 'r') as file:
    print(file)
    for row in file:
        print(row)
    file.seek(0)
    for row in file.readlines():
        print(row, end='')

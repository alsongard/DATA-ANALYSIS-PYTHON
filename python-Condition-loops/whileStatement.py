"""
    for the while loop it executes a statement as long as the condition is met
    however prevent entering into a loop us

    structure:
    while condition:
        statement
"""

line = "*"
# print(type(line))
# print(line)
# print(len(line))

while len(line) <= 10:
    print(line)
    line = line + "*"

while len(line) > 0:
    print(line)
    line = line[:-1]


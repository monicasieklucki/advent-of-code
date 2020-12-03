
f = open(r"C:\Users\User\Desktop\AOC\input\Day1.txt")

numbers = []

sum = 2020

for line in f:
    numbers.append(int(line))

# Part 1 #
for n1 in numbers:
    if (2020 - n1) in numbers:
        print(n1 * (2020 - n1))
            
# Part 2 #
for n1 in numbers:
    for n2 in numbers:
        if (2020 - n1 - n2) in numbers:
            print ((2020 - n1 - n2) * n1 * n2)
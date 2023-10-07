import random

x = [1, 2, 3, 4, 4]
file = open("file.txt", "w")
for n in range(0, 1000):
    num = random.randint(0, 10)
    x.append(num)
for n in x:
    file.write(str(n))
file.close()
print(file)
#2.1 + 2.2 + 2.3 + 2.4
sizes = [5,7,300,90,24,50,75]
print("Hello, My name is Dat and there are my sheep sizes")
print(sizes)

max = sizes[0]
for i in sizes:
    if max < i:
        max = i
print("My biggest sheep has size",end = ' ')
print(max,end = ' ')
print("let's shear it")

sizes[2] = 8
print("After shearing, here is my flock")
print(sizes)

for i in range(7):
    sizes[i] += 50
print("One month has passed, now here is my flock")
print(sizes)
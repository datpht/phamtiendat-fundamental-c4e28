#2.5
sizes = [5,7,300,90,24,50,75]
m = 1
print("Hello, My name is Dat and there are my sheep sizes")
print(sizes)
for mth in range(3):
    print("MONTH", end = ' ')
    print(m,end = '')
    print(":")
    m = m + 1
   
    for i in range(7):
        sizes[i] += 50
    print("One month has passed, now here is my flock")
    print(sizes)
    
    max = sizes[0]
    for j in sizes:
        if max < j:
            max = j
    print("Now my biggest sheep has size",end = ' ')
    print(max,end = ' ')
    print("let's shear it")
    
    for k,j in enumerate(sizes):
        if max == j:
            sizes[k] = 8
            print("After shearing, here is my flock")
            print(sizes)


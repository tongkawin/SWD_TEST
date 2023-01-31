array = [ 1, 2, 1, 3, 5, 6, 4 ]  #input array here
max = 0
compare = 0
j = 0
index = 0
for i in array:
    j += 1
    if j == 1:
        max = i
        compare = i
    compare = i
    if max < compare:
        max = compare
        index = j
print(index-1)
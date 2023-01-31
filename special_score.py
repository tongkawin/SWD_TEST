#Roman to num :)

values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
word = 'XXX'
result = 0
for i in range(len(word)):
    if i > 0 and values[word[i]] > values[word[i-1]]:
        result += values[word[i]] - 2 * values[word[i-1]]
    else:
        result += values[word[i]] 
print(result)
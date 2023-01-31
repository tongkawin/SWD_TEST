factorial = 29 #input number here
num = 1
mod = 10
count = 0
while factorial >= 1:
    num = num*factorial
    factorial = factorial-1
while num%mod == 0:
    mod = mod*10
    count += 1
print(count)
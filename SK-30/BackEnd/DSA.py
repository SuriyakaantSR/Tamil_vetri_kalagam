n = int(input("Enter a value of n : "))
s = 0 # switch off
for i in range(2,n):
    if n % i == 0:
        s = 1   # Switch On if not a prime
        break
if s == 0:
    print(n,"is Prime")
else:
    print(n,"Not Prime")
#Prime or not prime. Input: L= [3,4,6,9,11] Output: L= [P, NP, NP, NP, P] using map function.

l = [3,4,6,9,11]

def isPrime(x):
    flag = 1
    if x == 1: return "np"
    elif x == 2: return "p"
    for i in range(2,x):
        if(x%i == 0):
            flag = 0
    if(flag):
        return "p"
    else:
        return "np"

output = map(isPrime, l)

print(list(output))
    
        
#define the gen_primes function here
def prime(number):
    for _ in range(2,number):
        if number % _ == 0:
            return False
        return True

def genPrimes():
    number = 2
    while True:
        if prime(number):
            yield number
        number += 1

def main():
    data = input()
    l = data.split()
    a = int(l[0])
    b = int(l[1])
    primeGenerator = genPrimes()
    for i in range(a):
        p = primeGenerator.__next__()
        if(i%b == 0):
            print(p)
    
if __name__== "__main__":
    main()

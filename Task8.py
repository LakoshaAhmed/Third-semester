def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**(1/2)) + 1, 2):
        if n % i == 0:
            return False
    return True

total = 0
primes = []

for num in range(2, 101):
    if is_prime(num):
        primes.append(num)
        total =sum (primes)

print("Prime numbers between 2 and 100:" , primes)

print("Sum of all prime numbers between 2 and 100,", total)

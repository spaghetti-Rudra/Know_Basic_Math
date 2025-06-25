# Count Digits
n = 12345
count = 0
while n > 0:
    n = n // 10
    count += 1
print("Number of digits:", count)

# Reverse a Number
n = 1234
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
print("Reversed number:", rev)

# Armstrong Number
n = 153
temp = n
result = 0
while n > 0:
    digit = n % 10
    result += digit ** 3
    n //= 10
print("Armstrong" if result == temp else "Not Armstrong")

# Prime Check (Corrected Version)
N = int(input("Enter number: "))
if N < 2:
    print("Not Prime:", N)
else:
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            print("Not Prime:", N)
            break
    else:
        print("Prime:", N)

# All Factors of a Number
n = 36
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        print(i)
        if i != n // i:
            print(n // i)

# GCD (Greatest Common Divisor)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print("GCD:", gcd(48, 18))  # Example output: 6

# LCM (Least Common Multiple)
def lcm(a, b):
    return (a * b) // gcd(a, b)
print("LCM:", lcm(12, 15))  # Example output: 60

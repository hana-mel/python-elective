#program to generate n prime numbers
n = int(input("How many prime numbers do you want to print? "))
count = 0
num = 2

while count < n:
    is_prime = True
    for item in range(2, int(num ** (1/2)) + 1):
        if num % item == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        count += 1
    num += 1

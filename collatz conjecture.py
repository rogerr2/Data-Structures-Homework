#Roger Robinson
#Part A

n = int(input("Enter a positive number: "))

def collatzConjecture(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(n * 3 + 1)
    else:
        print(n)

collatzConjecture(n)


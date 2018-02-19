#Roger Robinson
#Part B.2

from timeit import default_timer as timer

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

for i in range(1, 100):
    print (fib(i))


start = timer()
end = timer()
print(end - start)


#Roger Robinson
#Part B.1

from timeit import default_timer as timer

def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+ fib(n-2)

for i in range(1, 100):
        print(fib(i))

start = timer()
end = timer()
print(end-start)



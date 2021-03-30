import time


def Fib(x, memo = {}):
    if x in memo:
        return memo[x]
    if x <= 2:
        return 1
    memo[x] = Fib(x - 1, memo) + Fib(x - 2, memo)
    return memo[x]

time_start = time.time()
inp = int(input("Choose value: "))
sol = Fib(inp)
print(f"The {inp}th Fibonacci value is {float(sol)}")
print(f"And it took {time.time()-time_start:.3f} seconds to calculate")

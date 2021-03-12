def Fib(x, memo = {}):
    if x in memo:
        return memo[x]
    if x <= 2:
        return 1
    memo[x] = Fib(x - 1, memo) + Fib(x - 2, memo)
    return memo[x]


sol = Fib(int(input("Choose value: ")))
print(f"Fibonacci value is {sol}")

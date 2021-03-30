import time

def grid(x, y, memo = {}):
    if (x, y) in memo:
        return memo[(x, y)]
    if x == 0 or y == 0:
        return 0
    if x == 1 and y == 1:
        return 1
    memo[(x, y)] =  grid(x - 1, y) + grid(x, y - 1)
    return memo[(x, y)]

n = int(input("Number of rows: "))
m = int(input("Number of columns: "))
start = time.time()
print(f"Number of possible routes: {float(grid(n, m))}")
print(f"Coumputed in {time.time()-start:.2f} seconds")

def min_coins(sum, coins, opt = - 1, memo = {}):
    if sum <= 0:
        return 0
    if sum == 1:
        return 1
    if sum in memo:
        return memo[sum]
    for coin in coins:
        if coin <= sum:
            new_sum = sum - coin
            memo[sum] = min_coins(new_sum, coins, memo = memo) + 1
            if memo[sum] < opt or opt == -1:
                opt = memo[sum]
    return opt

sum = int(input("For what sum do you wish to calculate? "))
try:
    coins = []
    while (True):
        coins.append(int(input("What coins are available? ")))
except:
    coin_dict = {coin:0 for coin in coins}
print(min_coins(sum, coins))

def minimumNumberCoins(money, coins):
    minCoins = [0] * money
    m = len(coins)
    for i in range(1, money):
        minCoins[i] = float('inf')
        for j in range(1, m):
            if i >= coins[j]:
                numCoins = minCoins[i - coins[j]] + 1
                if numCoins < minCoins[i]:
                    minCoins[i] = numCoins
    return minCoins[money - 1]


value = int(input())
print(minimumNumberCoins(value + 1, [0, 1, 3, 4]))

def knapsack(items, i, size):
    """items: sequence of weights,
    i: item you're considering; i==len(items)->done
    size: size of knapsack"""
    memo = {0: [0]}

    for i in range(len(items)):
        memo[i+1] = []
        for weights in memo[i]:
            memo[i+1].append(weights)
            if weights + items[i] <= size:
                memo[i+1].append(weights + items[i])

    # see the max size of len(items)
    print(memo)
    return max(memo[len(items)])

items = [4, 2, 3]
size = 5
print(knapsack(items, 0, size))


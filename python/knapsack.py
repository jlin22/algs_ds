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
    return max(memo[len(items)])

def knapsack_v2(sizes, values, knapsack_size):
    """sizes: array of sizes of items
    values: array of values of items
    sizes[i] corresponds to weight of item at values[i]
    knapsack_size: how much your knapsack can carry"""

    #memo[item you're considering][total weight of items so far]
    memo = {}

    #Base case
    memo[len(sizes)] = [0 for s in range(knapsack_size+1)]
    
    #In topologically sorted order
    for i in reversed(range(len(sizes))):
        memo[i] = [0 for s in range(knapsack_size+1)]
        for s in range(knapsack_size+1):
            if s >= sizes[i]:
                memo[i][s] = max(memo[i+1][s], memo[i+1][s-sizes[i]] + values[i])
            else:
                memo[i][s] = memo[i+1][s]
    return max(memo[0])

items = [4, 2, 3]
values = [10, 4, 7]
size = 5
print(knapsack(items, 0, size))
print()
print(knapsack_v2(items, values, size))

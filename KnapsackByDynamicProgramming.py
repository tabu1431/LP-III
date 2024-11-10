# Function to solve 0-1 Knapsack Problem using Dynamic Programming
def knapsack(weights, values, capacity):
    n = len(weights)
    # Create a 2D DP table where dp[i][w] represents the maximum value for first i items with weight limit w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]  # Return the maximum value that can be obtained

# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

max_value = knapsack(weights, values, capacity)
print("Maximum value in Knapsack:", max_value)

# Function to solve the fractional knapsack problem
def fractional_knapsack(weights, values, capacity):
    # Calculate value-to-weight ratio for each item and sort by this ratio in descending order
    items = sorted([(v / w, w, v) for v, w in zip(values, weights)], reverse=True)
    total_value = 0  # Total value accumulated
    for ratio, weight, value in items:
        if capacity >= weight:
            # Take the whole item
            total_value += value
            capacity -= weight
        else:
            # Take fraction of the item
            total_value += ratio * capacity
            break
    return total_value

# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

max_value = fractional_knapsack(weights, values, capacity)
print("Maximum value in Knapsack:", max_value)

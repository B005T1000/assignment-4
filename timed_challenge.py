# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

def running_total_with_reset(values):
    """
    Track a running total of values. If a negative number is added, reset the total to 0.

    Example:
    Input: [5, 7, -1, 3, 2]
    Output: [5, 12, 0, 3, 5]
    """
    # A simple list is the right structure here because we need to maintain 
    # the running totals in order. Each step only depends on the previous total.
    # The operations are additions and resets, both O(1), making the entire 
    # algorithm O(n) where n is the number of values.
    totals = []
    current = 0
    for v in values:
        if v < 0:
            current = 0
        else:
            current += v
        totals.append(current)
    return totals


# Quick test
print(running_total_with_reset([5, 7, -1, 3, 2]))  # [5, 12, 0, 3, 5]
print(running_total_with_reset([1, 2, 3]))         # [1, 3, 6]
print(running_total_with_reset([-5, 10, -2, 4]))   # [0, 10, 0, 4]
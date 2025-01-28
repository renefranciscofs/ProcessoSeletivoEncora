def makeChange(n):
    """
    The function below will calculate all possible ways to represent `n` cents
    using an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents),
    and pennies (1 cent). Each combination is represented as a list [quarters, dimes, nickels, pennies].

    The function works as follows:
    - Iterate over all possible numbers of quarters (from 0 to the maximum possible).
    - For each number of quarters, iterate over all possible numbers of dimes.
    - For each combination of quarters and dimes, iterate over all possible numbers of nickels.
    - Calculate the remaining amount to be represented by pennies.
    - If the remaining amount is non-negative, add the combination to the result set as a list.
    - Return the set of all valid combinations.
    """
    result = set()  # Use a set to store unique combinations

    # Iterate over all possible numbers of quarters
    for quarters in range(n // 25 + 1):
        # Iterate over all possible numbers of dimes
        for dimes in range((n - quarters * 25) // 10 + 1):
            # Iterate over all possible numbers of nickels
            for nickels in range((n - quarters * 25 - dimes * 10) // 5 + 1):
                # Calculate the remaining amount to be represented by pennies
                pennies = n - (quarters * 25 + dimes * 10 + nickels * 5)
                # Ensure the remaining amount is non-negative
                if pennies >= 0:
                    # Add the combination to the result set as a list
                    result.add(tuple([quarters, dimes, nickels, pennies]))

    # Convert the set of tuples to a set of lists for the final output
    return [list(combination) for combination in result]

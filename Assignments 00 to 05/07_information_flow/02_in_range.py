def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    # Check if n is greater than or equal to low and less than or equal to high
    return low <= n <= high

# Sample test cases
print(in_range(5, 1, 10))  
print(in_range(15, 1, 10)) 
print(in_range(3, 1, 3))

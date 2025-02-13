def n()print("")

def recursive_function(n, count=0):
    if n <= 0:
        return count
    else:
        return recursive_function(n - 1, count + 1)

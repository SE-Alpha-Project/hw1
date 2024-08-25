def fibo_recurs(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_recurs(n-1) + fibo_recurs(n-2)

# Example usage
print(fibo_recurs(n)) 

"""
Command: prime_numbers
Return a list of all the prime numbers inferior or equal to n
"""
def prime_numbers(n):
    
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n > 2 and n % 2 == 0:
            return False
    
        max_div = math.floor(math.sqrt(n))
        for i in range(3, 1 + max_div, 2):
            if n % i == 0:
                return False
        return True

    result = []
    for i in range(n+1):
        if is_prime(i):
            result.append(i)
    return result


"""
Command: sum_prime_numbers
Return a sum of all the prime numbers inferior or equal to n
"""
def sum_prime_numbers(n):
    return sum(prime_numbers(n))

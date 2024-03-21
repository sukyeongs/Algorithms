import math

def convert(n, k):
    result = ''
    q, r = divmod(n, k)
    if q == 0:
        return str(r)
    else:
        return convert(q, k) + str(r)
        

def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def solution(n, k):
    answer = 0
    
    conver_str = convert(n, k)
    prime_list = conver_str.split('0')
    print(prime_list)
    
    for prime in prime_list:
        if len(prime) != 0 and is_prime(int(prime)):
            answer += 1
    
    return answer
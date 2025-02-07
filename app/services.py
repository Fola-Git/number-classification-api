def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def get_fun_fact(n: int) -> str:
    import requests
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math")
        if response.status_code == 200:
            return response.text
    except:
        pass
    return "Fun fact not available."

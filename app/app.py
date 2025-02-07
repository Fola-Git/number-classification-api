from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"] , # Allow all methods
    allow_headers=["*"]  # Allow all headers
)

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
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math")
        if response.status_code == 200:
            return response.text
    except:
        pass
    return "Fun fact not available."

@app.get("/api/classify-number")
def classify_number(number: str):
    if not number.isdigit():
        raise HTTPException(status_code=400, detail={"number": number, "error": True})
    
    num = int(number)
    digit_sum = sum(int(digit) for digit in str(num))
    properties = ["odd" if num % 2 != 0 else "even"]
    if is_armstrong(num):
        properties.insert(0, "armstrong")
    
    return {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": get_fun_fact(num)
    }
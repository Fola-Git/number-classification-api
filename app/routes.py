
from fastapi import APIRouter, HTTPException
from app.services import is_prime, is_perfect, is_armstrong, get_fun_fact

router = APIRouter()

@router.get("/classify-number")
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

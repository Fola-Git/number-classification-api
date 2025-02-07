from pydantic import BaseModel

class NumberRequest(BaseModel):
    number: str

class NumberResponse(BaseModel):
    number: int
    is_prime: bool
    is_perfect: bool
    properties: list
    digit_sum: int
    fun_fact: str
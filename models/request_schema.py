from pydantic import BaseModel, Field


class PowerRequest(BaseModel):
    base: int = Field(..., description="Baza numarului")
    exponent: int = Field(..., description="Exponentul")


class FactorialRequest(BaseModel):
    number: int = Field(..., ge=0, description="Numar intreg pozitiv")


class FibonacciRequest(BaseModel):
    number: int = Field(..., ge=0, description="Indexul n in sirul Fibonacci")

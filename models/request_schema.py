from pydantic import BaseModel, Field


class PowerRequest(BaseModel):
    base: int = Field(..., description="Baza numărului")
    exponent: int = Field(..., description="Exponentul")


class FactorialRequest(BaseModel):
    number: int = Field(..., ge=0, description="Număr întreg pozitiv")


class FibonacciRequest(BaseModel):
    number: int = Field(..., ge=0, description="Indexul n în șirul Fibonacci")

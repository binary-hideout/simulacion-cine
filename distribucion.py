from random import random

def distribucion(sd: float, m: float) -> float:
    suma = sum(random() for _ in range(12))
    normal = m + (sd * (suma - 6))
    return normal

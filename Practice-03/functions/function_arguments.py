# Positional and default arguments

def power(base, exponent=2):
    """Raise base to exponent (default square)"""
    return base ** exponent


print(power(5))      # 25
print(power(2, 3))   # 8


"""
See the README for the mathematics behind this.
"""

def peasant(a, b):
    """
    Multiplication, without multiplication!
    """
    ret_val = 0
    while b > 0:
        if b & 1:
            ret_val += a
        a <<= 1
        b >>= 1
    return ret_val

from functools import wraps
import numbers 
from data import *

"""
Chose List over Dictionary as data, for future extensibility
"""

__all__ = [
    "Element",
]

def guess_symbol(key):
    symbol = key.strip().title()[0:2]
    if symbol in Symbols:
        pass 
    elif symbol[0] in Symbols:
        symbol = symbol[0]
    else: 
        symbol = "X" 
    return symbol

def guess_atomic_number(key):
    if isinstance(key,numbers.Integral):
        atomic_number = key 

    elif isinstance(key,str):
        key = key.title() 
        if key in Names:
            atomic_number=Names.index(key)
        else: 
            symbol = guess_symbol(key) 
            atomic_number = Symbols.index(symbol)
    else:
        atomic_number = 0 # X 


    if (atomic_number < 1 or atomic_number > 118):
        raise ValueError(f"Can not guess element from '{key}'")
    else:
        return atomic_number

"""
Decorator to convert key into atomic_number 
"""
def to_atomic_number(arg_id):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            args = list(args)
            args[arg_id] = guess_atomic_number(args[arg_id])
            args = tuple(args)
            return func(*args, **kwargs)
        return wrapper
    return decorator



class Element:
    @to_atomic_number(1)
    def __init__(self,key):
        self.atomic_number = key

    @property 
    def name(self):
        return Names[self.atomic_number] 

    @property 
    def symbol(self):
        return Symbols[self.atomic_number] 

    @property
    def atomic_mass(self):
        return AtomicMasses[self.atomic_number]

    @property 
    def vdw_radius(self):
        return vdw_radii[self.atomic_number] 

    @property
    def vesta_hex_color(self):
        return Vesta_hex_colors[self.atomic_number]

    @property
    def cpk_hex_color(self):
        return Cpk_hex_colors[self.atomic_number]
    
    @property
    def jmol_hex_color(self):
        return Cpk_hex_colors[self.atomic_number]

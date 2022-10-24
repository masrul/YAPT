from functools import wraps
import numbers 

"""
Chose List over Dictionary as data, for future extensibility
"""

Names = [
    "Ghost", #0
    "Hydrogen", #1
    "Helium", #2
    "Lithium", #3
    "Beryllium", #4
    "Boron", #5
    "Carbon", #6
    "Nitrogen", #7
    "Oxygen", #8
    "Fluorine", #9
    "Neon", #10
    "Sodium", #11
    "Magnesium", #12
    "Aluminum", #13
    "Silicon", #14
    "Phosphorus", #15
    "Sulfur", #16
    "Chlorine", #17
    "Argon", #18
    "Potassium", #19
    "Calcium", #20
    "Scandium", #21
    "Titanium", #22
    "Vanadium", #23
    "Chromium", #24
    "Manganese", #25
    "Iron", #26
    "Cobalt", #27
    "Nickel", #28
    "Copper", #29
    "Zinc", #30
    "Gallium", #31
    "Germanium", #32
    "Arsenic", #33
    "Selenium", #34
    "Bromine", #35
    "Krypton", #36
    "Rubidium", #37
    "Strontium", #38
    "Yttrium", #39
    "Zirconium", #40
    "Niobium", #41
    "Molybdenum", #42
    "Technetium", #43
    "Ruthenium", #44
    "Rhodium", #45
    "Palladium", #46
    "Silver", #47
    "Cadmium", #48
    "Indium", #49
    "Tin", #50
    "Antimony", #51
    "Tellurium", #52
    "Iodine", #53
    "Xenon", #54
    "Cesium", #55
    "Barium", #56
    "Lanthanum", #57
    "Cerium", #58
    "Praseodymium", #59
    "Neodymium", #60
    "Promethium", #61
    "Samarium", #62
    "Europium", #63
    "Gadolinium", #64
    "Terbium", #65
    "Dysprosium", #66
    "Holmium", #67
    "Erbium", #68
    "Thulium", #69
    "Ytterbium", #70
    "Lutetium", #71
    "Hafnium", #72
    "Tantalum", #73
    "Tungsten", #74
    "Rhenium", #75
    "Osmium", #76
    "Iridium", #77
    "Platinum", #78
    "Gold", #79
    "Mercury", #80
    "Thallium", #81
    "Lead", #82
    "Bismuth", #83
    "Polonium", #84
    "Astatine", #85
    "Radon", #86
    "Francium", #87
    "Radium", #88
    "Actinium", #89
    "Thorium", #90
    "Protactinium", #91
    "Uranium", #92
    "Neptunium", #93
    "Plutonium", #94
    "Americium", #95
    "Curium", #96
    "Berkelium", #97
    "Californium", #98
    "Einsteinium", #99
    "Fermium", #100
    "Mendelevium", #101
    "Nobelium", #102
    "Lawrencium", #103
    "Rutherfordium", #104
    "Dubnium", #105
    "Seaborgium", #106
    "Bohrium", #107
    "Hassium", #108
    "Meitnerium", #109
    "Darmstadtium", #110
    "Roentgenium", #111
    "Copernicium", #112
    "Nihonium", #113
    "Flerovium", #114
    "Moscovium", #115
    "Livermorium", #116
    "Tennessine", #117
    "Oganesson", #118
]


Symbols=[
    "X", #0
    "H", #1
    "He", #2
    "Li", #3
    "Be", #4
    "B", #5
    "C", #6
    "N", #7
    "O", #8
    "F", #9
    "Ne", #10
    "Na", #11
    "Mg", #12
    "Al", #13
    "Si", #14
    "P", #15
    "S", #16
    "Cl", #17
    "Ar", #18
    "K", #19
    "Ca", #20
    "Sc", #21
    "Ti", #22
    "V", #23
    "Cr", #24
    "Mn", #25
    "Fe", #26
    "Co", #27
    "Ni", #28
    "Cu", #29
    "Zn", #30
    "Ga", #31
    "Ge", #32
    "As", #33
    "Se", #34
    "Br", #35
    "Kr", #36
    "Rb", #37
    "Sr", #38
    "Y", #39
    "Zr", #40
    "Nb", #41
    "Mo", #42
    "Tc", #43
    "Ru", #44
    "Rh", #45
    "Pd", #46
    "Ag", #47
    "Cd", #48
    "In", #49
    "Sn", #50
    "Sb", #51
    "Te", #52
    "I", #53
    "Xe", #54
    "Cs", #55
    "Ba", #56
    "La", #57
    "Ce", #58
    "Pr", #59
    "Nd", #60
    "Pm", #61
    "Sm", #62
    "Eu", #63
    "Gd", #64
    "Tb", #65
    "Dy", #66
    "Ho", #67
    "Er", #68
    "Tm", #69
    "Yb", #70
    "Lu", #71
    "Hf", #72
    "Ta", #73
    "W", #74
    "Re", #75
    "Os", #76
    "Ir", #77
    "Pt", #78
    "Au", #79
    "Hg", #80
    "Tl", #81
    "Pb", #82
    "Bi", #83
    "Po", #84
    "At", #85
    "Rn", #86
    "Fr", #87
    "Ra", #88
    "Ac", #89
    "Th", #90
    "Pa", #91
    "U", #92
    "Np", #93
    "Pu", #94
    "Am", #95
    "Cm", #96
    "Bk", #97
    "Cf", #98
    "Es", #99
    "Fm", #100
    "Md", #101
    "No", #102
    "Lr", #103
    "Rf", #104
    "Db", #105
    "Sg", #106
    "Bh", #107
    "Hs", #108
    "Mt", #109
    "Ds", #110
    "Rg", #111
    "Cn", #112
    "Nh", #113
    "Fl", #114
    "Mc", #115
    "Lv", #116
    "Ts", #117
    "Og", #118
]

AtomicNumbers = [i for i in range(119)]

AtomicMasses=[
    None, #0 
    1.0080, #1
    4.0026, #2
    6.9400, #3
    9.0122, #4
    10.8100, #5
    12.0110, #6
    14.0070, #7
    15.9990, #8
    18.9984, #9
    20.1797, #10
    22.9898, #11
    24.3050, #12
    26.9815, #13
    28.0850, #14
    30.9738, #15
    32.0600, #16
    35.4500, #17
    39.9480, #18
    39.0983, #19
    40.0780, #20
    44.9559, #21
    47.8670, #22
    50.9415, #23
    51.9961, #24
    54.9380, #25
    55.8450, #26
    58.9332, #27
    58.6934, #28
    63.5460, #29
    65.3800, #30
    69.7230, #31
    72.6300, #32
    74.9216, #33
    78.9710, #34
    79.9040, #35
    83.7980, #36
    85.4678, #37
    87.6200, #38
    88.9058, #39
    91.2240, #40
    92.9064, #41
    95.9500, #42
    97.9072, #43
    101.0700, #44
    102.9055, #45
    106.4200, #46
    107.8682, #47
    112.4140, #48
    114.8180, #49
    118.7100, #50
    121.7600, #51
    127.6000, #52
    126.9045, #53
    131.2930, #54
    132.9055, #55
    137.3270, #56
    138.9055, #57
    140.1160, #58
    140.9077, #59
    144.2420, #60
    144.9128, #61
    150.3600, #62
    151.9640, #63
    157.2500, #64
    158.9254, #65
    162.5000, #66
    164.9303, #67
    167.2590, #68
    168.9342, #69
    173.0450, #70
    174.9668, #71
    178.4900, #72
    180.9479, #73
    183.8400, #74
    186.2070, #75
    190.2300, #76
    192.2170, #77
    195.0840, #78
    196.9666, #79
    200.5920, #80
    204.3800, #81
    207.2000, #82
    208.9804, #83
    209.0000, #84
    210.0000, #85
    222.0000, #86
    223.0000, #87
    226.0000, #88
    227.0000, #89
    232.0377, #90
    231.0359, #91
    238.0289, #92
    237.0000, #93
    244.0000, #94
    243.0000, #95
    247.0000, #96
    247.0000, #97
    251.0000, #98
    252.0000, #99
    257.0000, #100
    258.0000, #101
    259.0000, #102
    262.0000, #103
    267.0000, #104
    268.0000, #105
    271.0000, #106
    274.0000, #107
    269.0000, #108
    276.0000, #109
    281.0000, #110
    281.0000, #111
    285.0000, #112
    286.0000, #113
    289.0000, #114
    288.0000, #115
    293.0000, #116
    294.0000, #117
    294.0000, #118
]

vdw_radii=[    # Alvarez
     None, #0
     1.20, #1
     1.43, #2
     2.12, #3
     1.98, #4
     1.91, #5
     1.77, #6
     1.66, #7
     1.50, #8
     1.46, #9
     1.58, #10
     2.50, #11
     2.51, #12
     2.25, #13
     2.19, #14
     1.90, #15
     1.89, #16
     1.82, #17
     1.94, #18
     2.73, #19
     2.62, #20
     2.58, #21
     2.46, #22
     2.42, #23
     2.45, #24
     2.45, #25
     2.44, #26
     2.40, #27
     2.40, #28
     2.38, #29
     2.39, #30
     2.32, #31
     2.29, #32
     1.88, #33
     1.82, #34
     1.86, #35
     2.07, #36
     3.21, #37
     2.84, #38
     2.75, #39
     2.52, #40
     2.56, #41
     2.45, #42
     2.44, #43
     2.46, #44
     2.44, #45
     2.15, #46
     2.53, #47
     2.49, #48
     2.43, #49
     2.42, #50
     2.47, #51
     1.99, #52
     2.04, #53
     2.28, #54
     3.48, #55
     3.03, #56
     2.98, #57
     2.88, #58
     2.92, #59
     2.95, #60
     None, #61
     2.90, #62
     2.87, #63
     2.83, #64
     2.79, #65
     2.87, #66
     2.81, #67
     2.83, #68
     2.79, #69
     2.80, #70
     2.74, #71
     2.63, #72
     2.53, #73
     2.57, #74
     2.49, #75
     2.48, #76
     2.41, #77
     2.29, #78
     2.32, #79
     2.45, #80
     2.47, #81
     2.60, #82
     2.54, #83
     None, #84
     None, #85
     2.40, #86
     None, #87
     None, #88
     2.80, #89
     2.93, #90
     2.88, #91
     2.71, #92
     2.82, #93
     2.81, #94
     2.83, #95
     3.05, #96
     3.40, #97
     3.05, #98
     2.70, #99
     None, #100
     None, #101
     None, #102
     None, #103
     None, #104
     None, #105
     None, #106
     None, #107
     None, #108
     None, #109
     None, #110
     None, #111
     None, #112
     None, #113
     None, #114
     None, #115
     None, #116
     None, #117
     None, #118
]


def guess_symbol(Str):
    symbol = Str.strip().title()[0:2]
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


    if (atomic_number<=0 or atomic_number>118):
        raise ValueError(f"Can not guess element from '{arg}'")
    else:
        return atomic_number






def to_atomic_number(arg_id):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            args = list(args)
            arg = args[arg_id]

            # atomic number 
            if isinstance(arg,numbers.Integral):
                pass 

            # symbol/name 
            elif isinstance(arg,str):
                arg = arg.title() 
                if arg in Names:
                    arg=Names.index(arg)
                else: 
                    symbol = guess_symbol(arg) 
                    if symbol == "X":
                        raise ValueError(f"Can not guess element from '{arg}'")
                    arg = Symbols.index(symbol) + 1

            else: 
                raise ValueError(f"Argument must be integer/string")

            args[arg_id] = arg 
            args = tuple(args)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@to_atomic_number(0)
def element_name(key):
    return Names[key]

@to_atomic_number(0)
def element_symbol(key):
    return Symbols[key]

@to_atomic_number(0)
def element_atomic_mass(key):
    return AtomicMasses[key]

@to_atomic_number(0)
def element_atomic_number(key):
    return key


class Element:
    @to_atomic_number(1)
    def __init__(self,key):
        self.name = Names[key] 
        self.symbol = Symbols[key]
        self.atomic_number = key
        self.atomic_mass = AtomicMasses[key] 
        self.vdw_radius = vdw_radii[key]
    

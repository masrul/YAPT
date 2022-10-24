import numpy as np 

periodic_table_txt="""Element,Symbol,AtomicNumber,AtomicMass,AtomicRadius
Hydrogen,H,1,1.0070000000000001,0.79
Helium,He,2,4.002,0.49
Lithium,Li,3,6.941,2.1
Beryllium,Be,4,9.012,1.4
Boron,B,5,10.811,1.2
Carbon,C,6,12.011,0.91
Nitrogen,N,7,14.007,0.75
Oxygen,O,8,15.999,0.65
Fluorine,F,9,18.998,0.57
Neon,Ne,10,20.18,0.51
Sodium,Na,11,22.99,2.2
Magnesium,Mg,12,24.305,1.7
Aluminum,Al,13,26.982,1.8
Silicon,Si,14,28.086,1.5
Phosphorus,P,15,30.974,1.2
Sulfur,S,16,32.065,1.1
Chlorine,Cl,17,35.453,0.97
Argon,Ar,18,39.948,0.88
Potassium,K,19,39.098,2.8
Calcium,Ca,20,40.078,2.2
Scandium,Sc,21,44.956,2.1
Titanium,Ti,22,47.867,2.0
Vanadium,V,23,50.942,1.9
Chromium,Cr,24,51.996,1.9
Manganese,Mn,25,54.938,1.8
Iron,Fe,26,55.845,1.7
Cobalt,Co,27,58.933,1.7
Nickel,Ni,28,58.693000000000005,1.6
Copper,Cu,29,63.54600000000001,1.6
Zinc,Zn,30,65.38,1.5
Gallium,Ga,31,69.723,1.8
Germanium,Ge,32,72.64,1.5
Arsenic,As,33,74.922,1.3
Selenium,Se,34,78.96,1.2
Bromine,Br,35,79.904,1.1
Krypton,Kr,36,83.79799999999999,1.0
Rubidium,Rb,37,85.46799999999999,3.0
Strontium,Sr,38,87.62,2.5
Yttrium,Y,39,88.906,2.3
Zirconium,Zr,40,91.22399999999999,2.2
Niobium,Nb,41,92.906,2.1
Molybdenum,Mo,42,95.96,2.0
Technetium,Tc,43,98.0,2.0
Ruthenium,Ru,44,101.07,1.9
Rhodium,Rh,45,102.906,1.8
Palladium,Pd,46,106.42,1.8
Silver,Ag,47,107.868,1.8
Cadmium,Cd,48,112.411,1.7
Indium,In,49,114.818,2.0
Tin,Sn,50,118.71,1.7
Antimony,Sb,51,121.76,1.5
Tellurium,Te,52,127.6,1.4
Iodine,I,53,126.904,1.3
Xenon,Xe,54,131.293,1.2
Cesium,Cs,55,132.905,3.3
Barium,Ba,56,137.327,2.8
Lanthanum,La,57,138.905,2.7
Cerium,Ce,58,140.116,2.7
Praseodymium,Pr,59,140.908,2.7
Neodymium,Nd,60,144.24200000000002,2.6
Promethium,Pm,61,145.0,2.6
Samarium,Sm,62,150.36,2.6
Europium,Eu,63,151.964,2.6
Gadolinium,Gd,64,157.25,2.5
Terbium,Tb,65,158.925,2.5
Dysprosium,Dy,66,162.5,2.5
Holmium,Ho,67,164.93,2.5
Erbium,Er,68,167.25900000000001,2.5
Thulium,Tm,69,168.93400000000003,2.4
Ytterbium,Yb,70,173.054,2.4
Lutetium,Lu,71,174.967,2.3
Hafnium,Hf,72,178.49,2.2
Tantalum,Ta,73,180.94799999999998,2.1
Wolfram,W,74,183.84,2.0
Rhenium,Re,75,186.207,2.0
Osmium,Os,76,190.23,1.9
Iridium,Ir,77,192.217,1.9
Platinum,Pt,78,195.084,1.8
Gold,Au,79,196.967,1.8
Mercury,Hg,80,200.59,1.8
Thallium,Tl,81,204.38299999999998,2.1
Lead,Pb,82,207.2,1.8
Bismuth,Bi,83,208.98,1.6
Polonium,Po,84,210.0,1.5
Astatine,At,85,210.0,1.4
Radon,Rn,86,222.0,1.3
Francium,Fr,87,223.0,
Radium,Ra,88,226.0,
Actinium,Ac,89,227.0,
Thorium,Th,90,232.03799999999998,
Protactinium,Pa,91,231.03599999999997,
Uranium,U,92,238.02900000000002,
Neptunium,Np,93,237.0,
Plutonium,Pu,94,244.0,
Americium,Am,95,243.0,
Curium,Cm,96,247.0,
Berkelium,Bk,97,247.0,
Californium,Cf,98,251.0,
Einsteinium,Es,99,252.0,
Fermium,Fm,100,257.0,
Mendelevium,Md,101,258.0,
Nobelium,No,102,259.0,
Lawrencium,Lr,103,262.0,
Rutherfordium,Rf,104,261.0,
Dubnium,Db,105,262.0,
Seaborgium,Sg,106,266.0,
Bohrium,Bh,107,264.0,
Hassium,Hs,108,267.0,
Meitnerium,Mt,109,268.0,
Darmstadtium ,Ds ,110,271.0,
Roentgenium ,Rg ,111,272.0,
Copernicium ,Cn ,112,285.0,
Nihonium,Nh,113,284.0,
Flerovium,Fl,114,289.0,
Moscovium,Mc,115,288.0,
Livermorium,Lv,116,292.0,
Tennessine,Ts,117,295.0,
Oganesson,Og,118,294.0,"""

Names = [
    "Ghost",
    "Hydrogen",
    "Helium",
    "Lithium",
    "Beryllium",
    "Boron",
    "Carbon",
    "Nitrogen",
    "Oxygen",
    "Fluorine",
    "Neon",
    "Sodium",
    "Magnesium",
    "Aluminum",
    "Silicon",
    "Phosphorus",
    "Sulfur",
    "Chlorine",
    "Argon",
    "Potassium",
    "Calcium",
    "Scandium",
    "Titanium",
    "Vanadium",
    "Chromium",
    "Manganese",
    "Iron",
    "Cobalt",
    "Nickel",
    "Copper",
    "Zinc",
    "Gallium",
    "Germanium",
    "Arsenic",
    "Selenium",
    "Bromine",
    "Krypton",
    "Rubidium",
    "Strontium",
    "Yttrium",
    "Zirconium",
    "Niobium",
    "Molybdenum",
    "Technetium",
    "Ruthenium",
    "Rhodium",
    "Palladium",
    "Silver",
    "Cadmium",
    "Indium",
    "Tin",
    "Antimony",
    "Tellurium",
    "Iodine",
    "Xenon",
    "Cesium",
    "Barium",
    "Lanthanum",
    "Cerium",
    "Praseodymium",
    "Neodymium",
    "Promethium",
    "Samarium",
    "Europium",
    "Gadolinium",
    "Terbium",
    "Dysprosium",
    "Holmium",
    "Erbium",
    "Thulium",
    "Ytterbium",
    "Lutetium",
    "Hafnium",
    "Tantalum",
    "Wolfram",
    "Rhenium",
    "Osmium",
    "Iridium",
    "Platinum",
    "Gold",
    "Mercury",
    "Thallium",
    "Lead",
    "Bismuth",
    "Polonium",
    "Astatine",
    "Radon",
    "Francium",
    "Radium",
    "Actinium",
    "Thorium",
    "Protactinium",
    "Uranium",
    "Neptunium",
    "Plutonium",
    "Americium",
    "Curium",
    "Berkelium",
    "Californium",
    "Einsteinium",
    "Fermium",
    "Mendelevium",
    "Nobelium",
    "Lawrencium",
    "Rutherfordium",
    "Dubnium",
    "Seaborgium",
    "Bohrium",
    "Hassium",
    "Meitnerium",
    "Darmstadtium",
    "Roentgenium",
    "Copernicium",
    "Nihonium",
    "Flerovium",
    "Moscovium",
    "Livermorium",
    "Tennessine",
    "Oganesson",
]

Symbols=[
"X", # Ghost 
"H",
"He",
"Li",
"Be",
"B",
"C",
"N",
"O",
"F",
"Ne",
"Na",
"Mg",
"Al",
"Si",
"P",
"S",
"Cl",
"Ar",
"K",
"Ca",
"Sc",
"Ti",
"V",
"Cr",
"Mn",
"Fe",
"Co",
"Ni",
"Cu",
"Zn",
"Ga",
"Ge",
"As",
"Se",
"Br",
"Kr",
"Rb",
"Sr",
"Y",
"Zr",
"Nb",
"Mo",
"Tc",
"Ru",
"Rh",
"Pd",
"Ag",
"Cd",
"In",
"Sn",
"Sb",
"Te",
"I",
"Xe",
"Cs",
"Ba",
"La",
"Ce",
"Pr",
"Nd",
"Pm",
"Sm",
"Eu",
"Gd",
"Tb",
"Dy",
"Ho",
"Er",
"Tm",
"Yb",
"Lu",
"Hf",
"Ta",
"W",
"Re",
"Os",
"Ir",
"Pt",
"Au",
"Hg",
"Tl",
"Pb",
"Bi",
"Po",
"At",
"Rn",
"Fr",
"Ra",
"Ac",
"Th",
"Pa",
"U",
"Np",
"Pu",
"Am",
"Cm",
"Bk",
"Cf",
"Es",
"Fm",
"Md",
"No",
"Lr",
"Rf",
"Db",
"Sg",
"Bh",
"Hs",
"Mt",
"Ds",
"Rg",
"Cn",
"Nh",
"Fl",
"Mc",
"Lv",
"Ts",
"Og",
]

AtomicNumbers = [i for in range(119)]

AromicMasses = [
   None,
   1.008,
   4.003,
   6.941,
   9.012,
  10.811,
  12.011,
  14.007,
  15.999,
  18.998,
  20.180,
  22.990,
  24.305,
  26.982,
  28.086,
  30.974,
  32.065,
  35.453,
  39.948,
  39.098,
  40.078,
  44.956,
  47.867,
  50.942,
  51.996,
  54.938,
  55.845,
  58.933,
  58.693,
  63.546,
  65.380,
  69.723,
  72.640,
  74.922,
  78.960,
  79.904,
  83.798,
  85.468,
  87.620,
  88.906,
  91.224,
  92.906,
  95.960,
  98.000,
 101.070,
 102.906,
 106.420,
 107.868,
 112.411,
 114.818,
 118.710,
 121.760,
 127.600,
 126.904,
 131.293,
 132.905,
 137.327,
 138.905,
 140.116,
 140.908,
 144.242,
 145.000,
 150.360,
 151.964,
 157.250,
 158.925,
 162.500,
 164.930,
 167.259,
 168.934,
 173.054,
 174.967,
 178.490,
 180.948,
 183.840,
 186.207,
 190.230,
 192.217,
 195.084,
 196.967,
 200.590,
 204.383,
 207.200,
 208.980,
 210.000,
 210.000,
 222.000,
 223.000,
 226.000,
 227.000,
 232.038,
 231.036,
 238.029,
 237.000,
 244.000,
 243.000,
 247.000,
 247.000,
 251.000,
 252.000,
 257.000,
 258.000,
 259.000,
 262.000,
 261.000,
 262.000,
 266.000,
 264.000,
 267.000,
 268.000,
 271.000,
 272.000,
 285.000,
 284.000,
 289.000,
 288.000,
 292.000,
 295.000,
 294.000,
]

from io import StringIO 
from dataclasses import dataclass 
from functools import wraps
import numbers 

@dataclass 
class Entry: 
    element: str
    symbol: str
    atomic_mass: float 
    atomic_radius: float 


def guess_symbol(Str):
    symbol = Str.strip().title()[0:2]

    if symbol in Symbols:
        pass 
    elif symbol[0] in Symbols:
        symbol = symbol[0]
    else: 
        symbol = "X" 

    return symbol



def to_atomic_number(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        new_args = []
        for arg in args:
            if isinstance(arg,numbers.Integral) :
                arg = np.array(arg)
            elif isinstance(arg,str):
                symbol = guess_symbol(arg) 
                if symbol == "X":
                    raise ValueError(f"Can not guess element from '{arg}'")
                arg = Symbols.index(symbol) + 1
            new_args.append(arg)
        args = tuple(new_args)



    return wrapper




class PeriodicTable:
    def __init__(self):
        self.table = dict()
        self.read() 
        self.write()

    def read(self):
        with StringIO(periodic_table_txt) as FH:
            lines = FH.readlines()[1:]
            for line  in lines:
                keys = line.strip().split(',')
                element = keys[0]
                symbol = keys[1]
                atomic_number = int(keys[2])
                atomic_mass = float(keys[3])
                if keys[4].strip()=="":
                    atomic_radius = 2.0 
                else: 
                    atomic_radius = float(keys[4])

                self.table[atomic_number] = Entry(element,symbol,atomic_mass,atomic_radius)

    def write(self):
        atomic_numbers = sorted(self.table.keys())
        print(atomic_numbers)
        left = "{"
        right = "}"
        
        with open("pt.txt","w") as FH:
            FH.write("PTable = {\n")
            for atomic_number in atomic_numbers: 
                FH.write(f"    {atomic_number:<3d} : {left:1s}\n")
                FH.write(f"        'element' : '{self.table[atomic_number].element}',\n")
                FH.write(f"        'symbol' : '{self.table[atomic_number].symbol}',\n")
                FH.write(f"        'atomic_mass' : {self.table[atomic_number].atomic_mass:10.5f},\n")
                FH.write(f"        'atomic_radius' : {self.table[atomic_number].atomic_radius:5.2f},\n")
                FH.write(f"    {right:1s},\n\n")
            FH.write("}\n")



    def atomic_mass(self,key): 
        return self.table[key].atomic_mass




@to_atomic_number
def test(key):
    print(key)


pt = PeriodicTable()

# 
Strs = ["H1","NA+","CL3","H_1"," N3","Nx5","ch3",23,"1X"]

for Str in Strs:
    print(Str)
    test(Str)

    # for key, val in kwargs.items():
    #     if isinstance(val,numbers.Integral) :
    #         kwargs[key] = val 
    #     elif isinstance(val,str):
    #         symbol = guess_symbol(arg) 
    #         if symbol == "X":
    #             raise ValueError(f"Can not guess chemical identity from '{arg}'")
    #         val = Symbols.index(symbol) + 1
    #         kwargs[key] = val 

    # return func(*args, **kwargs)

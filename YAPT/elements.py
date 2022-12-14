import matplotlib.colors 

colors = {
    "H": {
        "vdw_radius": 1.20,
        "vesta_color": (1.00, 0.80, 0.80),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (1.00, 1.00, 1.00),
    },
    "He": {
        "vdw_radius": 1.43,
        "vesta_color": (0.99, 0.91, 0.81),
        "cpk_color": (1.00, 0.75, 0.80),
        "jmol_color": (0.85, 1.00, 1.00),
    },
    "Li": {
        "vdw_radius": 2.12,
        "vesta_color": (0.53, 0.88, 0.46),
        "cpk_color": (0.70, 0.13, 0.13),
        "jmol_color": (0.80, 0.50, 1.00),
    },
    "Be": {
        "vdw_radius": 1.98,
        "vesta_color": (0.37, 0.85, 0.48),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.76, 1.00, 0.00),
    },
    "B": {
        "vdw_radius": 1.91,
        "vesta_color": (0.12, 0.64, 0.06),
        "cpk_color": (0.00, 1.00, 0.00),
        "jmol_color": (1.00, 0.71, 0.71),
    },
    "C": {
        "vdw_radius": 1.77,
        "vesta_color": (0.50, 0.29, 0.16),
        "cpk_color": (0.78, 0.78, 0.78),
        "jmol_color": (0.56, 0.56, 0.56),
    },
    "N": {
        "vdw_radius": 1.66,
        "vesta_color": (0.69, 0.73, 0.90),
        "cpk_color": (0.56, 0.56, 1.00),
        "jmol_color": (0.19, 0.31, 0.97),
    },
    "O": {
        "vdw_radius": 1.50,
        "vesta_color": (1.00, 0.01, 0.00),
        "cpk_color": (0.94, 0.00, 0.00),
        "jmol_color": (1.00, 0.05, 0.05),
    },
    "F": {
        "vdw_radius": 1.46,
        "vesta_color": (0.69, 0.73, 0.90),
        "cpk_color": (0.85, 0.65, 0.12),
        "jmol_color": (0.56, 0.88, 0.31),
    },
    "Ne": {
        "vdw_radius": 1.58,
        "vesta_color": (1.00, 0.22, 0.71),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.70, 0.89, 0.96),
    },
    "Na": {
        "vdw_radius": 2.50,
        "vesta_color": (0.98, 0.87, 0.24),
        "cpk_color": (0.00, 0.00, 1.00),
        "jmol_color": (0.67, 0.36, 0.95),
    },
    "Mg": {
        "vdw_radius": 2.51,
        "vesta_color": (0.99, 0.48, 0.08),
        "cpk_color": (0.13, 0.55, 0.13),
        "jmol_color": (0.54, 1.00, 0.00),
    },
    "Al": {
        "vdw_radius": 2.25,
        "vesta_color": (0.51, 0.70, 0.84),
        "cpk_color": (0.50, 0.50, 0.56),
        "jmol_color": (0.75, 0.65, 0.65),
    },
    "Si": {
        "vdw_radius": 2.19,
        "vesta_color": (0.11, 0.23, 0.98),
        "cpk_color": (0.85, 0.65, 0.12),
        "jmol_color": (0.94, 0.78, 0.63),
    },
    "P": {
        "vdw_radius": 1.90,
        "vesta_color": (0.76, 0.61, 0.76),
        "cpk_color": (1.00, 0.65, 0.00),
        "jmol_color": (1.00, 0.50, 0.00),
    },
    "S": {
        "vdw_radius": 1.89,
        "vesta_color": (1.00, 0.98, 0.00),
        "cpk_color": (1.00, 0.78, 0.20),
        "jmol_color": (1.00, 1.00, 0.19),
    },
    "Cl": {
        "vdw_radius": 1.82,
        "vesta_color": (0.20, 0.99, 0.01),
        "cpk_color": (0.00, 1.00, 0.00),
        "jmol_color": (0.12, 0.94, 0.12),
    },
    "Ar": {
        "vdw_radius": 1.83,
        "vesta_color": (0.81, 1.00, 0.77),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.50, 0.82, 0.89),
    },
    "K": {
        "vdw_radius": 2.73,
        "vesta_color": (0.63, 0.13, 0.97),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.56, 0.25, 0.83),
    },
    "Ca": {
        "vdw_radius": 2.62,
        "vesta_color": (0.36, 0.59, 0.74),
        "cpk_color": (0.50, 0.50, 0.56),
        "jmol_color": (0.24, 1.00, 0.00),
    },
    "Sc": {
        "vdw_radius": 2.58,
        "vesta_color": (0.71, 0.39, 0.67),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.90, 0.90, 0.90),
    },
    "Ti": {
        "vdw_radius": 2.46,
        "vesta_color": (0.47, 0.79, 1.00),
        "cpk_color": (0.50, 0.50, 0.56),
        "jmol_color": (0.75, 0.76, 0.78),
    },
    "V": {
        "vdw_radius": 2.42,
        "vesta_color": (0.90, 0.10, 0.00),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.65, 0.65, 0.67),
    },
    "Cr": {
        "vdw_radius": 2.45,
        "vesta_color": (0.00, 0.00, 0.62),
        "cpk_color": (0.50, 0.50, 0.56),
        "jmol_color": (0.54, 0.60, 0.78),
    },
    "Mn": {
        "vdw_radius": 2.45,
        "vesta_color": (0.66, 0.03, 0.62),
        "cpk_color": (0.50, 0.50, 0.56),
        "jmol_color": (0.61, 0.48, 0.78),
    },
    "Fe": {
        "vdw_radius": 2.44,
        "vesta_color": (0.71, 0.45, 0.00),
        "cpk_color": (1.00, 0.65, 0.00),
        "jmol_color": (0.88, 0.40, 0.20),
    },
    "Co": {
        "vdw_radius": 2.40,
        "vesta_color": (0.00, 0.00, 0.69),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.94, 0.56, 0.63),
    },
    "Ni": {
        "vdw_radius": 2.40,
        "vesta_color": (0.72, 0.74, 0.74),
        "cpk_color": (0.65, 0.17, 0.17),
        "jmol_color": (0.31, 0.82, 0.31),
    },
    "Cu": {
        "vdw_radius": 2.38,
        "vesta_color": (0.13, 0.28, 0.87),
        "cpk_color": (0.65, 0.17, 0.17),
        "jmol_color": (0.78, 0.50, 0.20),
    },
    "Zn": {
        "vdw_radius": 2.39,
        "vesta_color": (0.56, 0.56, 0.51),
        "cpk_color": (0.65, 0.17, 0.17),
        "jmol_color": (0.49, 0.50, 0.69),
    },
    "Ga": {
        "vdw_radius": 2.32,
        "vesta_color": (0.62, 0.89, 0.45),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.76, 0.56, 0.56),
    },
    "Ge": {
        "vdw_radius": 2.29,
        "vesta_color": (0.50, 0.43, 0.65),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.40, 0.56, 0.56),
    },
    "As": {
        "vdw_radius": 1.88,
        "vesta_color": (0.46, 0.82, 0.34),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.74, 0.50, 0.89),
    },
    "Se": {
        "vdw_radius": 1.82,
        "vesta_color": (0.60, 0.94, 0.06),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (1.00, 0.63, 0.00),
    },
    "Br": {
        "vdw_radius": 1.86,
        "vesta_color": (0.50, 0.19, 0.01),
        "cpk_color": (0.65, 0.17, 0.17),
        "jmol_color": (0.65, 0.16, 0.16),
    },
    "Kr": {
        "vdw_radius": 2.25,
        "vesta_color": (0.98, 0.76, 0.95),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.36, 0.72, 0.82),
    },
    "Rb": {
        "vdw_radius": 3.21,
        "vesta_color": (1.00, 0.00, 0.60),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.44, 0.18, 0.69),
    },
    "Sr": {
        "vdw_radius": 2.84,
        "vesta_color": (0.00, 1.00, 0.15),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.00, 1.00, 0.00),
    },
    "Y": {
        "vdw_radius": 2.75,
        "vesta_color": (0.40, 0.60, 0.56),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.58, 1.00, 1.00),
    },
    "Zr": {
        "vdw_radius": 2.52,
        "vesta_color": (0.00, 1.00, 0.00),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.58, 0.88, 0.88),
    },
    "Nb": {
        "vdw_radius": 2.56,
        "vesta_color": (0.30, 0.70, 0.46),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.45, 0.76, 0.79),
    },
    "Mo": {
        "vdw_radius": 2.45,
        "vesta_color": (0.71, 0.53, 0.69),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.33, 0.71, 0.71),
    },
    "Tc": {
        "vdw_radius": 2.44,
        "vesta_color": (0.81, 0.69, 0.79),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.23, 0.62, 0.62),
    },
    "Ru": {
        "vdw_radius": 2.46,
        "vesta_color": (0.81, 0.72, 0.68),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.14, 0.56, 0.56),
    },
    "Rh": {
        "vdw_radius": 2.44,
        "vesta_color": (0.81, 0.82, 0.67),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.04, 0.49, 0.55),
    },
    "Pd": {
        "vdw_radius": 2.15,
        "vesta_color": (0.76, 0.77, 0.72),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.00, 0.41, 0.52),
    },
    "Ag": {
        "vdw_radius": 2.53,
        "vesta_color": (0.72, 0.74, 0.74),
        "cpk_color": (0.50, 0.50, 0.56),
        "jmol_color": (0.75, 0.75, 0.75),
    },
    "Cd": {
        "vdw_radius": 2.49,
        "vesta_color": (0.95, 0.12, 0.86),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (1.00, 0.85, 0.56),
    },
    "In": {
        "vdw_radius": 2.43,
        "vesta_color": (0.84, 0.50, 0.73),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.65, 0.46, 0.45),
    },
    "Sn": {
        "vdw_radius": 2.42,
        "vesta_color": (0.61, 0.56, 0.73),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.40, 0.50, 0.50),
    },
    "Sb": {
        "vdw_radius": 2.47,
        "vesta_color": (0.85, 0.51, 0.31),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.62, 0.39, 0.71),
    },
    "Te": {
        "vdw_radius": 1.99,
        "vesta_color": (0.68, 0.64, 0.32),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.83, 0.48, 0.00),
    },
    "I": {
        "vdw_radius": 2.04,
        "vesta_color": (0.56, 0.12, 0.54),
        "cpk_color": (0.63, 0.12, 0.94),
        "jmol_color": (0.58, 0.00, 0.58),
    },
    "Xe": {
        "vdw_radius": 2.06,
        "vesta_color": (0.61, 0.63, 0.97),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.26, 0.62, 0.69),
    },
    "Cs": {
        "vdw_radius": 3.48,
        "vesta_color": (0.06, 1.00, 0.73),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.34, 0.09, 0.56),
    },
    "Ba": {
        "vdw_radius": 3.03,
        "vesta_color": (0.12, 0.94, 0.18),
        "cpk_color": (1.00, 0.65, 0.00),
        "jmol_color": (0.00, 0.79, 0.00),
    },
    "La": {
        "vdw_radius": 2.98,
        "vesta_color": (0.35, 0.77, 0.29),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.44, 0.83, 1.00),
    },
    "Ce": {
        "vdw_radius": 2.88,
        "vesta_color": (0.82, 0.99, 0.02),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (1.00, 1.00, 0.78),
    },
    "Pr": {
        "vdw_radius": 2.92,
        "vesta_color": (0.99, 0.89, 0.02),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.85, 1.00, 0.78),
    },
    "Nd": {
        "vdw_radius": 2.95,
        "vesta_color": (0.99, 0.56, 0.03),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.78, 1.00, 0.78),
    },
    "Pm": {
        "vdw_radius": None,
        "vesta_color": (0.00, 0.00, 0.96),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.64, 1.00, 0.78),
    },
    "Sm": {
        "vdw_radius": 2.90,
        "vesta_color": (0.99, 0.02, 0.49),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.56, 1.00, 0.78),
    },
    "Eu": {
        "vdw_radius": 2.87,
        "vesta_color": (0.98, 0.03, 0.84),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.38, 1.00, 0.78),
    },
    "Gd": {
        "vdw_radius": 2.83,
        "vesta_color": (0.75, 0.01, 1.00),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.27, 1.00, 0.78),
    },
    "Tb": {
        "vdw_radius": 2.79,
        "vesta_color": (0.44, 0.02, 1.00),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.19, 1.00, 0.78),
    },
    "Dy": {
        "vdw_radius": 2.87,
        "vesta_color": (0.19, 0.02, 0.99),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.12, 1.00, 0.78),
    },
    "Ho": {
        "vdw_radius": 2.81,
        "vesta_color": (0.03, 0.26, 0.99),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.00, 1.00, 0.61),
    },
    "Er": {
        "vdw_radius": 2.83,
        "vesta_color": (0.29, 0.45, 0.23),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.00, 0.90, 0.46),
    },
    "Tm": {
        "vdw_radius": 2.79,
        "vesta_color": (0.00, 0.00, 0.88),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.00, 0.83, 0.32),
    },
    "Yb": {
        "vdw_radius": 2.80,
        "vesta_color": (0.15, 0.99, 0.96),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.00, 0.75, 0.22),
    },
    "Lu": {
        "vdw_radius": 2.74,
        "vesta_color": (0.15, 0.99, 0.71),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.00, 0.67, 0.14),
    },
    "Hf": {
        "vdw_radius": 2.63,
        "vesta_color": (0.71, 0.71, 0.35),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.30, 0.76, 1.00),
    },
    "Ta": {
        "vdw_radius": 2.53,
        "vesta_color": (0.72, 0.61, 0.34),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.30, 0.65, 1.00),
    },
    "W": {
        "vdw_radius": 2.57,
        "vesta_color": (0.56, 0.54, 0.50),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.13, 0.58, 0.84),
    },
    "Re": {
        "vdw_radius": 2.49,
        "vesta_color": (0.70, 0.69, 0.56),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.15, 0.49, 0.67),
    },
    "Os": {
        "vdw_radius": 2.48,
        "vesta_color": (0.79, 0.70, 0.47),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.15, 0.40, 0.59),
    },
    "Ir": {
        "vdw_radius": 2.41,
        "vesta_color": (0.79, 0.81, 0.45),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.09, 0.33, 0.53),
    },
    "Pt": {
        "vdw_radius": 2.29,
        "vesta_color": (0.80, 0.78, 0.75),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.82, 0.82, 0.88),
    },
    "Au": {
        "vdw_radius": 2.32,
        "vesta_color": (1.00, 0.70, 0.22),
        "cpk_color": (0.85, 0.65, 0.12),
        "jmol_color": (1.00, 0.82, 0.14),
    },
    "Hg": {
        "vdw_radius": 2.45,
        "vesta_color": (0.83, 0.72, 0.80),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.72, 0.72, 0.82),
    },
    "Tl": {
        "vdw_radius": 2.47,
        "vesta_color": (0.59, 0.54, 0.43),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.65, 0.33, 0.30),
    },
    "Pb": {
        "vdw_radius": 2.60,
        "vesta_color": (0.32, 0.33, 0.36),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.34, 0.35, 0.38),
    },
    "Bi": {
        "vdw_radius": 2.54,
        "vesta_color": (0.82, 0.19, 0.97),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.62, 0.31, 0.71),
    },
    "Po": {
        "vdw_radius": None,
        "vesta_color": (0.00, 0.00, 1.00),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.67, 0.36, 0.00),
    },
    "At": {
        "vdw_radius": None,
        "vesta_color": (0.00, 0.00, 1.00),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.46, 0.31, 0.27),
    },
    "Rn": {
        "vdw_radius": None,
        "vesta_color": (1.00, 1.00, 0.00),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.26, 0.51, 0.59),
    },
    "Fr": {
        "vdw_radius": None,
        "vesta_color": (0.00, 0.00, 0.00),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.26, 0.00, 0.40),
    },
    "Ra": {
        "vdw_radius": None,
        "vesta_color": (0.43, 0.67, 0.35),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.00, 0.49, 0.00),
    },
    "Ac": {
        "vdw_radius": 2.80,
        "vesta_color": (0.39, 0.62, 0.45),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.44, 0.67, 0.98),
    },
    "Th": {
        "vdw_radius": 2.93,
        "vesta_color": (0.15, 1.00, 0.47),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.00, 0.73, 1.00),
    },
    "Pa": {
        "vdw_radius": 2.88,
        "vesta_color": (0.16, 0.98, 0.21),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.00, 0.63, 1.00),
    },
    "U": {
        "vdw_radius": 2.71,
        "vesta_color": (0.48, 0.63, 0.67),
        "cpk_color": (1.00, 0.08, 0.58),
        "jmol_color": (0.00, 0.56, 1.00),
    },
    "Np": {
        "vdw_radius": 2.82,
        "vesta_color": (0.30, 0.30, 0.30),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.00, 0.50, 1.00),
    },
    "Pu": {
        "vdw_radius": 2.81,
        "vesta_color": (0.30, 0.30, 0.30),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.00, 0.42, 1.00),
    },
    "Am": {
        "vdw_radius": 2.83,
        "vesta_color": (0.30, 0.30, 0.30),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.33, 0.36, 0.95),
    },
    "Cm": {
        "vdw_radius": 3.05,
        "vesta_color": (1.00, 1.00, 1.00),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.47, 0.36, 0.89),
    },
    "Bk": {
        "vdw_radius": 3.40,
        "vesta_color": (1.00, 1.00, 1.00),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.54, 0.31, 0.89),
    },
    "Cf": {
        "vdw_radius": 3.05,
        "vesta_color": (1.00, 1.00, 1.00),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.63, 0.21, 0.83),
    },
    "Es": {
        "vdw_radius": 2.70,
        "vesta_color": (1.00, 1.00, 1.00),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.70, 0.12, 0.83),
    },
    "Fm": {
        "vdw_radius": None,
        "vesta_color": (1.00, 1.00, 1.00),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.70, 0.12, 0.73),
    },
    "Md": {
        "vdw_radius": None,
        "vesta_color": (1.00, 1.00, 1.00),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.70, 0.05, 0.65),
    },
    "No": {
        "vdw_radius": None,
        "vesta_color": (1.00, 1.00, 1.00),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.74, 0.05, 0.53),
    },
    "Lr": {
        "vdw_radius": None,
        "vesta_color": (1.00, 1.00, 1.00),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.78, 0.00, 0.40),
    },
    "Rf": {
        "vdw_radius": None,
        "vesta_color": (1.00, 1.00, 1.00),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.80, 0.00, 0.35),
    },
    "Db": {
        "vdw_radius": None,
        "vesta_color": (1.00, 1.00, 1.00),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.82, 0.00, 0.31),
    },
    "Sg": {
        "vdw_radius": None,
        "vesta_color": (1.00, 1.00, 1.00),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.85, 0.00, 0.27),
    },
    "Bh": {
        "vdw_radius": None,
        "vesta_color": (1.00, 1.00, 1.00),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.88, 0.00, 0.22),
    },
    "Hs": {
        "vdw_radius": None,
        "vesta_color": (1.00, 1.00, 1.00),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.90, 0.00, 0.18),
    },
    "Mt": {
        "vdw_radius": None,
        "vesta_color": (1.00, 1.00, 1.00),
        "cpk_color": (1.00, 1.00, 1.00),
        "jmol_color": (0.92, 0.00, 0.15),
    },
}


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




vesta_x_color = "#4c4c4c" 
print(f"vesta_hex_color = [")
for atomic_number,symbol in enumerate(Symbols):
    try:
        hex_color = matplotlib.colors.to_hex(colors[symbol]["vesta_color"])
    except:
        hex_color = vesta_x_color 

    print(f'    "{hex_color}", #{atomic_number}')

print("]")

cpk_x_color = "#4c4c4c" 
print(f"cpk_hex_color = [")
for atomic_number,symbol in enumerate(Symbols):
    try:
        hex_color = matplotlib.colors.to_hex(colors[symbol]["cpk_color"])
    except:
        hex_color = cpk_x_color 

    print(f'    "{hex_color}", #{atomic_number}')

print("]")

jmol_x_color = "#fa1691" 
print(f"jmol_hex_color = [")
for atomic_number,symbol in enumerate(Symbols):
    try:
        hex_color = matplotlib.colors.to_hex(colors[symbol]["jmol_color"])
    except:
        hex_color = jmol_x_color 

    print(f'    "{hex_color}", #{atomic_number}')

print("]")

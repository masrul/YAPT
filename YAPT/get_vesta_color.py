import matplotlib.colors 

with open("elements.ini", "r") as FH:
    lines = FH.readlines() 

    for line in lines:
        keys = line.strip().split()

        atomic_number = int(keys[0])
        r = float(keys[-3])
        g = float(keys[-2])
        b = float(keys[-1]) 

        hex_color = matplotlib.colors.to_hex([r,g,b]) 

        print(f'"{hex_color:s}", #{atomic_number}')
    
for atomic_number in range(97,119):
    print(f'"{hex_color:s}", #{atomic_number}')



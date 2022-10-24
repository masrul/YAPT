with open("d.txt",'r') as FH:
    lines = FH.readlines()

    for line in lines:
        keys = line.split(',') 

        print(f"{float(keys[3]):8.3f},")

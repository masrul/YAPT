from mendeleev import element 

# print("Names=[")
# for i in range(1,119):
#     print(f'    "{element(i).name:s}", #{i}')
# print("]")

# print("Symbols=[")
# for i in range(1,119):
#     print(f'    "{element(i).symbol:s}", #{i}')
# print("]")

# print("AtomicMasses=[")
# for i in range(1,119):
#     print(f'    {element(i).mass: .4f}, #{i}')
# print("]")

# print("vdw_radii_bondi=[")
# for i in range(1,119):
#     try: 
#         print(f'    {element(i).vdw_radius_bondi/100: .2f}, #{i}')
#     except: 
#         print(f'    None, #{i}')
# print("]")

# print("vdw_radii_bondi=[")
# for i in range(1,119):
#     try: 
#         print(f'    {element(i).vdw_radius_bondi/100: .2f}, #{i}')
#     except: 
#         print(f'    None, #{i}')
# print("]")


print("cpk_color=[")
for i in range(1,119):
    try:
        print(f'    "{element(i).cpk_color:s}", #{i}')
    except:
        print(f'    "#ffffff", #{i}')

print("]")



#%%
#Read the input
with open('input.txt') as file:
    module_mass=[int(line.strip()) for line in file]
file.close()
#%%
def get_fuel(mass):
    return int(mass/3)-2
total_fuel=0
for module in module_mass:
    fuel=get_fuel(module)
    total_fuel+=fuel
    while fuel>6:
        fuel=get_fuel(fuel)
        total_fuel+=fuel
print(total_fuel)


# %%

import math

def read_input(file):
    file = open(file, 'r')
    Lines = file.readlines()
    data = list()
    count = 0
    # Strips the newline character
    for line in Lines:
        data.append(int(line.strip()))
    return data

def calculate_req_fuel(mass):
    req_fuel= mass/3
    req_fuel = math.floor(req_fuel)-2
    return req_fuel

# Fuel required to launch a given module is based on its mass.
# Specifically, to find the fuel required for a module, take its mass,
# divide by three, round down, and subtract 2.
def sum_all_modules(modules_mass_list):
    sum_req_fuel=0
    for module_mass in modules_mass_list:
        sum_req_fuel+=fuel_req_for_fuel(module_mass)

    return sum_req_fuel

def fuel_req_for_fuel(module_mass):
    sum_req_fuel=0

    while(calculate_req_fuel(module_mass)>0):
        sum_req_fuel+=calculate_req_fuel(module_mass)
        module_mass=calculate_req_fuel(module_mass)

    return sum_req_fuel

print(sum_all_modules(read_input("data/day1.txt")))
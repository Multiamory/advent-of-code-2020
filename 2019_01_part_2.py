import math

def main():
    with open("2019_day01_input.txt", "r") as f:
        input_lines = f.read().splitlines()

    fuel_total = 0
    fuel_with_fuel_total = 0
    for module in input_lines:
        fuel_total += get_fuel_from_mass(module)
        fuel_with_fuel_total += get_fuel_from_mass_recursive(module)
    
    print("Initial Estimate:", fuel_total)
    print("Including Fuel:  ", fuel_with_fuel_total)

def get_fuel_from_mass(mass):
    mass = int(mass)
    res = math.floor(mass/3) - 2
    return res if res > 0 else 0

def get_fuel_from_mass_recursive(mass):
    mass = int(mass)
    total_mass = 0
    while mass > 0:
        mass = get_fuel_from_mass(mass)

        total_mass += mass
    return total_mass

if __name__ == "__main__":
    main()

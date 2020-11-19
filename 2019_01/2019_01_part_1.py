import math

def main():
    with open("2019_day01_input.txt", "r") as f:
        input_lines = f.read().splitlines()

    fuel_total = 0
    for module in input_lines:
        fuel_total += get_fuel_from_mass(module)
    
    print("Total fuel needed:", fuel_total)

def get_fuel_from_mass(mass):
    mass = int(mass)
    res = math.floor(mass/3) - 2
    return res if res > 0 else 0

if __name__ == "__main__":
    main()

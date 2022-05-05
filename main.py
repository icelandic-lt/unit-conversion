#!/usr/bin/env python3
import re
from utils import get_valid_numbers, get_field, load_numbers
from units import verb, distance_units, distance_convert_to


sentences = []
numbers_dict = load_numbers()
numbers_dict = load_numbers(file="dummy.tsv")


def generate_distance():
    """ """
    to_return = []
    for key, num in numbers_dict.items():
        f = key[1]
        for number in num:
            for unit, unit_from in distance_units.items():
                for unit_to, p in distance_convert_to.items():

                    if f in unit_from and unit_to not in unit_from.values():
                        # Hvað er/eru 100 metrar margir kilómetrar
                        s = f"Hvað {verb[f]} {number} {unit_from[f]} {p} {unit_to}?"
                        # Hvers margir/mörg metrar/fet eru í einum kílómetra
                        to_return.append(s)
                        print(s)
    return to_return


def main():

    distance = generate_distance()
    print(len(distance))


if __name__ == "__main__":
    main()

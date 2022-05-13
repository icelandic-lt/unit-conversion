#!/usr/bin/env python3
from ctypes.wintypes import PINT
import re
from traceback import print_tb
from utils import get_valid_numbers, get_field, load_numbers
from units import verb, distance_units_s1, distance_units_s2, distance_convert_to


sentences = []
# numbers_dict = load_numbers(file="dummy.tsv")
# numbers_dict = load_numbers(file="nums_1to122.tsv")

numbers_dict = load_numbers(file="generate_numbers/numbers.tsv")

# too bæta við hvað eru  margir metra í einum kílómetra?


def generate_distance_sentences():
    """ """
    to_return = []
    for (n, f), num in numbers_dict.items():
        for number in num:
            for unit, unit_from in distance_units_s1.items():
                for unit_to, p in distance_convert_to.items():

                    # This conditonal catches cases like "Hvað eru tuttugu og einir sentimetrar mörg fet?"
                    # print(n, f, int(str(n)[-1]) != 1, "_ft_" not in f)
                    if int(str(n)[-1]) != 1 or "_ft_" not in f:

                        if f in unit_from and unit_to not in unit_from.values():
                            # Hvað er/eru 100 metrar margir kilómetrar
                            s1 = (
                                f"Hvað {verb[f]} {number} {unit_from[f]} {p} {unit_to}?"
                            )
                            to_return.append([n, f, s1])

            for unit, unit_from in distance_units_s2.items():
                for unit_to, p in distance_convert_to.items():
                    if unit_to not in unit_from.values() and f in unit_from:
                        # This conditonal catches cases like "Hvað eru tuttugu og einir sentimetrar mörg fet?"
                        if int(str(n)[-1]) == 1 and "_ft_" not in f:
                            # Hvað er/eru 100 metrar margir kilómetrar
                            # s1 = f"Hvað {verb[f]} {number} {unit_from[f]} {p} {unit_to}?"
                            # Hvers margir/mörg metrar/fet eru í einum kílómetra
                            s2 = f"Hversu {p} {unit_to} eru í {number} {unit_from[f]}?"

                            to_return.append([n, f, s2])
                        if int(str(n)[-1]) != 1 and "_et_" not in f:
                            s2 = f"Hversu {p} {unit_to} eru í {number} {unit_from[f]}?"
                            to_return.append([n, f, s2])

    return to_return


def sanity_check(sentences):
    """
    Takes the lowest and highest number and checks if all numbers have been generated between that range
    """

    nums = [x[0] for x in sentences]
    highest = max(nums)
    lowest = min(nums)
    missing = set()
    for n in range(int(lowest), int(highest)):
        n = str(n)
        if n not in nums:
            missing.add(n)
    missing = sorted(missing)
    print(f"Range {lowest} - {highest}")
    if missing:
        print("Missing:\n{}".format("\n".join(missing)))
    else:
        print("OK")


def main():
    distance = generate_distance_sentences()
    with open("out.tsv", "w") as f_out:
        for line in distance:
            f_out.write(line[0] + "\t" + line[1] + "\t" + line[2] + "\n")
    sanity_check(distance)
    print(len(distance))


if __name__ == "__main__":
    main()

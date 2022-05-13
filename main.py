#!/usr/bin/env python3


from utils import load_numbers
from units import (
    verb,
    distance_units_s1,
    distance_units_s2,
    distance_units_s3,
    distance_convert_to,
    distance_convert_to_s3,
    volume_convert_to,
    volume_unit_s1,
)


sentences = []
# numbers_dict = load_numbers(file="dummy.tsv")
# numbers_dict = load_numbers(file="nums_1to122.tsv")

numbers_dict = load_numbers(file="generate_numbers/numbers.tsv")

# too bæta við hvað eru  margir metra í einum kílómetra?


def generate_sentances():
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
                    # pass
            for unit, unit_to in distance_units_s2.items():
                for unit_from, p in distance_convert_to.items():
                    if unit_from not in unit_to.values() and f in unit_to:
                        # This conditonal catches cases like "Hvað eru tuttugu og einir sentimetrar mörg fet?"
                        # if int(str(n)[-1]) == 1 and "_ft_" not in f:
                        if int(str(n)[-1]) != 1 or "_ft_" not in f:
                            # Hvers margir/mörg metrar/fet eru í einum kílómetra
                            s2 = f"Hversu {p} {unit_from} eru í {number} {unit_to[f]}?"

                            to_return.append([n, f, s2])
                        # if int(str(n)[-1]) != 1 and "_et_" not in f:
                        #     s2 = f"Hversu {p} {unit_from} eru í {number} {unit_to[f]}?"
                        #     to_return.append([n, f, s2])
            for unit, unit_from in distance_units_s3.items():
                for unit_to in distance_convert_to_s3:
                    if f in unit_from and unit_to not in unit_from.values():

                        if int(str(n)[-1]) != 1 or "_ft_" not in f:
                            # Breyttu 100 metrum í kílómetra
                            s3 = f"Breyttu {number} {unit_from[f]} í {unit_to}"
                        # if int(str(n)[-1]) != 1 and "_et_" not in f:
                        #     s3 = f"Breyttu {number} {unit_from[f]} í {unit_to}"
                        to_return.append([n, f, s3])

            for unit, unit_from in volume_unit_s1.items():
                for unit_to, p in volume_convert_to.items():
                    # This conditonal catches cases like "Hvað eru tuttugu og einir sentimetrar mörg fet?"
                    # print(n, f, int(str(n)[-1]) != 1, "_ft_" not in f)
                    if int(str(n)[-1]) != 1 or "_ft_" not in f:

                        if f in unit_from and unit_to not in unit_from.values():
                            # Hvað er/eru 10 lítrar margar 
                            s1 = (
                                f"Hvað {verb[f]} {number} {unit_from[f]} {p} {unit_to}?"
                            )
                            to_return.append([n, f, s1])

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
    sentences = generate_sentances()
    with open("out.tsv", "w") as f_out:
        for line in sentences:
            f_out.write(line[0] + "\t" + line[1] + "\t" + line[2] + "\n")
    sanity_check(sentences)
    print(len(sentences))


if __name__ == "__main__":
    main()

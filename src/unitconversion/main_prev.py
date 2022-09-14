#!/usr/bin/env python3
volume_unit_s1 = {
    "lítri": {
        "et_kk_nf": "lítri",
        "ft_kk_nf": "lítrar",
        "at_af": "lítrar",
    },
    "desilítri": {
        "et_kk_nf": "desilítri",
        "ft_kk_nf": "desilítrar",
        "at_af": "desilítrar",
    },
    "millilítri": {
        "et_kk_nf": "millilítri",
        "ft_kk_nf": "millilítrar",
        "at_af": "millilítrar",
    },
    "grömm": {
        "et_hk_nf": "gramm",
        "ft_hk_nf": "grömm",
        "at_af": "grömm",
    },
    "peli": {
        "et_kk_nf": "peli",
        "ft_kk_nf": "pelar",
    },
}


distance_convert_to = {
    "fet": "mörg",
    "tommur": "margar",
    "mílur": "margar",
    "millimetrar": "margir",
    "sentimetrar": "margir",
    "metrar": "margir",
    "kílómetrar": "margir",
}


distance_convert_to_s3 = [
    "fet",
    "tommur",
    "mílur",
    "millimetra",
    "sentimetra",
    "metra",
    "kílómetra",
]


distance_units_s1 = {
    "millimetri": {
        "et_kk_nf": "millimetri",
        "ft_kk_nf": "millimetrar",
        "at_af": "millimetrar",
        # "et_kk_þf": "millimetri", # Gefur það sama og et_kk_nf
    },
    "sentimetri": {
        "et_kk_nf": "sentimetri",
        "ft_kk_nf": "sentimetrar",
        "at_af": "sentimetrar",
    },
    "metri": {
        "et_kk_nf": "metri",
        "ft_kk_nf": "metrar",
        "at_af": "metrar",
    },
    "kílómetri": {
        "et_kk_nf": "kílómetri",
        "ft_kk_nf": "kílómetrar",
        "at_af": "kílómetrar",
    },
    "míla": {
        "et_kvk_nf": "míla",
        "ft_kvk_nf": "mílur",
        "at_af": "mílur",
    },
    "tomma": {
        "et_kvk_nf": "tomma",
        "ft_kvk_nf": "tommur",
        "at_af": "tommur",
    },
    "fet": {
        "et_hk_nf": "fet",
        "at_af": "fet",
    },
}
distance_units_s2 = {
    "millimetri": {
        "et_kk_þgf": "millimetra",
        "ft_kk_þgf": "millimetrum",
        "at_af": "millimetrum",
        "_": "millimetrar",
    },
    "sentimetri": {
        "et_kk_þgf": "sentimetra",
        "ft_kk_þgf": "sentimetrum",
        "at_af": "sentimetrum",
        "_": "sentimetrar",
    },
    "metri": {
        "et_kk_þgf": "metra",
        "ft_kk_þgf": "metrum",
        "at_af": "metrum",
        "_": "metrar",
    },
    "kílómetri": {
        "et_kk_þgf": "kílómetra",
        "ft_kk_þgf": "kílómetrum",
        "at_af": "kílómetrum",
        "_": "kílómetrar",
    },
    "míla": {
        "et_kvk_þgf": "mílu",
        "ft_kvk_þgf": "mílum",
        "at_af": "mílum",
        "_": "mílur",
    },
    "tomma": {
        "et_kvk_þgf": "tommu",
        "ft_kvk_þgf": "tommum",
        "at_af": "tommum",
        "_": "tommur",
    },
    "fet": {
        "et_hk_þgf": "feti",
        "ft_hk_þgf": "fetum",
        "at_af": "fetum",
        "_": "fet",
    },
}


distance_units_s3 = {
    "millimetri": {
        "et_kk_þgf": "millimetra",
        "ft_kk_þgf": "millimetrum",
        "at_af": "millimetrum",
        "_": "millimetrar",
    },
    "sentimetri": {
        "et_kk_þgf": "sentimetra",
        "ft_kk_þgf": "sentimetrum",
        "at_af": "sentimetrum",
        "_": "sentimetrar",
    },
    "metri": {
        "et_kk_þgf": "metra",
        "ft_kk_þgf": "metrum",
        "at_af": "metrum",
        "_": "metrar",
    },
    "kílómetri": {
        "et_kk_þgf": "kílómetra",
        "ft_kk_þgf": "kílómetrum",
        "at_af": "kílómetrum",
        "_": "kílómetrar",
    },
    "míla": {
        "et_kvk_þgf": "mílu",
        "ft_kvk_þgf": "mílum",
        "at_af": "mílum",
        "_": "mílur",
    },
    "tomma": {
        "et_kvk_þgf": "tommu",
        "ft_kvk_þgf": "tommum",
        "at_af": "tommum",
        "_": "tommur",
    },
    "fet": {
        "et_hk_þgf": "feti",
        "ft_hk_þgf": "fetum",
        "at_af": "fetum",
        "_": "fet",
    },
}

import logging, os, sys

from unitconversion.utils import (
    load_numbers,
    test_output_with_GreynirCorrect,
    sanity_check,
    save_to_file,
)

from unitconversion.sentences import *
from unitconversion.units import *


def generate_sentances_integers(n: int, f: str, number: str):
    """
    Takes in a dictionary of numbers and generates sentences using those numbers.
    numbers =[
        [34, "ft_hk_ef", "þrjátíu og fjögurra"],
        [34, "ft_hk_ef", "þrjátíu og fjögra"],
        [35, "at_af", "þrjátíu og fimm"],
        [36, "at_af", "þrjátíu og sex"],
        [37, "at_af", "þrjátíu og sjö"],
        [38, "at_af", "þrjátíu og átta"],
                        ...
    ]
    """

    to_return = set()
    logging.debug(f"n, f: {n,f}")
    logging.debug(f"Number: {number}")
    for unit, unit_from in distance_units_s1.items():
        logging.debug(f"  1: Unit_from {unit_from}")
        for unit_to, p in distance_convert_to.items():
            logging.debug(f"    1: unit_to, p:{unit_to, p}")
            # This conditonal catches cases like "Hvað eru tuttugu og einir sentimetrar mörg fet?"
            # print(n, f, int(str(n)[-1]) != 1, "ft_" not in f)

            if int(str(n)[-1]) != 1 or "ft_" not in f:
                logging.debug(f"      here")

                # This statement makes it so that the question never asked
                # for the distance of a unit in the same unit.
                # e.g Hvað eru einn komma tveir millimetrar margar millimetrar?
                if f in unit_from and unit_to not in unit_from.values():
                    # Hvað er/eru 100 metrar margir kilómetrar
                    s1 = f"Hvað {verb[f]} {number} {unit_from[f]} {p} {unit_to}?"
                    logging.debug(f"        1: Adding {[n, f, s1]}")

                    to_return.add((n, f, s1))

    for unit, unit_to in distance_units_s2.items():
        for unit_from, p in distance_convert_to.items():
            if unit_from not in unit_to.values() and f in unit_to:
                # This conditonal catches cases like "Hvað eru tuttugu og einir sentimetrar mörg fet?"
                # if int(str(n)[-1]) == 1 and "ft_" not in f:
                if int(str(n)[-1]) != 1 or "ft_" not in f:
                    # Hvers margir/mörg metrar/fet eru í einum kílómetra
                    s2 = f"Hversu {p} {unit_from} eru í {number} {unit_to[f]}?"

                    to_return.add((n, f, s2))
    for unit, unit_from in distance_units_s3.items():
        for unit_to in distance_convert_to_s3:
            if f in unit_from and unit_to not in unit_from.values():

                if int(str(n)[-1]) != 1 or "ft_" not in f:
                    # Breyttu 100 metrum í kílómetra
                    s3 = f"Breyttu {number} {unit_from[f]} í {unit_to}"
                    # if int(str(n)[-1]) != 1 and "_et_" not in f:
                    #     s3 = f"Breyttu {number} {unit_from[f]} í {unit_to}"
                    to_return.add((n, f, s3))

    for unit, unit_from in volume_unit_s1.items():
        for unit_to, p in volume_convert_to.items():
            # This conditonal catches cases like "Hvað eru tuttugu og einir sentimetrar mörg fet?"
            # print(n, f, int(str(n)[-1]) != 1, "ft_" not in f)
            if int(str(n)[-1]) != 1 or "ft_" not in f:

                # This statement makes it so that the question never asked
                # for the distance of a unit in the same unit.
                # e.g Hvað eru einn komma tveir millimetrar margar millimetrar?
                if f in unit_from and unit_to not in unit_from.values():

                    # Hvað er/eru 10 lítrar margar
                    s1 = f"Hvað {verb[f]} {number} {unit_from[f]} {p} {unit_to}?"
                    to_return.add((n, f, s1))

    return to_return


def generate_sentances_fractions(n: float, f: str, number: str):
    """
    Takes in a dictionary of numbers and generates sentences using those numbers.
    numbers ={
        [0.1, "et_kk_nf", "núll komma einn"],
        [0.1, "et_kk_þf", "núll komma einn"],
        [0.1, "et_kk_þgf", "núll komma einum"],
        [0.1, "et_kk_ef", "núll komma eins"],
        [0.1, "et_kvk_nf", "núll komma ein"],
                        ...
    }
    """
    to_return = []
    logging.debug(f"n, f: {n,f}")
    logging.debug(f"Number: {number}")
    for unit, unit_from in distance_units_s1.items():
        logging.debug(f"  1: Unit_from {unit_from}")
        for unit_to, p in distance_convert_to.items():
            logging.debug(f"    1: unit_to, p:{unit_to, p}")
            # This conditonal catches cases like "Hvað eru tuttugu og einir sentimetrar mörg fet?"
            logging.debug(f"      here")

            # This statement makes it so that the question never asked
            # for the distance of a unit in the same unit.
            # e.g Hvað eru einn komma tveir millimetrar margar millimetrar?
            if f in unit_from and unit_to not in unit_from.values():
                # Hvað er/eru 100 metrar margir kilómetrar
                s1 = f"Hvað {verb[f]} {number} {unit_from[f]} {p} {unit_to}?"
                logging.debug(f"        1: Adding {[n, f, s1]}")

                to_return.append([n, f, s1])

    for unit, unit_to in distance_units_s2.items():
        for unit_from, p in distance_convert_to.items():
            if unit_from not in unit_to.values() and f in unit_to:
                # This conditonal catches cases like "Hvað eru tuttugu og einir sentimetrar mörg fet?"
                # Hvers margir/mörg metrar/fet eru í einum kílómetra
                s2 = f"Hversu {p} {unit_from} eru í {number} {unit_to[f]}?"

                to_return.append([n, f, s2])

    for unit, unit_from in distance_units_s3.items():
        for unit_to in distance_convert_to_s3:
            if f in unit_from and unit_to not in unit_from.values():

                # Breyttu 100 metrum í kílómetra
                s3 = f"Breyttu {number} {unit_from[f]} í {unit_to}"
                # if int(str(n)[-1]) != 1 and "_et_" not in f:
                #     s3 = f"Breyttu {number} {unit_from[f]} í {unit_to}"
                to_return.append([n, f, s3])

    for unit, unit_from in volume_unit_s1.items():
        for unit_to, p in volume_convert_to.items():
            # This conditonal catches cases like "Hvað eru tuttugu og einir sentimetrar mörg fet?"

            # This statement makes it so that the question never asked
            # for the distance of a unit in the same unit.
            # e.g Hvað eru einn komma tveir millimetrar margar millimetrar?

            if f in unit_from and unit_to not in unit_from.values():

                # 1.8 et_kk_nf    Hvað er einn komma átta peli margir desilítrar?
                # print(n)

                if str(n).split(".")[1] == "1" and "ft_" not in f:
                    # Hvað er/eru 10 lítrar margar
                    s1 = f"Hvað {verb[f]} {number} {unit_from[f]} {p} {unit_to}?"
                    to_return.append([n, f, s1])

                if str(n).split(".")[1] > "1" and "et_kk_nf" not in f:
                    s1 = f"Hvað {verb_simple[f]} {number} {unit_from[f]} {p} {unit_to}?"
                    to_return.append([n, f, s1])
                # if n == "1.2":
                #     input()
    return to_return


def parallel_process(function, iterable, n_jobs=5):
    from multiprocessing.pool import Pool

    to_return = []
    with Pool(processes=n_jobs) as pool:
        res = pool.starmap(function, iterable)
        for line in res:
            if line:
                for chunk in line:
                    to_return.append(chunk)
    return to_return


if __name__ == "__main__":
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)15s()] %(message)s"
    logging.basicConfig(level=logging.WARNING, format=FORMAT)

    output_file = "output/sentences_test.tsv"

    nums = sys.argv[1]
    numbers = load_numbers(file=nums)

    # sentences = generate_sentances_fractions(1.9, "ft_hk_nf", "eitt komma níu")
    # sentences = generate_sentances_fractions(1.3, "ft_kk_nf", "einn komma þrír")

    # sentences = generate_sentances_fractions(1.4, "ft_kk_nf", "einn komma fjórir")
    # sentences = generate_sentances_integers(5, "at_af", "fimm")
    # print(sentences)
    # logging.info(f"Using {len(numbers)} numbers")
    # if "." in numbers[0][0]:
    #     logging.info(f"Generating fractions")
    #     sentences = parallel_process(generate_sentances_fractions, numbers)
    # else:
    #     logging.info(f"Generating initegers")
    #     sentences = parallel_process(generate_sentances_integers, numbers)

    for line in numbers:
        generate_sentances_integers(*line)

    # logging.info(f"Generated {len(sentences)} sentences")
    # save_to_file(sentences, output_file)

    # logging.info(f"Saved to {output_file}")
    # test_output_with_GreynirCorrect(sentences, output_file)
    # sanity_check(sentences)

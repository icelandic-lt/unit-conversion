#!/usr/bin/env python3


from cmath import pi
import logging, os, sys

from unitconversion.utils import (
    load_numbers,
    test_output_with_GreynirCorrect,
    sanity_check,
    save_to_file,
)

from unitconversion.sentences import *
from unitconversion.units import *


def mix(units: list) -> list:
    """
    Takes in a list of dicts containing the convertion units and creates
    a list of all combinations of units.  We ignore line were same unit is on
    both sides of the combination.
    """
    to_return = []
    for idx_from, line_from in enumerate(units):
        for idx_to, line_to in enumerate(units):
            if idx_from != idx_to:
                for conj_from, word_from in line_from.items():
                    for conj_to, word_to in line_to.items():
                        to_return.append([[conj_from, word_from], [conj_to, word_to]])
    return to_return


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

    to_return = []
    logging.debug(f"n, f: {n,f}")
    logging.debug(f"Number: {number}")

    if int(str(n)[-1]) != 1 or "ft_" not in f:
        for conj_word_from, conj_word_to in mix(weight_units):
            s = sentence_rule_1(
                f,
                number,
                conj_word_from,
                conj_word_to,
            )
            if s:
                to_return.append((n, f, s))
            # print(s)

        for conj_word_from, conj_word_to in mix(volume_units):
            s = sentence_rule_2(
                f,
                number,
                conj_word_from,
                conj_word_to,
            )
            if s:
                to_return.append((n, f, s))
            # print(s)

            s = sentence_rule_3(
                f,
                number,
                conj_word_from,
                conj_word_to,
            )
            if s:
                to_return.append((n, f, s))
            # print(s)

        for conj_word_from, conj_word_to in mix(distanace_units):
            s = sentence_rule_1(
                f,
                number,
                conj_word_from,
                conj_word_to,
            )
            if s:
                to_return.append((n, f, s))
            # print(s)

            s = sentence_rule_2(
                f,
                number,
                conj_word_from,
                conj_word_to,
            )
            # print(s)
            if s:
                to_return.append((n, f, s))

            s = sentence_rule_4(
                f,
                number,
                conj_word_from,
                conj_word_to,
            )
            # print(s)
            if s:
                to_return.append((n, f, s))

        for conj_word_from, conj_word_to in mix(currency_units):
            s = sentence_rule_1(
                f,
                number,
                conj_word_from,
                conj_word_to,
            )
            if s:
                to_return.append((n, f, s))
            # print(s)

            s = sentence_rule_2(
                f,
                number,
                conj_word_from,
                conj_word_to,
            )
            # print(s)
            if s:
                to_return.append((n, f, s))
            s = sentence_rule_6(
                f,
                number,
                conj_word_from,
                conj_word_to,
            )
            # print(s)
            if s:
                to_return.append((n, f, s))

            s = sentence_rule_7(
                f,
                number,
                conj_word_from,
                conj_word_to,
            )
            # print(s)
            if s:
                to_return.append((n, f, s))

        # This dosen't take in any number and will therefore
        # be adding the same sentences over and over to the set.
        # I should just run this once seperetaly from the rest
        # but as we are adding it to a set...
        # s = sentence_rule_8(conj_word_from, conj_word_to):
        #     # print(s)
        #     to_return.append(s)
        for conj_word_from, conj_word_to in mix(weight_units):
            s = sentence_rule_1(
                f,
                number,
                conj_word_from,
                conj_word_to,
            )
            if s:
                to_return.append((n, f, s))
            # print(s)

            s = sentence_rule_2(
                f,
                number,
                conj_word_from,
                conj_word_to,
            )
            if s:
                to_return.append((n, f, s))
            # print(s)

            s = sentence_rule_3(
                f,
                number,
                conj_word_from,
                conj_word_to,
            )
            if s:
                to_return.append((n, f, s))
            # print(s)

            s = sentence_rule_4(
                f,
                number,
                conj_word_from,
                conj_word_to,
            )
            if s:
                to_return.append((n, f, s))
            # print(s)

            s = sentence_rule_6(
                f,
                number,
                conj_word_from,
                conj_word_to,
            )
            if s:
                to_return.append((n, f, s))
            # print(s)

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

    output_file = "output/sentences_16sept.tsv"

    nums = sys.argv[1]
    # numbers = load_numbers(file=nums)

    # logging.info(f"Using {len(numbers)} numbers")
    # if "." in numbers[0][0]:
    #     logging.info(f"Generating fractions")
    #     sentences = parallel_process(generate_sentances_fractions, numbers)
    # else:
    #     logging.info(f"Generating integers")
    #     sentences = parallel_process(generate_sentances_integers, numbers)

    # logging.info(f"Generated {len(sentences)} sentences")
    # save_to_file(sentences, output_file)

    # for line in numbers:
    #     generate_sentances_integers(*line)

    # sentences = generate_sentances_fractions(1.9, "ft_hk_nf", "eitt komma níu")
    # sentences = generate_sentances_fractions(1.3, "ft_kk_nf", "einn komma þrír")

    # sentences = generate_sentances_fractions(1.4, "ft_kk_nf", "einn komma fjórir")
    # sentences = generate_sentances_integers(5, "at_af", "fimm")

    # test_output_with_GreynirCorrect(sentences, output_file)
    # sanity_check(sentences)

    # Generate formatted test data
    test_set = []
    for line in [
        # [1, "et_kk_nf", "einn"],
        [2, "ft_kvk_þgf", "tveim"],
        # [3, "ft_kk_þgf", "þremur"],
        # [5, "at_af", "fimm"],
    ]:
        test_set.append((line, generate_sentances_integers(*line)))
    for line in test_set:
        print(line)

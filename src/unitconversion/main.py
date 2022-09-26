#!/usr/bin/env python3


import logging, os, sys, random
import re
import copy
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
                for infl_from, word_from in line_from.items():
                    for infl_to, word_to in line_to.items():
                        to_return.append([[infl_from, word_from], [infl_to, word_to]])
    return to_return


def generate_sentences_integers(n: int, f: str, number: str):
    """
    Generates all possible sentences given the input number.
    """

    to_return = []
    logging.debug(f"n, f: {n,f}")
    logging.debug(f"Number: {number}")
    if int(str(n)[-1]) != 1 or "ft_" not in f:
        for infl_word_from, infl_word_to in (
            mix(volume_units) + mix(weight_units) + mix(distanace_units)
        ):
            s = Sentence_rule_1().get(
                f,
                number,
                infl_word_from,
                infl_word_to,
            )
            if s:
                to_return.append([n, f, s])

            s = Sentence_rule_2().get(
                f,
                number,
                infl_word_from,
                infl_word_to,
            )
            if s:
                to_return.append([n, f, s])

            s = Sentence_rule_3().get(
                f,
                number,
                infl_word_from,
                infl_word_to,
            )
            if s:
                to_return.append([n, f, s])

            s = Sentence_rule_4().get(
                f,
                number,
                infl_word_from,
                infl_word_to,
            )
            if s:
                to_return.append([n, f, s])

            s = Sentence_rule_5().get(
                f,
                number,
                infl_word_from,
                infl_word_to,
            )
            if s:
                to_return.append([n, f, s])

        for infl_word_from, infl_word_to in mix(currency_units):
            s = Sentence_rule_1().get(
                f,
                number,
                infl_word_from,
                infl_word_to,
            )
            if s:
                to_return.append([n, f, s])

            s = Sentence_rule_2().get(
                f,
                number,
                infl_word_from,
                infl_word_to,
            )
            if s:
                to_return.append([n, f, s])

            s = Sentence_rule_5().get(
                f,
                number,
                infl_word_from,
                infl_word_to,
            )
            if s:
                to_return.append([n, f, s])

            s = Sentence_rule_6().get(
                f,
                number,
                infl_word_from,
                infl_word_to,
            )
            if s:
                to_return.append([n, f, s])

        # This dosen't take in any number and will therefore
        # be adding the same sentences over and over to the set.
        # I should just run this once seperetaly from the rest
        # but as we are adding it to a set...
        # s = sentence_rule_7(infl_word_from, infl_word_to):
        #     # print(s)
        #     to_return.append(s)

        return to_return


def mix_valid_units(units: list) -> list:
    """
    Takes in a list of dicts containing the convertion units and creates
    a list of all combinations of units.  We ignore line were same unit is on
    both sides of the combination.
    """

    all_rules = [
        Sentence_rule_1,
        Sentence_rule_2,
        Sentence_rule_3,
        Sentence_rule_4,
        Sentence_rule_5,
        Sentence_rule_6,
    ]

    all_valid_rule_combos = set()

    for sentence_rule in all_rules:
        for rule_from in sentence_rule().get_rule_from:
            for rule_to in sentence_rule().get_rule_to:
                all_valid_rule_combos.add((rule_from, rule_to))

    to_return = []
    for idx_from, line_from in enumerate(units):
        for idx_to, line_to in enumerate(units):
            if idx_from != idx_to:
                for infl_from, word_from in line_from.items():
                    for infl_to, word_to in line_to.items():
                        if (infl_from, infl_to) in all_valid_rule_combos:
                            to_return.append(
                                [[infl_from, word_from], [infl_to, word_to]]
                            )
    return to_return


VALID_COMBOS = {
    "volume": mix_valid_units(volume_units),
    "weight": mix_valid_units(weight_units),
    "distanace": mix_valid_units(distanace_units),
    "currency": mix_valid_units(currency_units),
}


def generate_one_random_sentence(n: int, f: str, number: str):
    """
    Creates one sentence for the given number
    """
    if int(str(n)[-1]) != 1 or "ft_" not in f:
        random_unit = random.choice(list(units2sentences.keys()))
        random_sentence = random.choice(units2sentences[random_unit])

        s = None
        tmp_combos = copy.deepcopy(VALID_COMBOS[random_unit])
        random.shuffle(tmp_combos)
        for infl_word_from, infl_word_to in tmp_combos:

            s = random_sentence().get(
                f,
                number,
                infl_word_from,
                infl_word_to,
            )
            if s:
                break
        if s:
            return [n, f, s]


def parallel_process(function, iterable, n_jobs=5, output_file=None):
    from multiprocessing.pool import Pool
    import time

    start_time = time.time()

    if output_file:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        logging.info(f"Saving to file {output_file}")
        num_chunks = 100
        chunk_size = int(len(iterable) / num_chunks)
        list_chunked = [
            iterable[i : i + chunk_size] for i in range(0, len(iterable), chunk_size)
        ]

        with open(output_file, "w") as f_out:
            count = 0
            logging.info(f"Done {count}/{len(iterable)}")
            for idx, chunk in enumerate(list_chunked):
                with Pool(processes=n_jobs) as pool:
                    for c in pool.starmap(function, chunk):
                        if c:
                            f_out.write(str(c[0]) + "\t" + c[1] + "\t" + c[2] + "\n")
                count += len(chunk)
                elapsed_time = time.time() - start_time
                est = ((elapsed_time / (idx + 1)) * num_chunks) / 60
                logging.info(
                    f"Done {count}/{len(iterable)} - Elapsed times: {elapsed_time:.0f} sek - ETA: {est:.0f} min"
                )

        logging.info(f"Saved to {output_file}")
        num_s = len(open(output_file, "r").readlines())
        logging.info(f"Generated {num_s} sentences")

    else:
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
    logging.basicConfig(level=logging.INFO, format=FORMAT)

    output_file = "output/fractions.tsv"

    nums = sys.argv[1]
    numbers = load_numbers(file=nums)

    logging.info(f"Using {len(numbers)} numbers")

    parallel_process(
        generate_one_random_sentence, numbers, n_jobs=5, output_file=output_file
    )
    # sentences = parallel_process(generate_sentences_integers, numbers, n_jobs=5)
    # logging.info(f"Generated {len(sentences)} sentences")
    # save_to_file(sentences, output_file)

    # sentences = []
    # for line in numbers:
    #     sentences.append(generate_one_random_sentence(*line))
    # logging.info(f"Generated {len(sentences)} sentences")

###########

# test_output_with_GreynirCorrect(sentences, output_file)
# sanity_check(sentences)

# Generate formatted test data
# test_set = []
# for line in [
# [1, "et_kk_nf", "einn"],
# [2, "ft_kvk_þgf", "tveim"],
# [3, "ft_kk_þgf", "þremur"],
# [5, "at_af", "fimm"],
# ]:
#     test_set.append((line, sentence_rule_5(*line)))
# for line in test_set:
#     print(line)


# inflections_1_6 = [
#     "et_hk_nf",
#     "et_hk_þf",
#     "et_hk_þgf",
#     "et_kk_nf",
#     "et_kk_þf",
#     "et_kk_þgf",
#     "et_kvk_nf",
#     "et_kvk_þf",
#     "et_kvk_þgf",
#     "ft_hk_nf",
#     "ft_hk_þf",
#     "ft_hk_þgf",
#     "ft_kk_nf",
#     "ft_kk_þf",
#     "ft_kk_þgf",
#     "ft_kvk_nf",
#     "ft_kvk_þf",
#     "ft_kvk_þgf",
# ]
# for line in inflections_1_6:
#     check = set()
#     for x in distanace_units:
#         for y in x.keys():
#             check.add(y)
#     if line not in check:
#         print(line)

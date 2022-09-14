from unitconversion.units import (
    verb_simple,
    adj_many,
)


def currency_s1(f, number, conj_from, word_from, line_to):
    """
    The sentences are:
        hvað er eitt/einn/ein [hk/kk/kvk_et_nf] [mörg/margir/margar] [hk/kk/kvk_ft_nf]
        hvað eru tvö/tveir/tvö [hk/kk/kvk_ft_nf] [mörg/margir/margar] [hk/kk/kvk_ft_nf]
    """
    rule_from = set(
        [
            "et_kvk_nf",
            "et_hk_nf",
            "et_kk_nf",
            "ft_kvk_nf",
            "ft_hk_nf",
            "ft_kk_nf",
        ]
    )
    rule_to = set(
        [
            "ft_kvk_nf",
            "ft_hk_nf",
            "ft_kk_nf",
        ]
    )
    ftet_from = conj_from.split("_")[0]

    if conj_from in rule_from and (
        f == conj_from or (f == "at_af" and ftet_from == "ft")
    ):
        for conj_to, word_to in line_to.items():
            if conj_to in rule_to:
                yield f"Hvað {verb_simple[ftet_from]} {number} {word_from} {adj_many[conj_to]} {word_to}"


def currency_s2(f, number, conj_from, word_from, line_to):
    """
    The sentences are:
        hvað er eitt/einn/ein [hk/kk/kvk_et_nf] í [hk/kk/kvk_ft_þgf]
        hvað eru fimm/fimm/fimm [hk/kk/kvk_ft_nf] í [hk/kk/kvk_ft_þgf]
    """
    rule_from = set(
        [
            "et_kvk_nf",
            "et_hk_nf",
            "et_kk_nf",
            "ft_kvk_nf",
            "ft_hk_nf",
            "ft_kk_nf",
        ]
    )
    rule_to = set(
        [
            "ft_kvk_þgf",
            "ft_hk_þgf",
            "ft_kk_þgf",
        ]
    )

    ftet_from = conj_from.split("_")[0]

    if conj_from in rule_from and (
        f == conj_from or (f == "at_af" and ftet_from == "ft")
    ):
        for conj_to, word_to in line_to.items():
            if conj_to in rule_to:
                yield f"Hvað {verb_simple[ftet_from]} {number} {word_from} í {word_to}"


def currency_s3(f, number, conj_from, word_from, line_to):
    """
    The sentences are:
        hversu mörg/marga/margar [hk/kk/kvk_ft_þf] fæ ég fyrir eitt/einn/ein [hk/kk/kvk_et_þf]
        hversu mörg/marga/margar [hk/kk/kvk_ft_þf] fæ ég fyrir tvö/tvo/tvær[hk/kk/kvk_ft_þf]
    """
    rule_from = set(
        [
            "et_kvk_þf",
            "et_hk_þf",
            "et_kk_þf",
            "ft_kvk_þf",
            "ft_hk_þf",
            "ft_kk_þf",
        ]
    )
    rule_to = set(
        [
            "ft_kvk_þf",
            "ft_hk_þf",
            "ft_kk_þf",
        ]
    )

    ftet_from = conj_from.split("_")[0]

    if conj_from in rule_from and (
        f == conj_from or (f == "at_af" and ftet_from == "ft")
    ):
        for conj_to, word_to in line_to.items():
            if conj_to in rule_to:
                yield f"Hversu {adj_many[conj_to]} {word_to} fæ ég fyrir {number} {word_from}"


def currency_s4(conj_from, word_from, line_to):
    """
    The sentences are:
        hvert er gengið á [hk/kk/kvk_et_þgf_mg] gagnvart[hk/kk/kvk_et_þgf_mg]
    """
    rule = set(
        [
            "et_kvk_þf",
            "et_hk_þf",
            "et_kk_þf",
            "ft_kvk_þf",
            "ft_hk_þf",
            "ft_kk_þf",
        ]
    )
    ftet_from = conj_from.split("_")[0]

    if conj_from in rule:
        for conj_to, word_to in line_to.items():
            if conj_to in rule:
                s = f"Hvert {verb_simple[ftet_from]} gengið á {word_from} gagnvart {word_to}"


def distance_s1(f, number, conj_from, word_from, line_to):
    """
    The sentences are:
        Breyttu einum/einni/einu [hk/kk/kvk_et_þgf] í [hk/kk/kvk_ft_þf]
        Breyttu tveimur/tveim/tveim [hk/kk/kvk_ft_þgf] í [hk/kk/kvk_ft_þf]
    """
    rule_from = set(
        [
            "et_kvk_þgf",
            "et_hk_þgf",
            "et_kk_þgf",
            "ft_kvk_þgf",
            "ft_hk_þgf",
            "ft_kk_þgf",
        ]
    )
    rule_to = set(
        [
            "ft_kvk_þf",
            "ft_hk_þf",
            "ft_kk_þf",
        ]
    )

    ftet_from = conj_from.split("_")[0]

    if conj_from in rule_from and (
        f == conj_from or (f == "at_af" and ftet_from == "ft")
    ):
        for conj_to, word_to in line_to.items():
            if conj_to in rule_to:
                yield f"Breyttu {number} {word_from} í {word_to}"


def sentence_rule_1(f, number, conj_word_from, conj_word_to):
    """
    The sentences are:
        Breyttu einum/einni/einu [hk/kk/kvk_et_þgf] í [hk/kk/kvk_ft_þf]
        Breyttu tveimur/tveim/tveim [hk/kk/kvk_ft_þgf] í [hk/kk/kvk_ft_þf]
    """
    rule_from = set(
        [
            "et_kvk_þgf",
            "et_hk_þgf",
            "et_kk_þgf",
            "ft_kvk_þgf",
            "ft_hk_þgf",
            "ft_kk_þgf",
        ]
    )
    rule_to = set(
        [
            "ft_kvk_þf",
            "ft_hk_þf",
            "ft_kk_þf",
        ]
    )

    ftet_from = conj_word_from[0].split("_")[0]

    if conj_word_from[0] in rule_from and (
        f == conj_word_from[0]
        or (f == "at_af" and ftet_from == "ft")
        and (conj_word_to[0] in rule_to)
    ):
        yield f"Breyttu {number} {conj_word_from[1]} í {conj_word_to[1]}"


def distance_s2(f, number, conj_from, word_from, line_to):
    """
    The sentences are:
        Hvers mörg/marga/margar [hk/kk/kvk_ft_nf] eru í einum/einni/einu [hk/kk/kvk_et_þgf]
        Hvers mörg/marga/margar [hk/kk/kvk_ft_nf] eru í tveimur/tveim/tveim [hk/kk/kvk_ft_þgf]

    """
    rule_to = set(
        [
            "ft_kvk_nf",
            "ft_hk_nf",
            "ft_kk_nf",
        ]
    )
    rule_from = set(
        [
            "et_kvk_þgf",
            "et_hk_þgf",
            "et_kk_þgf",
            "ft_kvk_þgf",
            "ft_hk_þgf",
            "ft_kk_þgf",
        ]
    )

    ftet_from = conj_from.split("_")[0]

    if conj_from in rule_from and (
        f == conj_from or (f == "at_af" and ftet_from == "ft")
    ):
        for conj_to, word_to in line_to.items():
            if conj_to in rule_to:
                yield f"Hversu {adj_many[conj_to]} {word_to} eru í {number} {word_from}"


def distance_s3(f, number, conj_from, word_from, line_to):
    """
    The sentences are:
        Hvað er einn/ein/eitt [hk/kk/kvk_et_nf] mörg/marga/margar [hk/kk/kvk_ft_nf]
        Hvað eru tveir/tvær/tvö [hk/kk/kvk_ft_nf] mörg/marga/margar [hk/kk/kvk_ft_nf]
    """
    rule_from = set(
        [
            "et_kvk_nf",
            "et_hk_nf",
            "et_kk_nf",
            "ft_kvk_nf",
            "ft_hk_nf",
            "ft_kk_nf",
        ]
    )
    rule_to = set(
        [
            "ft_kvk_nf",
            "ft_hk_nf",
            "ft_kk_nf",
        ]
    )

    ftet_from = conj_from.split("_")[0]

    if conj_from in rule_from and (
        f == conj_from or (f == "at_af" and ftet_from == "ft")
    ):
        for conj_to, word_to in line_to.items():
            if conj_to in rule_to:
                yield f"Hvað {verb_simple[ftet_from]} {number} {word_from} {adj_many[conj_to]} {word_to}"


def volume_s1(f, number, conj_from, word_from, line_to):
    """
    The sentences are:
        Hvað er einn/ein/eitt [hk/kk/kvk_et_nf] mörg/marga/margar [hk/kk/kvk_ft_nf]
        Hvað eru tveir/tvær/tvö [hk/kk/kvk_ft_nf] mörg/marga/margar [hk/kk/kvk_ft_nf]
    """
    rule_from = set(
        [
            "et_kvk_nf",
            "et_hk_nf",
            "et_kk_nf",
            "ft_kvk_nf",
            "ft_hk_nf",
            "ft_kk_nf",
        ]
    )
    rule_to = set(
        [
            "ft_kvk_nf",
            "ft_hk_nf",
            "ft_kk_nf",
        ]
    )

    ftet_from = conj_from.split("_")[0]

    if conj_from in rule_from and (
        f == conj_from or (f == "at_af" and ftet_from == "ft")
    ):
        for conj_to, word_to in line_to.items():
            if conj_to in rule_to:
                yield f"Hvað {verb_simple[ftet_from]} {number} {word_from} {adj_many[conj_to]} {word_to}"


def volume_s2(f, number, conj_from, word_from, line_to):
    """
    The sentences are:
        Hvað eru mörg/margir/margar [hk/kk/kvk_ft_nf] í einum/einni/einu [hk/kk/kvk_et_þgf]
        Hvað eru mörg/margir/margar [hk/kk/kvk_ft_nf] í tveimur/tveim/tveim [hk/kk/kvk_ff_þgf]
    """
    rule_to = set(
        [
            "ft_kvk_nf",
            "ft_hk_nf",
            "ft_kk_nf",
        ]
    )
    rule_from = set(
        [
            "et_kvk_þgf",
            "et_hk_þgf",
            "et_kk_þgf",
            "ft_kvk_þgf",
            "ft_hk_þgf",
            "ft_kk_þgf",
        ]
    )

    ftet_from = conj_from.split("_")[0]

    if conj_from in rule_from and (
        f == conj_from or (f == "at_af" and ftet_from == "ft")
    ):
        for conj_to, word_to in line_to.items():
            if conj_to in rule_to:
                yield f"Hvað {verb_simple[ftet_from]} {adj_many[conj_to]} {word_to} í {number} {word_from}"

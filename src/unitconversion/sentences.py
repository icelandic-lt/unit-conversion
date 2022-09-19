from unitconversion.units import (
    verb_simple,
    adj_many,
)


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

    if (
        conj_word_from[0] in rule_from
        and (f == conj_word_from[0] or (f == "at_af" and ftet_from == "ft"))
        and (conj_word_to[0] in rule_to)
    ):
        return f"Breyttu {number} {conj_word_from[1]} í {conj_word_to[1]}"


def sentence_rule_2(f, number, conj_word_from, conj_word_to):
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

    ftet_from = conj_word_from[0].split("_")[0]

    if (
        (conj_word_from[0] in rule_from)
        and (f == conj_word_from[0] or (f == "at_af" and ftet_from == "ft"))
        and (conj_word_to[0] in rule_to)
    ):
        return f"Hvað {verb_simple[ftet_from]} {number} {conj_word_from[1]} {adj_many[conj_word_to[0]]} {conj_word_to[1]}"


def sentence_rule_3(f, number, conj_word_from, conj_word_to):
    """
    The sentences are:
        Hvað eru mörg/margir/margar [hk/kk/kvk_ft_nf] í einum/einni/einu [hk/kk/kvk_et_þgf]
        Hvað eru mörg/margir/margar [hk/kk/kvk_ft_nf] í tveimur/tveim/tveim [hk/kk/kvk_ft_þgf]
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

    ftet_from = conj_word_from[0].split("_")[0]

    if (
        (conj_word_from[0] in rule_from)
        and (f == conj_word_from[0] or (f == "at_af" and ftet_from == "ft"))
        and (conj_word_to[0] in rule_to)
    ):
        return f"Hvað {verb_simple[ftet_from]} {adj_many[conj_word_to[0]]} {conj_word_to[1]} í {number} {conj_word_from[1]}"


def sentence_rule_4(f, number, conj_word_from, conj_word_to):
    """
    The sentences are:
        Hversu mörg/marga/margar [hk/kk/kvk_ft_nf] eru í einum/einni/einu [hk/kk/kvk_et_þgf]
        Hversu mörg/marga/margar [hk/kk/kvk_ft_nf] eru í tveimur/tveim/tveim [hk/kk/kvk_ft_þgf]

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

    ftet_from = conj_word_from[0].split("_")[0]

    if (
        (conj_word_from[0] in rule_from)
        and (f == conj_word_from[0] or (f == "at_af" and ftet_from == "ft"))
        and (conj_word_to[0] in rule_to)
    ):
        return f"Hversu {adj_many[conj_word_to[0]]} {conj_word_to[1]} eru í {number} {conj_word_from[1]}"


def sentence_rule_6(f, number, conj_word_from, conj_word_to):
    """
    The sentences are:
        Hvað er eitt/einn/ein [hk/kk/kvk_et_nf] í [hk/kk/kvk_ft_þgf]
        Hvað eru fimm/fimm/fimm [hk/kk/kvk_ft_nf] í [hk/kk/kvk_ft_þgf]
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

    ftet_from = conj_word_from[0].split("_")[0]

    if (
        (conj_word_from[0] in rule_from)
        and (f == conj_word_from[0] or (f == "at_af" and ftet_from == "ft"))
        and (conj_word_to[0] in rule_to)
    ):
        return f"Hvað {verb_simple[ftet_from]} {number} {conj_word_from[1]} í {conj_word_to[1]}"


def sentence_rule_7(f, number, conj_word_from, conj_word_to):
    """
    The sentences are:
        Hversu mörg/marga/margar [hk/kk/kvk_ft_þf] fæ ég fyrir eitt/einn/ein [hk/kk/kvk_et_þf]
        Hversu mörg/marga/margar [hk/kk/kvk_ft_þf] fæ ég fyrir tvö/tvo/tvær[hk/kk/kvk_ft_þf]
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
    ftet_from = conj_word_from[0].split("_")[0]

    if (
        (conj_word_from[0] in rule_from)
        and (f == conj_word_from[0] or (f == "at_af" and ftet_from == "ft"))
        and (conj_word_to[0] in rule_to)
    ):
        return f"Hversu {adj_many[conj_word_to[0]]} {conj_word_to[1]} fæ ég fyrir {number} {conj_word_from[1]}"


def sentence_rule_8(conj_word_from, conj_word_to):
    """
    The sentences are:
        Hvert er gengið á [hk/kk/kvk_et_þgf_gr] gagnvart [hk/kk/kvk_et_þgf_gr]
    """
    rule = set(
        [
            "et_kvk_þgf_gr",
            "et_hk_þgf_gr",
            "et_kk_þgf_gr",
            "ft_kvk_þgf_gr",
            "ft_hk_þgf_gr",
            "ft_kk_þgf_gr",
        ]
    )
    ftet_from = conj_word_from[0].split("_")[0]

    if (conj_word_from[0] in rule) and (conj_word_to[0] in rule):

        return f"Hvert {verb_simple[ftet_from]} gengið á {conj_word_from[1]} gagnvart {conj_word_to[1]}"

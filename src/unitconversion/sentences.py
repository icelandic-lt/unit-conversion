from mimetypes import init
from unitconversion.units import (
    verb_simple,
    adj_many,
)


class Base:
    @property
    def get_rule_from(self):
        return list(self.rule_from)

    @property
    def get_rule_to(self):
        return list(self.rule_to)


class Sentence_rule_1(Base):
    """
    The sentences are:
        Breyttu einum/einni/einu [hk/kk/kvk_et_þgf] í [hk/kk/kvk_ft_þf]
        Breyttu tveimur/tveim/tveim [hk/kk/kvk_ft_þgf] í [hk/kk/kvk_ft_þf]
    """

    def __init__(self):
        self.rule_from = set(
            [
                "et_kvk_þgf",
                "et_hk_þgf",
                "et_kk_þgf",
                "ft_kvk_þgf",
                "ft_hk_þgf",
                "ft_kk_þgf",
            ]
        )

        self.rule_to = set(
            [
                "ft_kvk_þf",
                "ft_hk_þf",
                "ft_kk_þf",
            ]
        )

    def get(self, f, number, infl_word_from, infl_word_to):
        ftet_from = infl_word_from[0].split("_")[0]

        if (
            infl_word_from[0] in self.rule_from
            and (f == infl_word_from[0] or (f == "at_af" and ftet_from == "ft"))
            and (infl_word_to[0] in self.rule_to)
        ):
            return f"Breyttu {number} {infl_word_from[1]} í {infl_word_to[1]}"


class Sentence_rule_2(Base):
    """
    The sentences are:
        Hvað er einn/ein/eitt [hk/kk/kvk_et_nf] mörg/marga/margar [hk/kk/kvk_ft_nf]
        Hvað eru tveir/tvær/tvö [hk/kk/kvk_ft_nf] mörg/marga/margar [hk/kk/kvk_ft_nf]
    """

    def __init__(self):

        self.rule_from = set(
            [
                "et_kvk_nf",
                "et_hk_nf",
                "et_kk_nf",
                "ft_kvk_nf",
                "ft_hk_nf",
                "ft_kk_nf",
            ]
        )
        self.rule_to = set(
            [
                "ft_kvk_nf",
                "ft_hk_nf",
                "ft_kk_nf",
            ]
        )

    def get(self, f, number, infl_word_from, infl_word_to):

        ftet_from = infl_word_from[0].split("_")[0]

        if (
            (infl_word_from[0] in self.rule_from)
            and (f == infl_word_from[0] or (f == "at_af" and ftet_from == "ft"))
            and (infl_word_to[0] in self.rule_to)
        ):
            return f"Hvað {verb_simple[ftet_from]} {number} {infl_word_from[1]} {adj_many[infl_word_to[0]]} {infl_word_to[1]}"


class Sentence_rule_3(Base):
    """
    The sentences are:
        Hvað eru mörg/margir/margar [hk/kk/kvk_ft_nf] í einum/einni/einu [hk/kk/kvk_et_þgf]
        Hvað eru mörg/margir/margar [hk/kk/kvk_ft_nf] í tveimur/tveim/tveim [hk/kk/kvk_ft_þgf]
    """

    def __init__(self):

        self.rule_from = set(
            [
                "et_kvk_þgf",
                "et_hk_þgf",
                "et_kk_þgf",
                "ft_kvk_þgf",
                "ft_hk_þgf",
                "ft_kk_þgf",
            ]
        )
        self.rule_to = set(
            [
                "ft_kvk_nf",
                "ft_hk_nf",
                "ft_kk_nf",
            ]
        )

    def get(self, f, number, infl_word_from, infl_word_to):

        ftet_from = infl_word_to[0].split("_")[0]

        if (
            (infl_word_from[0] in self.rule_from)
            and (f == infl_word_from[0] or (f == "at_af" and ftet_from == "ft"))
            and (infl_word_to[0] in self.rule_to)
        ):
            # print(
            #     ftet_from, infl_word_to[0], infl_word_to[1], number, infl_word_from[1]
            # )
            # print(
            #     f"Hvað {verb_simple[ftet_from]} {adj_many[infl_word_to[0]]} {infl_word_to[1]} í {number} {infl_word_from[1]}"
            # )
            return f"Hvað {verb_simple[ftet_from]} {adj_many[infl_word_to[0]]} {infl_word_to[1]} í {number} {infl_word_from[1]}"


class Sentence_rule_4(Base):
    """
    The sentences are:
        Hversu mörg/margir/margar [hk/kk/kvk_ft_nf] eru í einum/einni/einu [hk/kk/kvk_et_þgf]
        Hversu mörg/margir/margar [hk/kk/kvk_ft_nf] eru í tveimur/tveim/tveim [hk/kk/kvk_ft_þgf]

    """

    def __init__(self):

        self.rule_to = set(
            [
                "ft_kvk_nf",
                "ft_hk_nf",
                "ft_kk_nf",
            ]
        )
        self.rule_from = set(
            [
                "et_kvk_þgf",
                "et_hk_þgf",
                "et_kk_þgf",
                "ft_kvk_þgf",
                "ft_hk_þgf",
                "ft_kk_þgf",
            ]
        )

    def get(self, f, number, infl_word_from, infl_word_to):

        ftet_from = infl_word_from[0].split("_")[0]

        if (
            (infl_word_from[0] in self.rule_from)
            and (f == infl_word_from[0] or (f == "at_af" and ftet_from == "ft"))
            and (infl_word_to[0] in self.rule_to)
        ):
            return f"Hversu {adj_many[infl_word_to[0]]} {infl_word_to[1]} eru í {number} {infl_word_from[1]}"


class Sentence_rule_5(Base):
    """
    The sentences are:
        Hvað er eitt/einn/ein [hk/kk/kvk_et_nf] í [hk/kk/kvk_ft_þgf]
        Hvað eru fimm/fimm/fimm [hk/kk/kvk_ft_nf] í [hk/kk/kvk_ft_þgf]
    """

    def __init__(self):

        self.rule_from = set(
            [
                "et_kvk_nf",
                "et_hk_nf",
                "et_kk_nf",
                "ft_kvk_nf",
                "ft_hk_nf",
                "ft_kk_nf",
            ]
        )
        self.rule_to = set(
            [
                "ft_kvk_þgf",
                "ft_hk_þgf",
                "ft_kk_þgf",
            ]
        )

    def get(self, f, number, infl_word_from, infl_word_to):

        ftet_from = infl_word_from[0].split("_")[0]

        if (
            (infl_word_from[0] in self.rule_from)
            and (f == infl_word_from[0] or (f == "at_af" and ftet_from == "ft"))
            and (infl_word_to[0] in self.rule_to)
        ):
            return f"Hvað {verb_simple[ftet_from]} {number} {infl_word_from[1]} í {infl_word_to[1]}"


class Sentence_rule_6(Base):
    """
    The sentences are:
        Hversu mörg/marga/margar [hk/kk/kvk_ft_þf] fæ ég fyrir eitt/einn/ein [hk/kk/kvk_et_þf]
        Hversu mörg/marga/margar [hk/kk/kvk_ft_þf] fæ ég fyrir tvö/tvo/tvær[hk/kk/kvk_ft_þf]
    """

    def __init__(self):

        self.rule_from = set(
            [
                "et_kvk_þf",
                "et_hk_þf",
                "et_kk_þf",
                "ft_kvk_þf",
                "ft_hk_þf",
                "ft_kk_þf",
            ]
        )
        self.rule_to = set(
            [
                "ft_kvk_þf",
                "ft_hk_þf",
                "ft_kk_þf",
            ]
        )

    def get(self, f, number, infl_word_from, infl_word_to):

        ftet_from = infl_word_from[0].split("_")[0]

        if (
            (infl_word_from[0] in self.rule_from)
            and (f == infl_word_from[0] or (f == "at_af" and ftet_from == "ft"))
            and (infl_word_to[0] in self.rule_to)
        ):
            return f"Hversu {adj_many[infl_word_to[0]]} {infl_word_to[1]} fæ ég fyrir {number} {infl_word_from[1]}"


class Sentence_rule_7(Base):
    """
    The sentences are:
        Hvert er gengið á [hk/kk/kvk_et_þgf_gr] gagnvart [hk/kk/kvk_et_þgf_gr]
    """

    def __init__(self):

        self.rule = set(
            [
                "et_kvk_þgf_gr",
                "et_hk_þgf_gr",
                "et_kk_þgf_gr",
                "ft_kvk_þgf_gr",
                "ft_hk_þgf_gr",
                "ft_kk_þgf_gr",
            ]
        )

    def get(self, infl_word_from, infl_word_to):

        ftet_from = infl_word_from[0].split("_")[0]

        if (infl_word_from[0] in self.rule) and (infl_word_to[0] in self.rule):

            return f"Hvert {verb_simple[ftet_from]} gengið á {infl_word_from[1]} gagnvart {infl_word_to[1]}"


units2sentences = {
    "volume": [
        Sentence_rule_1,
        Sentence_rule_2,
        Sentence_rule_3,
        Sentence_rule_4,
        Sentence_rule_5,
    ],
    "weight": [
        Sentence_rule_1,
        Sentence_rule_2,
        Sentence_rule_3,
        Sentence_rule_4,
        Sentence_rule_5,
    ],
    "distanace": [
        Sentence_rule_1,
        Sentence_rule_2,
        Sentence_rule_3,
        Sentence_rule_4,
        Sentence_rule_5,
    ],
    "currency": [
        Sentence_rule_1,
        Sentence_rule_2,
        Sentence_rule_5,
        Sentence_rule_6,
    ],
}

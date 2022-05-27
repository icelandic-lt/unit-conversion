from traceback import print_tb


base = {
    (0, "f_at_af"): "núll",
    (1, "f_et_kk_nf"): "einn",
    (1, "f_et_kk_þf"): "einn",
    (1, "f_et_kk_þgf"): "einum",
    (1, "f_et_kk_ef"): "eins",
    (1, "f_et_kvk_nf"): "ein",
    (1, "f_et_kvk_þf"): "eina",
    (1, "f_et_kvk_þgf"): "einni",
    (1, "f_et_kvk_ef"): "einnar",
    (1, "f_et_hk_nf"): "eitt",
    (1, "f_et_hk_þf"): "eitt",
    (1, "f_et_hk_þgf"): "einu",
    (1, "f_et_hk_ef"): "eins",
    (1, "f_ft_kk_nf"): "einir",
    (1, "f_ft_kk_þf"): "eina",
    (1, "f_ft_kk_þgf"): "einum",
    (1, "f_ft_kk_ef"): "einna",
    (1, "f_ft_kvk_nf"): "einar",
    (1, "f_ft_kvk_þf"): "einar",
    (1, "f_ft_kvk_þgf"): "einum",
    (1, "f_ft_kvk_ef"): "einna",
    (1, "f_ft_hk_nf"): "ein",
    (1, "f_ft_hk_þf"): "ein",
    (1, "f_ft_hk_þgf"): "einum",
    (1, "f_ft_hk_ef"): "einna",
    (2, "f_ft_kk_nf"): "tveir",
    (2, "f_ft_kk_þf"): "tvo",
    (2, "f_ft_kk_þgf"): "tveimur/tveim",
    (2, "f_ft_kk_ef"): "tvegga",
    (2, "f_ft_kvk_nf"): "tvær",
    (2, "f_ft_kvk_þf"): "tvær",
    (2, "f_ft_kvk_þgf"): "tveimur/tveim",
    (2, "f_ft_kvk_ef"): "tveggja",
    (2, "f_ft_hk_nf"): "tvö",
    (2, "f_ft_hk_þf"): "tvö",
    (2, "f_ft_hk_þgf"): "tveimur/tveim",
    (2, "f_ft_hk_ef"): "tveggja",
    (3, "f_ft_kk_nf"): "þrír",
    (3, "f_ft_kk_þf"): "þrjá",
    (3, "f_ft_kk_þgf"): "þremur/þrem",
    (3, "f_ft_kk_ef"): "þriggja",
    (3, "f_ft_kvk_nf"): "þrjár",
    (3, "f_ft_kvk_þf"): "þrjár",
    (3, "f_ft_kvk_þgf"): "þremur/þrem",
    (3, "f_ft_kvk_ef"): "þriggja",
    (3, "f_ft_hk_nf"): "þrjú",
    (3, "f_ft_hk_þf"): "þrjú",
    (3, "f_ft_hk_þgf"): "þremur/þrem",
    (3, "f_ft_hk_ef"): "þriggja",
    (4, "f_ft_kk_nf"): "fjórir",
    (4, "f_ft_kk_þf"): "fjóra",
    (4, "f_ft_kk_þgf"): "fjórum",
    (4, "f_ft_kk_ef"): "fjögurra/fjögra",
    (4, "f_ft_kvk_nf"): "fjórar",
    (4, "f_ft_kvk_þf"): "fjórar",
    (4, "f_ft_kvk_þgf"): "fjórum",
    (4, "f_ft_kvk_ef"): "fjögurra/fjögra",
    (4, "f_ft_hk_nf"): "fjögur",
    (4, "f_ft_hk_þf"): "fjögur",
    (4, "f_ft_hk_þgf"): "fjórum",
    (4, "f_ft_hk_ef"): "fjögurra/fjögra",
    (5, "f_at_af"): "fimm",
    (6, "f_at_af"): "sex",
    (7, "f_at_af"): "sjö",
    (8, "f_at_af"): "átta",
    (9, "f_at_af"): "níu",
    (10, "f_at_af"): "tíu",
    (11, "f_at_af"): "ellefu",
    (12, "f_at_af"): "tólf",
    (13, "f_at_af"): "þrettán",
    (14, "f_at_af"): "fjórtán",
    (15, "f_at_af"): "fimmtán",
    (16, "f_at_af"): "sextán",
    (17, "f_at_af"): "sautján",
    (18, "f_at_af"): "átján",
    (19, "f_at_af"): "nítján",
    (20, "f_at_af"): "tuttugu",
    (30, "f_at_af"): "þrjátíu",
    (40, "f_at_af"): "fjörutíu",
    (50, "f_at_af"): "fimmtíu",
    (60, "f_at_af"): "sextíu",
    (70, "f_at_af"): "sjötíu",
    (80, "f_at_af"): "áttatíu",
    (90, "f_at_af"): "níutíu",
    (100, "f_at_af"): "hundrað",
    (1000, "f_at_af"): "þúsund",
    (1000000, "f_at_af"): "milljón",
}


half = {
    "f_at_af": "hálfur",
    "f_et_kk_nf": "hálfur",
    "f_et_kk_þf": "hálfan",
    "f_et_kk_þgf": "hálfum",
    "f_et_kk_ef": "hálfs",
    "f_et_kvk_nf": "hálf",
    "f_et_kvk_þf": "hálfa",
    "f_et_kvk_þgf": "hálfri",
    "f_et_kvk_ef": "hálfrar",
    "f_et_hk_nf": "hálft",
    "f_et_hk_þf": "hálft",
    "f_et_hk_þgf": "hálfu",
    "f_et_hk_ef": "hálfs",
    "f_ft_kk_nf": "hálfur",
    "f_ft_kk_þf": "hálfan",
    "f_ft_kk_þgf": "hálfum",
    "f_ft_kk_ef": "hálfs",
    "f_ft_kvk_nf": "hálf",
    "f_ft_kvk_þf": "hálfa",
    "f_ft_kvk_þgf": "hálfri",
    "f_ft_kvk_ef": "hálfrar",
    "f_ft_hk_nf": "hálfs",
    "f_ft_hk_þf": "hálft",
    "f_ft_hk_þgf": "hálfu",
    "f_ft_hk_ef": "hálfs",
}


fallbeygingar_fyrir_1 = [
    "f_et_kk_nf",
    "f_et_kk_þf",
    "f_et_kk_þgf",
    "f_et_kk_ef",
    "f_et_kvk_nf",
    "f_et_kvk_þf",
    "f_et_kvk_þgf",
    "f_et_kvk_ef",
    "f_et_hk_nf",
    "f_et_hk_þf",
    "f_et_hk_þgf",
    "f_et_hk_ef",
    "f_ft_kk_nf",
    "f_ft_kk_þf",
    "f_ft_kk_þgf",
    "f_ft_kk_ef",
    "f_ft_kvk_nf",
    "f_ft_kvk_þf",
    "f_ft_kvk_þgf",
    "f_ft_kvk_ef",
    "f_ft_hk_nf",
    "f_ft_hk_þf",
    "f_ft_hk_þgf",
    "f_ft_hk_ef",
]

fallbeygingar_fyrir_2_3_4 = [
    "f_ft_kk_nf",
    "f_ft_kk_þf",
    "f_ft_kk_þgf",
    "f_ft_kk_ef",
    "f_ft_kvk_nf",
    "f_ft_kvk_þf",
    "f_ft_kvk_þgf",
    "f_ft_kvk_ef",
    "f_ft_hk_nf",
    "f_ft_hk_þf",
    "f_ft_hk_þgf",
    "f_ft_hk_ef",
]


def get_from_base(n, f):
    """
    Gets the numbers in the base that between 1-19 and all numbers that are divisable by 10,100,1000 etc.
    Return a number
    """
    num = base[n, f]
    if "/" in num:
        return n, f, num.split("/")

    else:
        return n, f, [num]


def nums_20_99(n, f):
    """
    Returns a list of [digit-intiger, case, digit-string] for the provided range between 20-99.
    Uses the pythonic range input.
    """

    n1 = int(str(n)[0] + "0")
    n2 = int(str(n)[1])
    last_number = get_from_base(n2, f)
    if len(last_number[2]) == 2:
        return n, f, [f"{base[n1,'f_at_af']} og {n2}" for n2 in last_number[2]]
    else:
        return n, f, [f"{base[n1,'f_at_af']} og {base[n2,f]}"]


def nums_100_999(n, f):
    """
    Returns a list of [digit-intiger, case, digit-string] for the provided range between 100-999.
    Uses the pythonic range input.
    """

    def hundreds(n):
        n_1 = int(str(n)[0])
        if n_1 == 1:
            num = f"{base[n_1, 'f_et_hk_nf']} hundrað"
        elif n_1 in [2, 3, 4]:
            num = f"{base[n_1,'f_ft_hk_nf']} hundruð"
        else:
            num = f"{base[n_1,'f_at_af']} hundruð"
        return num

    n1 = int(str(n)[0] + "00")
    num1 = hundreds(n1)
    n2 = n - n1

    if n in [100, 200, 300, 400, 500, 600, 700, 800, 900]:
        num = hundreds(n)
        return n, f, [num]
    elif n2 in [x for x in range(1, 20)] or n2 in [x for x in range(20, 101, 10)]:
        num2 = []
        for line in get_from_base(n2, f)[2]:
            num2.append(f"og {line}")
        num2 = [n, f, num2]

    else:
        num2 = nums_20_99(n2, f)

    num = [f"{num1} {n2}" for n2 in num2[2]]
    for line in num:
        if "eitt hundrað" in line:
            num.append(line.replace("eitt hundrað", "hundrað"))

    return n, f, num


def get_number(n, f):
    """
    Diverts requests to the correct function
    """
    if n < 1:
        print(n)
        return get_fraction_less_than_zero(n, f)
    elif n % int(n) == 0 and isinstance(n, float):
        n = int(n)
    if isinstance(n, float):
        return get_fraction(n, f)
    elif (
        n in [x for x in range(1, 20)]
        or n in [x for x in range(20, 101, 10)]
        or n in [1000, 1000000]
    ):
        return get_from_base(n, f)
    elif n in [x for x in range(20, 100)]:
        return nums_20_99(n, f)
    elif n in [x for x in range(100, 1000)]:
        return nums_100_999(n, f)


def get_fraction_less_than_zero(n, f):
    """ """

    n2 = int(str(n).split(".")[1])

    num = [f"núll komma {x}" for x in get_number(n2, f)[2]]
    return n, f, num


def get_fraction(n, f):
    """ """
    n1 = int(str(n).split(".")[0])
    n2 = int(str(n).split(".")[1])
    to_return = []

    if n1 < 5 and n2 < 5:
        # To account for that we only use the singular case of 1.
        if (n1, f) not in base:
            _n, _f, nums_1 = get_number(n1, f.replace("et", "ft"))
        else:
            _n, _f, nums_1 = get_number(n1, f)
        _n, _f, nums_2 = get_number(n2, f)

        pass
    else:
        print(n, f, n1, n2)
        if n1 > 4:
            _n, _f, nums_1 = get_number(n1, "f_at_af")
            _n, _f, nums_2 = get_number(n2, f)

        else:
            _n, _f, nums_1 = get_number(n1, f)
            _n, _f, nums_2 = get_number(n2, "f_at_af")

    to_return.append(f"{nums_1[0]} komma {nums_2[0]}")

    return n, f, to_return


def create_fill_in_list(a, b):
    """
    Returns a list with (number, inflection) items for all possible numbers in the given range.
    """

    def is_in_teens(n):
        if len(str(n)) == 1:
            return False
        elif (len(str(n)) == 2 and n in [x for x in range(11, 20)]) or (
            int(str(n)[-2:]) in [x for x in range(11, 20)]
        ):
            return True
        else:
            return False

    def is_in_the_tens(n):
        if len(str(n)) == 1:
            return False
        elif (len(str(n)) == 2 and n in [x for x in range(20, 101, 10)]) or (
            int(str(n)[-2:]) in [x for x in range(10, 101, 10)]
        ):
            return True
        else:
            return False

    to_return = []

    for n in range(a, b):
        if n in [x for x in range(1, 5)]:
            for f in [x[1] for x in base.keys() if x[0] == n]:
                to_return.append([n, f])
        elif (
            n in [x for x in range(5, 20)]
            or is_in_the_tens(n)
            or n in [100, 1000, 1000000]
            or is_in_teens(n)
            or n in [100, 200, 300, 400, 500, 600, 700, 800, 900]
        ):
            f = "f_at_af"
            to_return.append([n, f])

        else:
            last_num = int(str(n)[-1])
            for f in [x[1] for x in base.keys() if x[0] == last_num]:
                to_return.append([n, f])
    return to_return


def generate_whole_numbers():
    """ """
    with open("numbers.tsv", "w") as f_out:
        for n, f in create_fill_in_list(1, 1000):
            n, f, nums = get_number(n, f)
            for line in nums:
                f_out.write(f"{n}\t{f}\t{line}\n")


def create_fill_in_list_fractions(a, b, d):
    """
    Returns a list with (number, inflection) items for all possible numbers in the given range.
    """
    import numpy as np

    to_return = []
    for n in [np.round(x, 2) for x in np.arange(a, b, d)]:
        if n % int(n) == 0:
            continue

        n1 = int(str(n).split(".")[0])
        d = int(str(n)[-1])
        if d in [1, 2, 3, 4]:
            for f in [x[1] for x in base.keys() if x[0] == d]:
                # The plural form for 1 is not used in fractions
                if d == 1 and "ft" in f:
                    continue
                to_return.append([n, f])
        else:
            for f in [x[1] for x in base.keys() if x[0] == n1]:
                if n1 == 1 and "ft" in f:
                    continue
                to_return.append([n, f])

    return to_return


def add_half(n, f):
    """
    Gerum ráð fyrir að það er bara kallað í þetta fall þegar talan er x-hálfur
    Segjum að n=1,5 þá skilar fallið til baka "einn og hálfur".
    """
    n1 = int(str(n).split(".")[0])
    if n1 == 0:
        return half[f]

    else:
        return f"{get_number(n1, f)[2][0]} og {half[f]}"


def generate_fractions():
    """ """
    with open("fractions.tsv", "w") as f_out, open("fill_in_fractions", "w") as f_out2:
        for n, f in create_fill_in_list_fractions(0.1, 10, 0.1):
            f_out2.write(f"{n}\t{f}\n")
            n, f, nums = get_number(n, f)
            if int(str(n).split(".")[-1]) == 5:
                nums += [add_half(n, f)]
            for line in nums:
                f_out.write(f"{n}\t{f}\t{line}\n")


if __name__ == "__main__":
    # generate_whole_numbers()
    generate_fractions()

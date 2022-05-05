def get_field(s_obj, key):
    """
    Takes in a sentnce object and finds the values for the given key.
    """
    to_return = []
    for s in s_obj:
        if key in s:
            to_return.append(s)
    return to_return


def load_numbers(file="numbers.tsv"):
    """
    Loads the tsv containing the number as a dict
    """
    to_return = {}
    with open(file) as f_in:
        for line in f_in:
            line = line.rstrip().split("\t")
            to_return[(line[0], line[1])] = line[2:]

    return to_return


def get_valid_numbers(cf_obj):
    """
    Takes in a list of convert_from dict object and find all combination of valid numbers
    """
    for obj in cf_obj:
        print(obj)

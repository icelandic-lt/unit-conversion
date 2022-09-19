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
    to_return = []
    with open(file) as f_in:
        for line in f_in:
            line = line.rstrip().split("\t")
            to_return.append([line[0], line[1], line[2]])

    return to_return


from reynir_correct import check_single
import os, logging


def run_check_single(s):

    return [s, check_single(s)]


def test_output_with_GreynirCorrect(sentences, file):
    from multiprocessing.dummy import Pool
    import time

    start_time = time.time()

    # from concurrent import ProcessPoolExecutor

    # git clone https://github.com/mideind/GreynirCorrect
    # cd GreynirCorrect
    ## [ Activate your virtualenv here if you have one ]
    # pip install -e .

    # list of cases that greynir correct dosen't handle correctly.
    # We screen for these case to make the output more readable.

    dont_check = [
        "Ásláttarvilla: 'einni' -> 'einnig'",
        "Orðið 'míla' gæti átt að vera 'mála'",
    ]
    os.makedirs(os.path.dirname(file), exist_ok=True)

    iterable, res = [x[2] for x in sentences], []
    logging.info("Running greynir correct on the sentences")

    with Pool(processes=5) as pool:
        res = pool.map(run_check_single, iterable)

    # res = [run_check_single(s) for s in iterable]
    out_filename = os.path.join(os.path.dirname(file), "corrections.tsv")
    with open(out_filename, "w") as f_out:
        for s, sent in res:
            for annotation in sent.annotations:
                if annotation and not any([annotation.text in l for l in dont_check]):
                    f_out.write("Original: " + s + "\n")
                    f_out.write("Suggestion: " + str(sent) + "\n")
                    f_out.write(annotation.text + "\n------\n")
    t = time.time() - start_time
    logging.info(f"Correction runtime {t:.2f} seconds\n\t\t\t{t/60:.2f} minutes")

    logging.info(f"Corrections added to the file {out_filename}")


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


def save_to_file(sentences, file="out.tsv"):
    os.makedirs(os.path.dirname(file), exist_ok=True)
    logging.info(f"Saving to file {file}")
    with open(file, "w") as f_out:
        for line in sentences:

            f_out.write(str(line[0]) + "\t" + line[1] + "\t" + line[2] + "\n")
    logging.info(f"Saved to {file}")

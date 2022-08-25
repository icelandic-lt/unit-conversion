from re import L
from numi import spell_out

from random import randint

nums = set()

output = "input/numbers.tsv"
with open(output, "w") as f_out:

    # Add all numbers for 1 to 1000
    for n in range(1, 1001):
        nums.add(n)
        for line in spell_out(n):
            for s in line[2]:
                f_out.write(f"{line[0]}\t{line[1]}\t{s}\n")

    # Add numbers
    for n in range(10000, 999999, 1000):
        nums.add(n)
        for line in spell_out(n):
            for s in line[2]:
                f_out.write(f"{line[0]}\t{line[1]}\t{s}\n")

    # Add random numbers
    for _ in range(200000):
        n = randint(1000, 999999)
        if n not in nums:
            nums.add(n)
            for line in spell_out(n):
                for s in line[2]:
                    f_out.write(f"{line[0]}\t{line[1]}\t{s}\n")
    print(f"Created {len(nums)} numbers")
    print(f"Saved in {output}")

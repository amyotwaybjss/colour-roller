# This test should run colour_roll on a single sheet many times.
# It should then return percentages based on how often each option is selected.

from colour_roll import roller
from env import wb
from collections import Counter  # library


def ran_test(workbook, sheet, tests: int):
    results = []

    for x in range(1, tests+1):
        output = roller(workbook, sheet, "single").split(" ")[1]
        results.append(output)

    count_results = Counter(results).most_common()

    all_results = ""

    for r in count_results:
        score = f'{r[0]} ({format(r[1]/tests, ".0%")}), '
        all_results += score

    results_output = all_results.rstrip(", ")

    return results_output


test = ran_test(wb, "test", 500)
print(test)

# This test should run colour_roll on a single sheet many times.
# It should then return percentages based on how often each option is selected.

from colour_roll import roller
from env import wb
from collections import Counter

sheet = "test"
shuffle = "single"
tests = 100
results = []

# output = roller(wb, sheet, shuffle).split(" ")[1]

# print(output)

for x in range(1, tests+1):
    output = roller(wb, sheet, shuffle).split(" ")[1]
    results.append(output)

count_results = Counter(results).most_common()
# print(count_results)

all_results = ""

for r in count_results:
    score = f'{r[0]} ({format(r[1]/tests, ".0%")}), '
    all_results += score

print(all_results)

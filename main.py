from most_frequent import count_nums
from divise_words import screening, text
from inserction_lists import intersection, listA, listB

nums = [3, 2, 5, 4, 1, 2, 3, 1, 3, 4, 1, 1, 1, 1]

print(count_nums(nums))

for key, value in screening(text).items():
    print(f"{key}: {value}")

print(intersection(listA, listB))

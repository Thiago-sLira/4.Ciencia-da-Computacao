listA = [1, 2, 3, 4, 5, 6]
listB = [4, 5, 6, 7, 8, 9]


def intersection(list1, list2):
    seen_in_a = {}

    for item in list1:
        if item not in seen_in_a:
            seen_in_a[item] = True

    ans = []

    for item in list2:
        if item in seen_in_a:
            ans.append(item)

    return ans

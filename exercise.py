double = {i: i * 2 for i in range(3, 21)}

# print(double)

count_chars = {}

string = "bbbbaaaacccaaaaaaddddddddccccccc"

for char in string:
    if char not in count_chars:
        count_chars[char] = 1
    else:
        count_chars[char] += 1

print(count_chars)

for key in double.keys():
    if key % 2 != 0:
        double[key] = key * 3


print(double)

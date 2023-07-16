import collections

letter = "Hello welcome to Cathay 60th year anniversary"

# letter_upper = letter.upper().replace(" ", "")
# print(sorted(collections.Counter(letter_upper).items()))

count = {}
for x in letter.upper().replace(" ", ""):
    if x not in count:
        count[x] = 1
    else:
        count[x] += 1

print(sorted(count.items()))
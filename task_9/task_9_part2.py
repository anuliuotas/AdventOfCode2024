
memmory = []
numbers_only = []
with open('input.txt', 'r') as file:
    for line in file:
        print(line)
        l = line.replace('\n', '')
        number_idx = 0
        for i, number in enumerate(l):
            even = i % 2 == 0
            obj = (int(number), number_idx if even else '.')
            memmory.append(obj)
            if even:
                numbers_only.append(obj)
                number_idx += 1

print(memmory)

def find_first_gap(memmory, gap_size):
    for idx, c in enumerate(memmory):
        if c[0] >= gap_size and c[1] == '.':
            return idx, c[0]
    return None, None


for numb in reversed(numbers_only):
    print(numb)
    count = numb[0]
    nr = numb[1]

    idx = memmory.index(numb)
    gap_idx, gap_size = find_first_gap(memmory, count)

    if gap_idx is not None and gap_idx < idx:
        memmory[idx] = (count, '.')
        if gap_size == count:
            memmory[gap_idx] = numb
        else:
            memmory[gap_idx] = numb
            if memmory[gap_idx + 1][1] == '.':
                memmory[gap_idx + 1][1] = (memmory[gap_idx + 1][0] + gap_size-count, '.')
            else:
                memmory.insert(gap_idx + 1, (gap_size-count, '.'))
print(memmory)

adj_memmory = []
for c in memmory:
    for i in range(0, c[0]):
        adj_memmory.append(c[1])
print(adj_memmory)

result = 0
for idx in range(0, len(adj_memmory)):
    c = adj_memmory[idx]
    if c == '.':
        continue
    result += c * idx
print(result)

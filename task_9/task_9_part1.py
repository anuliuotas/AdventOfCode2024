
memmory = []
with open('input.txt', 'r') as file:
    for line in file:
        print(line)
        l = line.replace('\n', '')
        number_idx = 0
        for i, number in enumerate(l):
            even = i % 2 == 0
            for k in range(int(number)):
                if even:
                    memmory.append(number_idx)
                else:
                    memmory.append('.')
            if even:
                number_idx += 1

print(memmory)


def get_last_number(ll):
    for i in range(len(ll) - 1, -1, -1):
        c = ll[i]
        if c == '.':
            continue
        return i, c


for idx in range(0, len(memmory)):
    print(f'{idx} out of {len(memmory)}')
    c = memmory[idx]
    if c == '.':
        i, nr = get_last_number(memmory)
        if idx >= i:
            break
        memmory[idx] = nr
        memmory[i] = '.'

print(memmory)

result = 0
for idx in range(0, len(memmory)):
    c = memmory[idx]
    if c == '.':
        continue
    result += c * idx
print(result)
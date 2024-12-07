from dataclasses import dataclass
from itertools import product

def generate_combinations(numbers, operators):
    num_operators = len(numbers) - 1
    all_combinations = product(operators, repeat=num_operators)

    results = []
    for combination in all_combinations:
        mixed_list = []
        for i, num in enumerate(numbers):
            mixed_list.append(num)  # Add the number
            if i < len(combination):
                mixed_list.append(combination[i])  # Add the operator
        results.append(mixed_list)
    return results


def solve_eq_first_multiply(eq):
    while '*' in eq:
        multiply_idx = eq.index('*')

        v1 = eq[multiply_idx - 1]
        v2 = eq[multiply_idx + 1]
        r = v1 * v2
        eq.pop(multiply_idx - 1)
        eq.pop(multiply_idx - 1)
        eq.pop(multiply_idx - 1)
        eq.insert(multiply_idx - 1, r)

    while '+' in eq:
        eq.remove('+')
    if len(eq) == 1:
        return eq[0]

    return sum(eq)


def solve_eq_left_to_right(eq):
    while len(eq) != 1:
        operator_idx = 1

        v1 = eq[operator_idx - 1]
        v2 = eq[operator_idx + 1]
        operator = eq[operator_idx]
        if operator == '*':
            r = v1 * v2
        elif operator == '+':
            r = v1 + v2
        elif operator == '||':
            r = int(str(v1) + str(v2))

        eq.pop(operator_idx - 1)
        eq.pop(operator_idx - 1)
        eq.pop(operator_idx - 1)
        eq.insert(operator_idx - 1, r)

    return eq[0]


eqs = []

reading_rules_done = False
with open('input.txt', 'r') as file:
    for line in file:
        l = line.replace('\n', '')
        ls = l.split(': ')
        result = int(ls[0].strip())
        numbers = []
        for nr in ls[1].split(' '):
            numbers.append(int(nr.strip()))
        eqs.append((result, numbers))


# operators = ['+', '*']
# total_valid = 0
# for result, numbers in eqs:
#
#     combinations = generate_combinations(numbers, operators)
#     for eq in combinations:
#         if result == solve_eq_left_to_right(eq):
#             total_valid += result
#             break
# print(total_valid)


operators = ['+', '*', '||']
total_valid = 0
idx = 1
for result, numbers in eqs:
    print(f'Processing eq {idx} out of {len(eqs)}')

    combinations = generate_combinations(numbers, operators)
    for eq in combinations:
        if result == solve_eq_left_to_right(eq):
            total_valid += result
            break
    idx += 1
print(total_valid)
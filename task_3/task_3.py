
def calc_line_score(line):
    result = 0
    for s in line.split('mul('):
        first_number_buff = ''
        second_number_buff = ''

        first_number_found = False
        comma_found = False
        second_number_found = False

        for c in s:

            if not first_number_found:
                if c.isnumeric():
                    first_number_buff += c
                else:
                    first_number_found = True
                    if not first_number_buff.isnumeric():
                        break

            if first_number_found and not comma_found:
                if c == ',':
                    comma_found = True
                    continue
                else:
                    break

            if first_number_found and comma_found and not second_number_found:
                if c.isnumeric():
                    second_number_buff += c
                else:
                    if c == ")":
                        second_number_found = True
                        break
                    else:
                        break

        if first_number_found and second_number_found and comma_found:
            first_nr = int(first_number_buff)
            second_nr = int(second_number_buff)

            print(f'{first_number_buff} * {second_number_buff}')

            result = result + first_nr * second_nr
    return result


line = '_do'
with open('input.txt', 'r') as file:
    for l in file:
        line += l


print(f'First task result: {calc_line_score(line)}')

line = line.replace("don'tdo", "don't_do")  # avoiding exceptions

enabled_lines = []
for sa in line.split("don't"):
    previous_enabled = False

    for idx, sb in enumerate(sa.split('do')):
        if idx != 0:
            enabled_lines.append(sb)

score = 0
for line in enabled_lines:
    score += calc_line_score(line)

print(f'Second task result: {score}')
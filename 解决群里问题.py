alphabet = (
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X',
    'Y', 'Z')
i = 0

for output_1 in alphabet:
    for output_2 in alphabet:
        for output_3 in alphabet:
            for output_4 in alphabet:
                for output_5 in alphabet:
                    print(output_1 + output_2 + output_3 + output_4 + output_5 + ' ' + str(i))
                    i += 1

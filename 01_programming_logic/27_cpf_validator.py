"""
CPF Validator
"""
import re

while True:
    cpf = input("Type some CPF: ")
    cpf = re.sub("[^0-9]", "", cpf)

    if len(cpf) == 11:
        new_cpf = cpf[:-2]
        reverse = 10
        total = 0
        for i in range(19):
            if i >= 9:
                i -= 9
            total += int(new_cpf[i]) * reverse

            reverse -= 1
            if reverse < 2:
                reverse = 11
                d = 11 - (total % 11)

                if d > 9:
                    d = 0

                total = 0
                new_cpf += str(d)

        # CPF cannot be a sequence of numbers
        sequence = new_cpf == new_cpf[0] * 11

        if cpf == new_cpf and not sequence:
            print("Valid CPF.")
        else:
            print("Invalid CPF.")
    else:
        print("You must enter an 11-digits CPF number.")


# """
# My solution:
# """
# if len(cpf) == 11:
#     new_cpf = cpf[:-2]
#     counter = 0

#     for i, num in enumerate(range(len(new_cpf) + 1, 1, -1)):
#         cpf_num = int(new_cpf[i])
#         counter += cpf_num * num

#     digit = 11 - (counter % 11)
#     first_digit = 0 if digit > 9 else digit

#     new_cpf += str(first_digit)
#     counter = 0

#     for i, num in enumerate(range(len(new_cpf) + 1, 1, -1)):
#         cpf_num = int(new_cpf[i])
#         counter += cpf_num * num

#     digit = 11 - (counter % 11)
#     second_digit = 0 if digit > 9 else digit

#     new_cpf += str(second_digit)

#     print("Valid CPF.") if new_cpf == cpf else print("Invalid CPF.")
# else:
#     print("You must enter an 11-digits CPF number.")

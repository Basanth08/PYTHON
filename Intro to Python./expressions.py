def expressions_practice():
    a_constant = 123.456
    addition = 6+7
    exponent = 6 ** 7
    floor_division = 10//3
    mod = 10 % 3
    parens = (6+7) * 7
    mix_it_up = (6+7) * 6 // (7-5)
    print(a_constant)
    print(addition)
    print(exponent)
    print(floor_division)
    print(mod)
    print(parens)
    print(mix_it_up)


expressions_practice()

def promt_and_print():
    value_1 = int(input("enter a number:"))
    value_2 = int(input("Enter another"))
    if value_1 > 0 and value_2 > 0:

     print(value_1, '+' , value_2, "=", (value_1 + value_2))
    print(value_1, '-' , value_2, "=", (value_1 - value_2))
    print(value_1, '*' , value_2, "=", (value_1 * value_2))
    print(value_1, '//' , value_2, "=", (value_1 // value_2))

promt_and_print()



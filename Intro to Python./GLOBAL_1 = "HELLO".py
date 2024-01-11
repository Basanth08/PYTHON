GLOBAL_1 = "HELLO"
GLOBAL_2 = "Goodbye"

def function_1(parameter_1, parameter_2,):
    print(parameter_1)

    local_1 = "test"

    parameter_1= 123

    print(parameter_1, parameter_2, local_1)

function_1(GLOBAL_1, GLOBAL_2)

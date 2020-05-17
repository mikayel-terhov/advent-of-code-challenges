import math

OP_ADD = 1
OP_MUL = 2
OP_END = 99


def run_intcodes(data, noun=0, verb=0):
    array = data.copy()
    if noun != 0 and verb != 0:
        array[1] = noun
        array[2] = verb

    for index in range(0, len(array), 4):

        operator = array[index]
        inputA = array[array[index + 1]]
        inputB = array[array[index + 2]]
        if operator == OP_END:
            return array[0]
        elif operator == OP_ADD:
            array[array[index + 3]] = inputA + inputB
        elif operator == OP_MUL:
            array[array[index + 3]] = inputA * inputB


# array[1] = 12
# array[2] = 2
#
# print(array)
# run_intcodes()
# print(array)
with open("data/day2.txt") as f:
    # All data is on the first line
    inputs_array = [int(x) for x in f.readline().split(',')]

print(inputs_array)
for noun_t in range(100):
    for verb_t in range(100):
        inputs_array[1] = noun_t
        inputs_array[2] = verb_t

        output = run_intcodes(inputs_array,noun_t,verb_t)
        if output == 19690720:
            print(100 * noun_t + verb_t)
            break

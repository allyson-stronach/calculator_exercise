import arithmetic


while True:
    query = raw_input()
    token_list = query.split(" ")
    number_one=int(token_list[1])
    number_two=int(token_list[2])
    if token_list[0] == '+':
        print arithmetic.add (number_one, number_two)
    elif token_list[0] == '-':
        print arithmetic.subtract (number_one, number_two)
    elif token_list[0] == '*':
        print arithmetic.multiply (number_one, number_two)
    elif token_list[0] == '/':
        print arithmetic.divide (number_one, number_two)
    elif token_list[0] == 'square':
        print arithmetic.square (number_one)
    elif token_list[0] == 'cube':
        print arithmetic.cube (number_one)
    elif token_list[0] == 'pow':
        print arithmetic.power (number_one, number_two)
    elif token_list[0] == 'mod':
        print arithmetic.mod (number_one, number_two)
    else:
        print "I don't understand."

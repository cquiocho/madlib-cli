print("Welcome to a crazy and silly version of Mad Lib!\nPlease start by answering the questions below:\n")

path = 'assets/madlib.txt'

def read_template(path):
    # Opening file
    lines = list()
    with open(path) as f:
        f.readline()

        for line in f:
            if len(line) > 1:
                lines.append(line)
    return lines


def parse(line_to_parse):
    # Get words from inside brackets
    number_of_replacements = line_to_parse.count('{')
    words = list()
    start = 0
    end = 0
    for elem in range(number_of_replacements):
        start = line_to_parse.find('{', end)
        end = line_to_parse.find('}', start)

        word = line_to_parse[start + 1 : end]
        words.append(word)

    # Get a line without text between brackets
    new_line = ''
    add_characters = True

    for char in line_to_parse:
        if char == '}':
            add_characters = True
        if add_characters:
            new_line += char
        if char == '{':
            add_characters = False

    return new_line, words


def merge(line_to_fill, words):
    return line_to_fill.format(*words)


RUN = True

counter = 0

lines = read_template(path)

while RUN:
    current_line = lines[counter]
    empty_bracket_line, parsed_values = parse(current_line)
    print(empty_bracket_line)

    split_on_spaces = empty_bracket_line.split(' ')

    answers = list()
    for p in parsed_values:
        answer_input = input('Gimme a ' + p)
        answers.append(answer_input)

    # count = 0
    # answered_line = ''
    # for sp in split_on_spaces:
    #     if sp.find('{}'):
    #         answer = sp.replace('{}', answers[count])
    #         answered_line += answer
    #         count += 1
    #     else:
    #         answered_line += sp
    #
    #     answered_line += ' '

    answered_line = merge(empty_bracket_line, answers)

    print(answered_line)

    print('Do a madlib?')
    inp = input()
    if inp == 'n' or inp == 'N' or inp == 'no':
        RUN = False
    counter += 1

print('Thanks')
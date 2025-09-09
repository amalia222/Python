def analyze_file(filename):
    let_count = 0
    word_count = 0
    line_count = 0
    in_word = False
    with open(filename) as f:
        for line in f:
            line_count += 1
            for char in line:
                if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                    let_count += 1
                    if not in_word:
                        word_count += 1
                        in_word = True
                else:
                    in_word = False
    print(f'input File contains:', f'{let_count} letters', f'{word_count} words', f'{line_count} lines', sep = '\n')

analyze_file('text2.txt')
def wrap(text, line_length):
    words = text.split()
    lines_of_words = []
    current_line_length = line_length
    for word in words:
        if current_line_length + len(word) > line_length:
            lines_of_words.append([])
            current_line_length = 0
        lines_of_words[-1].append(word)
        current_line_length += len(word)
    lines = [' '. join(line_of_words) for line_of_words in lines_of_words]
    result = '\n'.join(lines)
    return result
wealth_of_nations="The annual labour of every \nnation in conjunction with \nprotocols"

if __name__ == '__main__':
    text=wrap(wealth_of_nations,25)
    print(text)

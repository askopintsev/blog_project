from collections import Counter


def get_text():
    """Function to get text from user input.
    Returns text
    """

    while True:
        print('Введите текст:')
        # user's choice handling
        text = str(input())
        if len(text) == 0:
            print('Не введено ни одного символа.')
            continue

        break

    return text


def get_data_from_text(text):
    """
    Function to get longest word from text and most frequent word from text.
    Returns longest word from text and most frequent word from text
    """
    top_length = [None, 0]  # variable to store longest word with its length
    top_count = Counter()  # structure to count words

    for word in text.split(' '):
        # cleaning word from symbols if word isn't symbol itself
        if len(word) > 1:
            word = word.strip(',.:;!? ')

        if len(word) > top_length[1]:
            top_length[0] = word
            top_length[1] = len(word)

        top_count.update([word])

    top_word = top_count.most_common(1)[0][0]

    return top_word, top_length[0]


if __name__ == '__main__':
    text = get_text()
    top_word, top_length = get_data_from_text(text)
    print('Наиболее часто встречающееся слово:', top_word)
    print('Самое длинное слово:', top_length)

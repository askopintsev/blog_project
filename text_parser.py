from collections import Counter


def get_text():
    """
    Function to get text from user input.
    :return: inputted_text (str)
    """

    while True:
        print('Введите текст:')

        # user's input text handling
        inputted_text = str(input())
        if len(inputted_text) == 0:
            print('Не введено ни одного символа.')
            continue  # go to new iteration if input is empty

        break  # finish cycle if input text is not empty

    return inputted_text


class WordAnalyzer:
    """
    Class which performs text analysis: search longest and most frequent word.
    Incapsulates methods for each different action.
    Methods:
        get_longest_word - search longest words
        get_frequent_word - search most frequent words
    """

    @staticmethod
    def get_longest_word(raw_text):
        """
        Function which searches for longest word from text
        or list of words if there are few of the same biggest length.
        :param raw_text: text from user as list of words
        :return: longest_word_list: list of words of biggest length from text - one or several elements
        """

        # list of words is sorted by length of words to get first word as longest
        raw_text.sort(key=lambda s: len(s), reverse=True)
        longest_element = raw_text[0]
        # filter by biggest length to find all words with the same length
        longest_word_list = [word for word in raw_text if len(word) == len(longest_element)]

        return longest_word_list

    @staticmethod
    def get_frequent_word(raw_text):
        """
        Function which searches most frequent word from text
        or list of words if there are few of the same frequency.
        :param raw_text: text from user as list of words
        :return: frequent_word_list: list of words of biggest frequency from text - one or several elements
        """

        # work with structure to store word's frequency
        frequent_words_dict = Counter()
        frequent_words_dict.update(raw_text)

        # getting biggest frequency to get words with it
        frequency = frequent_words_dict.most_common(1)[0][1]

        # filter by biggest frequency dict of words to get all most frequent words
        frequent_word_list = [key for key, value in frequent_words_dict.items() if value == frequency]

        return frequent_word_list


def get_data_from_text(raw_text):
    """
    Function to get longest word from text and most frequent word from inputted text.
    Returns longest word from text and most frequent word from inputted text.
    :parameter: raw_text (str), obligatory
        Plain text to process its words
    :return:
        frequent_words (list)
            list of most common words from text
        longest_words (list)
            list of longest words from text
    """

    analyzer = WordAnalyzer()

    text_list = []  # structure for processed words of text
    for word in raw_text.split(' '):
        # cleaning word from symbols if word isn't symbol itself
        if len(word) > 1:
            word = word.strip(',.:;!? ')
        word = word.lower()
        text_list.append(word)

    longest_words = analyzer.get_longest_word(text_list)
    frequent_words = analyzer.get_frequent_word(text_list)

    return longest_words, frequent_words


if __name__ == '__main__':
    text = get_text()
    top_length, top_words = get_data_from_text(text)
    print('Наиболее часто встречающееся слово:', ', '.join(top_words))
    print('Самое длинное слово:', ', '.join(top_length))

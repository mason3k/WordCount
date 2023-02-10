import collections
import string
from typing import Final

from nltk.corpus import stopwords

MAX_NUM_DEFAULT: Final[int] = 10


class WordBank:
    """
    A class to represent a collection of words for the purposes of tracking
    and sorting word frequency. Given a set of strings, tokenizes words and
    displays the top (n) most frequent words.

    Attributes
    -------------
        max_num : int
            maximum number of elements to display when printing top words

        word_bank : Counter
            collection of all words in the WordBank and their frequencies

        title: str
            header to display when displaying top words

        stop_words : set
            set of words to ignore when counting word frequencies

        is_empty : Boolean
            true if there are no words in the Wordbank, else false

        top_words : list
            list of the current top [max_num] words

    Methods
    -------------
        append_words(list)
            adds a list of words to the word bank

        add_word(string)
            validates and adds a single word to the word bank

        is_word_legal(string)
            returns whether the word can be added to the word bank
            not falsey, not unprintable, not in stop_words

        print_top_words()
            string representation of the top words by frequency in the
            word bank and the number of appearances
    """

    def __init__(self, max_num=MAX_NUM_DEFAULT):
        self.max_num = max_num
        self.word_bank = collections.Counter()
        # step_words is a list of words to ignore when counting frequencies
        # uses the NLTK stopwords corpus but allows "each" to be included (as in the sample text)
        self.stop_words = set(stopwords.words("english")) - {"each"}
        self.is_empty = True

        self.title = f"--Top {max_num} Words--"
        # replace_table is a translation table to helps strip unwanted characters from words
        self.replace_table = self.__init_replace_table()

    def __str__(self):
        return self.word_bank

    @property
    def top_words(self):
        """Gets current list of top [max_word] words"""
        return self.word_bank.most_common(self.max_num)

    def append_words(self, words):
        """Validates and adds a list of words to the WordBank"""
        for word in words:
            self.add_word(word)

    def add_word(self, word):
        """Validates and adds a single word to the WordBank"""
        sanitized_word = self.sanitize_word(word)
        if self.is_word_legal(sanitized_word) == False:
            return
        self.word_bank[sanitized_word] += 1
        self.is_empty = False

    def is_word_legal(self, word):
        """True if the word is valid to be added to the WordBank, else False

        Removes empty strings, words to ignore from stop_words, and unprintable characters
        """
        if not word or word in self.stop_words:
            return False
        return bool(str.isprintable(word))

    def print_top_words(self):
        """Prints a readable table of the top [max_num] words along with their frequencies"""
        if self.is_empty is True:
            print("No words to analyze found!")
            return

        print(f"{self.title:^45}")
        for entry in self.top_words:
            print("{:<25} {:>20}".format(*entry))

    def sanitize_word(self, word):
        """Converts word to lowercase and strips punctuation besides ' and -
        ' is included so as not to mangle contractions (don't, won't, etc.)
        - is included to prevent hyphenated words from being mangled
        """
        word = word.translate(self.replace_table)
        word = word.lower()
        return word

    @staticmethod
    def __init_replace_table():
        """Initializes a translation table that strips all punctuation besides ' and -"""
        # strip all characters besides ' and - (to avoid mangling words)
        chars_to_strip = string.punctuation.translate(str.maketrans("", "", "'-"))
        strip_punc_dict = {punc: "" for punc in chars_to_strip}
        return str.maketrans(strip_punc_dict)

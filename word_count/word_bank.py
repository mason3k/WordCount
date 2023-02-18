import collections
import string
from typing import Final
from rich.console import Console
from rich.table import Table
from nltk.corpus import stopwords
from itertools import cycle

MAX_NUM_DEFAULT: Final[int] = 10

console = Console()

COLOR_CYCLER = cycle(
    (
        "blue_violet",
        # "blue",
        "dark_turquoise",
        "dark_orange3",
        "magenta",
        "cyan",
    )
)


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

        self._title = f"--Top {max_num} Words--"

    def __str__(self):
        return self.word_bank

    @property
    def top_words(self) -> list[tuple[str, int]]:
        """Gets current list of top [max_word] words"""
        return self.word_bank.most_common(self.max_num)

    def add_words(self, *words: str) -> None:
        """Validates and adds a list of words to the WordBank"""
        for word in words:
            self.add_word(word)

    def add_word(self, word: str) -> None:
        """Validates and adds a single word to the WordBank"""
        sanitized_word = self.sanitize_word(word)
        if self.is_word_legal(sanitized_word):
            self.word_bank[sanitized_word] += 1
            self.is_empty = False

    def is_word_legal(self, word: str) -> bool:
        """True if the word is valid to be added to the WordBank, else False

        Removes empty strings, words to ignore from stop_words, and unprintable characters
        """
        if not word or word in self.stop_words:
            return False
        return bool(str.isprintable(word))

    def print_top_words(self) -> None:
        """Prints a readable table of the top [max_num] words along with their frequencies"""
        if self.is_empty is True:
            print("No words to analyze found!")
            return

        table = Table(title=self._title)
        table.add_column("Word", justify="center")
        table.add_column("Occurrences", justify="center")

        for entry in self.top_words:
            table.add_row(*(str(item) for item in entry), style=next(COLOR_CYCLER))
        console.print(table, justify="center")

    def sanitize_word(self, word: str) -> str:
        """Converts word to lowercase and strips punctuation besides ' and -
        ' is included so as not to mangle contractions (don't, won't, etc.)
        - is included to prevent hyphenated words from being mangled
        """
        punc_to_remove = string.punctuation.replace("'", "").replace("-", "")
        word = word.strip(punc_to_remove)
        word = word.lower()
        return word

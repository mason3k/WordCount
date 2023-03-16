[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge)](https://github.com/pre-commit/precommit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?&style=for-the-badge)](https://pycqa.github.io/isort/)
![GitHub last commit](https://img.shields.io/github/last-commit/mason3k/wordcount?style=for-the-badge)
![Snyk Vulnerabilities for GitHub Repo](https://img.shields.io/snyk/vulnerabilities/github/mason3k/wordcount?style=for-the-badge)

# WordCount

WordCount analyzes word-frequency within a corpus of texts and provides a count of
most-used words.

It allows you to select a text file (or all text files) in a sample
data directory and generates a list of the most common words in those
file(s) along with their usage count.

## Instructions

Per the requirements.txt file, this program requires the nltk and pick packages.
certifi==2020.6.20
pick==1.0.0
wincertstore==0.2
windows-curses==2.1.0
nltk==3.5

Files for analysis should be placed in "./sample_data/"
Only .txt files in this directory will be available for analysis.

Run WordCount.py from the console. You may use the 'up' and 'down' arrow keys
and 'enter' toselect the file you wish to analyze, or select the last option to
analyze all text files within the /sample_data/ directory.

Word processing:
Stopwords are excluded from word frequency analysis. The stopwords this program uses
are based on the NLTK stopwords corpus. See <http://www.nltk.org/nltk_data/>.

Punctuation is stripped from the words with the exception of ', so words like
don't are included.

Note on the pick tool that powers the file selection:
This is not intended to be run from a debugging context, so you may experience
issues if you run this code from an IDE in a debugging mode. It should work as
expected when run from the command line. It can also be run in debug mode in
Visual Studio if you go to Tools > Options > Python > Debugging and uncheck
"Tee Program Output to Debug Output Window." If you continue to have issues,
you can update WordCount.py to call simple_main instead of main.

## Assumptions

1. In my version of the sample, the most frequent number of items seem
 to have their word counts aligned, whereas the later words seem to just
 be tabbed from the word. I assumed this was not part of the specification
 and did not attempt to replicate it.

2. I did not attempt to strip the Project Gutenberg metadata (header and footer
 text/copyright information) for each file, so the words in these headers are
 included in my analysis. This is because there is no guarantee that this metadata
 will remain the same and because I thought it would be more generalizable to trust
 the user to perform any file manipulations prior to uploading the data.

3. I processed each text file in /sample_data/. I excluded files that did not have the
 extension .txt and did not recurse into subdirectories. This is to attempt to
 prevent processing unintended files.

4. The words the sample excluded mostly seemed to line up with the NLTK stopword corpus,
 but I noticed that "each" was included even though it was in the NLTK stopword corpus.
 Accordingly, I have used the corpus but made my own modifications, including getting
 rid of "each" as a stopword.

## Enhancements

- [ ] Handle "-" used when a word wraps a line
- [ ] Handle possessive ' or when used for plurals
- [ ] Cache file analysis between runs

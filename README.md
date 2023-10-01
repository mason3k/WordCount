[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge)](https://github.com/pre-commit/precommit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?&style=for-the-badge)](https://pycqa.github.io/isort/)
![GitHub last commit](https://img.shields.io/github/last-commit/mason3k/wordcount?style=for-the-badge)

# WordCount

WordCount analyzes word-frequency within a corpus of texts and provides a count of
most-used words.

It allows you to select a text file (or all text files) in a sample
data directory and generates a list of the most common words in those
file(s) along with their usage count.

## Instructions

1. Download the source code
1. Create a venv, activate it, and install `requirements.txt` (`pip install -r ./requirements.txt`)
1. Run the following in your shell:

```shell
python
import nltk
nltk.download('stopwords')
```

1. [optional] add files to `./word_count/sample_data`. Only .txt files in this directory will be available for analysis.
1. Run `python -m word_count`
You may use the 'up' and 'down' arrow keys and 'enter' to select the file you wish to analyze, or select the last option to analyze all text files within the `/sample_data/ directory.

### Word Processing

Stopwords are excluded from word frequency analysis. The stopwords this program uses
are based on the NLTK stopwords corpus. See <http://www.nltk.org/nltk_data/>.

Punctuation is stripped from the words with the exception of ', so words like
don't are included.

### Troubleshooting

The `pick` tool is not intended to be run from a debugging context, so you may experience issues if you run this code from an IDE in a debugging mode. It should work as expected when run from the command line. It can also be run in debug mode in Visual Studio if you go to Tools > Options > Python > Debugging and uncheck "Tee Program Output to Debug Output Window." If you continue to have issues, you can update `word_count.py` to call `simple_main` instead of `main`.

## Assumptions

1. I did not attempt to strip the Project Gutenberg metadata (header and footer text/copyright information) for each file, so the words in these headers are included in my analysis. This is because there is no guarantee that this metadata will remain the same and because I thought it would be more generalizable to trust the user to perform any file manipulations prior to uploading the data.

1. I processed each text file in `/sample_data/`. I excluded files that did not have the extension `.txt` and did not recurse into subdirectories.This is to attempt to prevent processing unintended files.

## Enhancements

- [ ] Handle "-" used when a word wraps a line
- [ ] Handle possessive ' or when used for plurals
- [ ] Cache file analysis between runs

"""
A word frequency analyzer implemented in Python.

Allows user to select a text file (or all text files) in a sample
data directory and generates a list of the most common words in those
file(s) along with their usage count.
"""

from pathlib import Path

from pick import pick

from .word_bank import WordBank
from rich.prompt import Confirm
from typing import Optional

from .word_bank import COLOR_CYCLER
from .word_bank import console


def main():
    """Main entrypoint into repeated user prompting and processing"""
    cont = True
    while cont:
        try:
            cont = interactive_main()
            if not cont:
                break
        except Exception as e:
            print(f"Error: {e}")
            cont = False


def simple_main():
    """A simplified entrypoint that processes all the files in the
    provided directory a single time without user input
    """
    word_bank = WordBank()

    if not scan_files(word_bank):
        print("No files found to analyze!")
        return

    word_bank.print_top_words()


def interactive_main():
    """Prompts for file selection, analyzes and displays word counts, and
    asks user whether to continue

    returns True if user has selected to continue, else False
    """
    # Initialize WordBank to track most common words
    word_bank = WordBank()

    filepath = get_file_from_user()

    if filepath == "":
        print("No file found!")
        return False
    elif filepath == "ALL":
        process_files(word_bank)
    else:
        process_files(word_bank, filepath)

    # Output most common words
    print("\n" * 2)
    word_bank.print_top_words()

    return Confirm.ask("Results complete. Run another analysis?")


def get_file_from_user():
    """Prompts user for filepath from directory to analyze, or whether to analyze all files in directory

    returns one of:
           - [the selected absolute filepath] to analyze a single file
           - "ALL" to analyze all files in directory
           - "" if there are no files in the directory
    """
    options = []
    cntr = 0
    prompt = "Select a file to process (using arrow keys):"

    # Print user-selectable options for all files in ./sample data
    for file in (Path(__file__).parent / "sample_data").glob("*.txt"):
        cntr += 1
        absolute_filepath = file.resolve()
        label = format_label(cntr, file.name)
        # options object is used by pick to populate the picklist
        #'label' is what is displayed to the user and 'filepath' is what will be returned if user selects this option
        options.append({"label": label, "filepath": absolute_filepath})
    if cntr == 0:
        # No files in ./sample_data
        return ""

    cntr += 1
    # Always show the user the option to select all files in directory
    options.append({"label": format_label(cntr, "All files in directory"), "filepath": "ALL"})

    selected = pick(options, prompt, indicator="=>", options_map_func=get_label)
    return selected[0].get("filepath")


def get_label(option: dict) -> str:
    return option.get("label")


def format_label(cntr, name: str) -> str:
    return f"{cntr}. {name:.40}"


def process_files(word_bank: WordBank, filepath: Optional[Path] = None) -> bool:
    """Traverses the /sample_data/ directory and performs word count analysis on each f
    ile in the directory

    Arguments:
    filepath -- the absolute filepath of the file to analyze. If None, process
    all files in the sample directory

    returns True if any files were successfully processed, else False
    """
    processed_file_cnt = 0
    if filepath is not None:
        files = [filepath]
    else:
        files = (Path(__file__).parent / "sample_data").glob("*.txt")

    for file in files:
        console.print("{}{:.45}{}".format("Analyzing ", file.name, "..."), style=next(COLOR_CYCLER))
        try:
            process_one_path(word_bank, file)
            processed_file_cnt += 1
        except Exception as e:
            console.print(f"Error processing {file}: {e}", style="white", highlight="red")
    return processed_file_cnt > 0


def process_one_path(word_bank: WordBank, filepath: Path):
    """Opens the given absolute filepath, reads in the file, and updates the WordBank
    with the words from the file

    Arguments:
    filepath -- the absolute filepath of the file to analyze
    word_bank -- the object containing data about the frequency of word appearances

    raises io exceptions
    """

    with filepath.open(encoding="utf-8") as f:
        while line := f.readline():
            words = line.split()
            # populate WordBank with words from this line
            # WordBank handles casing, stripping punctuation, stopwords, unprintable chars, etc.
            word_bank.add_words(*words)

# obtain a list of files in the input directory

# obtain a list of files in the input directory
import os

from ._internals.count_words import count_words
from ._internals.preprocess_lines import preprocess_lines
from ._internals.read_all_lines import read_all_lines
from ._internals.split_in_words import split_in_words
from ._internals.write_count_words import write_count_words

read_all_lines()
preprocess_lines()
split_in_words()
count_words()
write_count_words(counter)

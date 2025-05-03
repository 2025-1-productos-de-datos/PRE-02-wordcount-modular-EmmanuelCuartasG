def split_in_words():
    ## mover "split_in_words"
    words = []
    for line in all_lines:
        words.extend(word.strip(",.!?") for word in line.split())

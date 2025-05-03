def count_words(words):
    ## mover a "count_words"
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    return counter

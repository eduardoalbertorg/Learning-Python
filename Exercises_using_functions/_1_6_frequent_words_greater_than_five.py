def get_most_frequent_words(word_list):
    unique_word = set(word_list)
    word_frequency = {word:word_list.count(word) for word in unique_word if word_list.count(word) >= 5}
    return [word_frequency]
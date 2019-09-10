def return_word_count(word_list):
    '''
    Returns a dictionary with each word and the count number
    '''
    unique_word = set(word_list)
    word_frequency = {word:word_list.count(word) for word in unique_word}
    return [word_frequency]
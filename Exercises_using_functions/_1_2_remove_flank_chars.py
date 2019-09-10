def remove_from_word_list(word_list):
    '''
    Now, remove the flanking characters (such as , . - * ! and space)
    from each of the word, present in list words.
    '''
    return [word.strip(',.-*! ') for word in word_list]
def remove_duplicates(word_list):
    '''
    Remove duplicates by placing them into a set,
    and then turning it back into a list
    '''
    return list(set(word_list))
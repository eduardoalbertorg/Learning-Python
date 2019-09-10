import _1_1_separate_into_words as _1_1_separate_into_words
import _1_2_remove_flank_chars as _1_2_remove_flank_chars
import _1_3_convert_to_lowercase as _1_3_convert_to_lowercase
import _1_4_unique_words as _1_4_unique_words

zenPython = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

def main():
    word_list = _1_1_separate_into_words.convert_to_word_list(zenPython)
    word_list = _1_2_remove_flank_chars.remove_from_word_list(word_list)
    word_list = _1_3_convert_to_lowercase.to_lower(word_list)
    word_list = _1_4_unique_words.remove_duplicates(word_list)
    print(word_list)

if __name__ == '__main__':
    main()
from operator import itemgetter

def get_num_words(text):
    num_words = len(text.split())
    print(f'Found {num_words} total words')

def get_count_by_letter(text):
    count = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in count:
            count[lower_char] = 0
        count[lower_char] += 1
    return count
    
def sort_on(dict):
    return dict["num"]

def get_char_dictionary(text):
    count = get_count_by_letter(text)
    char_list = []
    for char in count:
        char_list.append({
            'char': char,
            'num': count[char]
        })
    
    char_list.sort(reverse=True, key=sort_on)
    for char in char_list:
        if(not char['char'].isalpha()):
            continue
        print(f"{char['char']}: {char['num']}")
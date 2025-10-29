
def get_book(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def num_of_words(text):
        word_list = text.split()
        num_words = len(word_list)
        print (f"Found {num_words} total words")

def num_of_char(text):
    char_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in char_dict:
            char_dict[char]+=1
        else:
            char_dict[char]=1
    return char_dict

def sort_on(items):
    return items["num"]


def dict_sort(dict):
    list_of_dict = []
    for key, value in dict.items():
        new_dict = {}
        new_dict["char"]=key
        new_dict["num"]=value
        list_of_dict.append(new_dict)
    list_of_dict.sort(reverse=True, key=sort_on)
    for item in list_of_dict:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

        
        


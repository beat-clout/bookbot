def get_num_words(text):
        words = text.split()
        return len(words)

def letter_count(text):
        all_text = text.lower()
        letter_dict = {}
        #loop through each chatacter
        for char in all_text:
            if char.isalpha():
                letter_dict[char] = letter_dict.get(char, 0) + 1
        return letter_dict

def transform_and_sort(letter_dict):
        #transform dictionary into list of dictionaries
        letter_list = [ {"char": char, "count": count} for char, count in letter_dict.items() ]
        #sort list of dictionaries by count in descending order
        letter_list.sort(reverse=True, key=lambda item: item["count"])
        return letter_list
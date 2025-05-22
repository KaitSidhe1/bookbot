def get_num_words(file_contents):
    return len(file_contents.split())

def get_per_char_count(file_contents):
    per_char_count = {}
    for char in file_contents.lower():
        if per_char_count.get(char):
            per_char_count[char] = per_char_count[char] + 1
        else:
            per_char_count[char] = 1
    return per_char_count

def sort_on(dict):
	    return dict["num"]

def get_sorted_count(per_char_count):
    counts = []
    for key, value in per_char_count.items():
        counts.append({"char": key, "num": value})
               
    counts.sort(reverse=True, key=sort_on)
    

    return counts

    


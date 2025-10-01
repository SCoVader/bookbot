def get_num_words(text):
    count = 0
    count = len(text.split())
    return count

def sym_count(text):
    stats = {}
    text = text.lower()
    for sym in text:
        if sym not in stats:
            stats[sym] = 1
        else:
            stats[sym]+=1
    return stats

def sort_on(item):
    return item["num"]

def prettify_sym_count(dictionary):
    pretty = []
    for key in dictionary:
        pretty.append({"char": key, "num": dictionary[key]})
    pretty.sort(reverse=True, key=sort_on)
    return pretty

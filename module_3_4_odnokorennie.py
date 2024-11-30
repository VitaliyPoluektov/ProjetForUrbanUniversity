def single_root_words(root_word, *other_words):
    same_words = []
    rw = root_word.upper()
    for i in range(len(other_words)):
        ow = other_words[i].upper()
        if rw == ow or \
        (len(rw) < len(ow) and ow.find(rw) != -1) or \
        (len(rw) > len(ow) and rw.find(ow) != -1):
            same_words.append(other_words[i])
    return same_words


print(single_root_words('корен', 'коренной', 'кора', 'береза', 'коренья', 'кор', 'корен'))
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
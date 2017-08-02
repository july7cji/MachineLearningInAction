# -*- coding: utf-8 -*-

# 按pattern中的标点符号分隔句子，并且保留分隔的标点                                                                                                                   
def my_split(s, pattern):
    result = []
    w = ''
    for c in s:
        if c not in pattern:
            w += c
        else:
            w += c
            if w in pattern: # 如果分割开后的仍然是一个符号，例如感叹号，说明有多个感叹号连在一起了，保留
                w = result[-1] + w 
                del result[-1]
            if w.strip() != "": 
                result.append(w)
                #print w
            w = ''
    if w.strip() != '': 
        result.append(w)
    return result

sents = my_split(sentence, ur"，。？！；,?!; ")

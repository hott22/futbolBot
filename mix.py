import random

def mix_list(list_original):
    listt = list_original[:]
    list_length = len(listt)
    for i in range(list_length):
        index_aleatory = random.randint(0, list_length - 1)
        temp = listt[i]
        listt[i] = listt[index_aleatory]
        listt[index_aleatory] = temp

    return listt



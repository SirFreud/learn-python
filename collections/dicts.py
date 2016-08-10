def word_count(string):
    my_dict = {}
    for word in string.split():
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return my_dict
st = "I am a cat in a tree"
my_var = word_count(st)
print(my_var)
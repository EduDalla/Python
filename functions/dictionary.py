dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
words = ['gato', 'lion', 'cavalo']

for word in words: # we only use for using "in" or "not in" to navegate around the dictionary
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "não está no dicionário")

# Another example

# dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
#
# for key in dictionary.keys():
#     print(key, "->", dictionary[key])

#   Adding a new vocabulary
#
# dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
#
# dictionary['swan'] = 'cygne' # or use dictionary.update({"swan": "cygne"})
# print(dictionary)

words = ['мадам', 'топот', 'тест', 'madam', 'word']
new_words = [i for i in words if i == i[::-1]]
print(new_words)
new2_words = []
for i in words:
    if i == i[::-1]:
        new2_words.append(str(i))
print(new2_words)

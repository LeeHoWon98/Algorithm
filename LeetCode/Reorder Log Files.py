logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", 
       "let3 art zero"]

word, digi = [], []

for i in logs:
    if i.split()[1].isdigit():
        digi.append(i)
    else:
        word.append(i)

word.sort(key=lambda x: (x.split()[1:], x.split()[0]))

print(word+digi)
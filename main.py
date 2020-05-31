f = open('words_alpha.txt', 'r+')
lines = [line for line in f.readlines()]
f.close()
word_list =list(map(lambda s: s.strip(), lines))


disallowed_chars = ["g","k","m","q","v","w","x"]
length = 0
longest_word= str()


for i in word_list:
    if len(i)>length:
        if not set(i).issubset(disallowed_chars):
            longest_word = i
            length = len(i)

print(longest_word)

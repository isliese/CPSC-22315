s = input("Enter the string : ")
word_list = s.split()

for word in word_list:
    word = word[::-1]
    print(word, end=" ")
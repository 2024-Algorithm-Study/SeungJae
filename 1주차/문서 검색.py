# **idea**
# slicing, 문자열의 인덱스 접근 이용

text = input()
word = input()

def search(text, word):
    count = 0
    i = 0
    while i < len(text):
        if text[i:i+len(word)] == word:
            count += 1
            i += len(word)
            continue
        
        i += 1
    return count

print(search(text, word))
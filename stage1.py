def solution(x):
    # Your code here
    words = x.split()
    decrypted = []
    for word in words:
        decrypted_words = []
        for letter in word:
            if ord(letter) >= 97 and ord(letter) <=122:
                decrypted_words.append(chr(97+(122-ord(letter))))
            else:
                decrypted_words.append(letter)
        decrypted.append(''.join(decrypted_words))
    return ' '.join(decrypted)
# Driver
print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))

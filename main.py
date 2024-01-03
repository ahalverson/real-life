import pyotp
import time
import nltk
from nltk.corpus import words

nltk.download('words')

word_list = words.words()

totp = [0 for i in range(6)]
sentence = ['' for i in range (6)]
keys = ['' for i in range (6)]

for i in range(0, 6):
    keys[i] = pyotp.random_base32()
    totp[i] = pyotp.TOTP(keys[i])
    print(totp[i].now())
    sentence[i] = word_list[int(totp[i].now()) % len(word_list)]

print ("Keys: \n\n")
for k in keys:
    print(k)

print(sentence)

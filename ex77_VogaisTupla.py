import re
words = ('batata', 'pii')
for x in range(len(words)):
    print(f'Word {words[x]} contains {re.findall(r"[aeiou]", words[x], re.IGNORECASE)}')

"""
for p in words:
    print(words)
    for letra in p :
        if letra in 'aeiou:
        print(letra)
"""

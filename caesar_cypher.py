# Secret Message app

alpha = "abcdefghijklmnopqrstuvwxyz"


def encrypt(cleartext):
    """a """
    cyphertext = ""
    for char in cleartext:
        if char in alpha:
            newpos = (alpha.find(char) + 12) % 26
            cyphertext += alpha[newpos]
        else:
            cyphertext += char

    return cyphertext


cleartext = input("Clear text: ")
# this next line help to support upper characters by converting them to lower.
cleartext = cleartext.lower()

print(encrypt(cleartext))

def clay(*strings, kley='-=-'):
    text = ''
    for string in strings:
        text += string + kley
    text = text[0:-len(kley)]
    return text


a = clay('lol', 'kek', 'azaza', 'pup', 'dodo', kley=' @ ')
print(a)

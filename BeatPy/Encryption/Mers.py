from util.core import Process


def encrypt(text=None, key=None):
    if key is None:
        cleared = text.replace('&', '').replace('é', '').replace('#', '').replace('@', '').replace('(', '')\
            .replace('§', '').replace('è', '').replace('!', '').replace('ç', '').replace('à', '')
        letters = Process.ltn(cleared, True)
        flipped = letters[::-1]
        convert = Process.ntl(flipped)
        return convert
    else:
        pass


def decrypt(text=None, key=None):
    if key is None:
        convert = Process.ltn(text)
        flipped = convert[::-1]
        letters = Process.ntl(flipped)
        return letters
    else:
        pass

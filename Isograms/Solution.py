def is_isogram(string):
    return len(string) == len(set(string.lower()))

if __name__ == '__main__':
    print(is_isogram('Dermatoglyphics'))
    print(is_isogram('isogram'))
    print(is_isogram('aba'))
    print(is_isogram('moOse'))
    print(is_isogram('isIsogram'))
    print(is_isogram(''))


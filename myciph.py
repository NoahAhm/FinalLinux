def SimpleCeasarCipher(shift):
    string = input("Enter your statement: ")
    myascii = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
        'N': 14,
        'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26,
        1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M',
        14: 'N',
        15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
    }
    new = ''
    for i in string:
        if i.isalpha():
            key = 26 - shift
            if myascii[i.upper()] > key:
                new += myascii[myascii[i.upper()] - key]
            else:
                new += myascii[myascii[i.upper()] + shift]
    newest = ''
    for x in range(0, len(new), 5):
        if x != 0 and x % 50 == 0:
            newest += '\n'
        newest = newest + new[x: x + 5] + " "
    return newest

if __name__ == '__main__':
    import sys
    shift = int(sys.argv[1])
    result = SimpleCeasarCipher(shift)
    print(result)

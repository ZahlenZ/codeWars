from itertools import groupby

#1 Takes as argument a string and returns a list of items without repeated elements and retaining order

def unique_in_order(iterable: str) -> list:
    return [k for (k, _) in groupby(iterable)]

unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]

def unique_in_order(iterable: str) -> list:
    return [ ch for i, ch in enumerate(iterable) if i == 0 or ch != iterable[i - 1] ]


#2 Takes as argument a string of space separated numbers, return the highest and lowest

def high_and_low(numbers: str) -> str:

    numbers = [int(x) for x in numbers.split()]
    
    return f'{max(numbers)} {min(numbers)}'


# 3 square every digit in a sequence and concatenate

def square_digits(num: int) -> int:
    return int(''.join(str(int(d)**2) for d in str(num)))
    

# 4 decode morse strings (Dictionary MORSE_CODE was provided)

def decode_morse(morse_code: str) -> str:
    
    MORSE_CODE = dict()
    translate = lambda code: ''.join(MORSE_CODE.get(morse) for morse in re.split(r' ', code))
    
    words = re.split(r'  ', morse_code.strip())
    
    translated_words = [translate(word.strip()) for word in words]
    
    return ' '.join(translated_words)
    
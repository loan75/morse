# morse.py
# pylint: disable=missing-docstring
MORSE_CODE = {
    '.-':   'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..':  'D',
    '.':    'E',
    '..-.': 'F',
    '--.':  'G',
    '....': 'H',
    '..':   'I',
    '.---': 'J',
    '-.-':  'K',
    '.-..': 'L',
    '--':   'M',
    '-.':   'N',
    '---':  'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.':  'R',
    '...':  'S',
    '-':    'T',
    '..-':  'U',
    '...-': 'V',
    '.--':  'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z'
}

def decode(message):
    if message == '':
        return ''
    else:
        return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in message.strip().split(' / '))
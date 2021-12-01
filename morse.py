"""Morse Code Translator"""
import doctest
import pytest

LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}

MORSE_TO_LETTER = {
    morse: letter
    for letter, morse in LETTER_TO_MORSE.items()
}


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе

    >>> encode('SOS')
    '... --- ...'
    >>> encode('EARLY TO BED AND EARLY TO RISE MAKES A MAN HEALTHY WEALTHY AND WISE')
    '. .- .-. .-.. -.--   - ---   -... . -..   .- -. -..   . .- .-. .-.. -.--   - ---
       .-. .. ... .   -- .- -.- . ...   .-   -- .- -.   .... . .- .-.. - .... -.--
       .-- . .- .-.. - .... -.--   .- -. -..   .-- .. ... .'
    >>> encode('hi')# doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    KeyError: 'h'
    >>> encode(True)# doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: 'bool' object is not iterable
    """

    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)


def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    """
    decoded_letters = [
        MORSE_TO_LETTER[letter] for letter in morse_message.split()
    ]

    return ''.join(decoded_letters)


@pytest.mark.parametrize("test_input,expected", [
    ('... --- ...', 'SOS'),
    ('.... ..', 'HI'),
    ('- . ... -', 'TEST')
])
def test_decode(test_input, expected):
    """
    Проверяет работу функции decode
    """
    assert decode(test_input) == expected


if __name__ == '__main__':
    morse_msg = '-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.'
    decoded_msg = decode(morse_msg)
    print(decoded_msg)
    assert morse_msg == encode(decoded_msg)
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
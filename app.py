MORSE_CODE = {
    "a": '.-',
    "b": '-...',
    "c": '-.-.',
    "d": '-..',
    "e": '.',
    "f": '..-.',
    "g": '--.',
    "h": '....',
    "i": '..',
    "j": '.---',
    "k": '-.-',
    "l": '.-..',
    "m": '--',
    "n": '-.',
    "o": '---',
    "p": '.--.',
    "q": '--.-',
    "r": '.-.',
    "s": '...',
    "t": '-',
    "u": '..-',
    "v": '...-',
    "w": '.--',
    "x": '-..-',
    "y": '-.--',
    "z": '--..',
    "1": '.----',
    "2": '..---',
    "3": '...--',
    "4": '....-',
    "5": '.....',
    "6": '-....',
    "7": '--...',
    "8": '---..',
    "9": '----.',
    "0": '-----',
    " ": '/'}


def encode(text):
    output = ""
    # Check is symbol in the entry. If it is a letter, convert to lower case
    for s in text:
        if s.isalpha():
            s = s.lower()
        # Check if symbol is in the Morse Code dictionary
        try:
            encoded_s = MORSE_CODE[s]
        # If symbol is not found, pass
        except KeyError:
            pass
        # If symbol is in dictionary, add it to the output string
        else:
            output += encoded_s + " "

    # Print the output string
    print(f"\nOUTPUT: \n{output}")


def text_accepted(text):
    if input_text == '@':
        return False
    else:
        return True


def is_morse(text):
    for char in text:
        if char in [".", "-", "/", " "]:
            it_is_morse = True
        else:
            it_is_morse = False
        return it_is_morse


def decode(text):
    decoded_word = ""
    list_of_chars = text.split(" ")
    for char in list_of_chars:
        for sym in MORSE_CODE:
            if MORSE_CODE[sym] == char:
                decoded_char = sym
                decoded_word += decoded_char
    # Print the output string
    print(f"\nOUTPUT: \n{decoded_word}")


def need_another_encoding():
    response_received = False
    while not response_received:
        response = input("\nNeed More Encoding/Decoding? Y/N: ").lower()
        if response == "n":
            return False
        elif response == "y":
            print("\n\n/////////// NEW ENCODING ///////////")
            return True


# set while variable
need_encoding = True

# While encoding is needed, request input
while need_encoding:
    print("---Type @ to quit---")
    input_text = input("\nINPUT:\n")

    # Check if user wants to quit or encode/decode
    if text_accepted(input_text):
        # Check if input is text or morse code
        if is_morse(input_text):
            decode(input_text)
        else:
            encode(input_text)
    else:
        break

    # Does user want to do another decoding/encoding session?
    need_encoding = need_another_encoding()

print("\n//////////// Good Bye! /////////////")

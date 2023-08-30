from replit import clear
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


def is_morse(input_text):
    for char in input_text:
        if char in [".", "-", "/", " "]:
            it_is_morse = True
        else:
            it_is_morse = False
        return it_is_morse


def decode(input_text):
    decoded_word = ""
    list_of_chars = input_text.split(" ")
    print(list_of_chars)
    for char in list_of_chars:
        for sym in MORSE_CODE:
            if MORSE_CODE[sym] == char:
                decoded_char = sym
                decoded_word += decoded_char
    print(decoded_word)





# set while variable
need_encoding = True

# While encoding is needed, request input
while need_encoding:
    print("---Type @ to quit---")
    input_text = input("\nINPUT: ")

    # Check if user wants to quit or encode/decode
    if text_accepted(input_text):
        # Check if input is text or morse code
        if is_morse(input_text):
            decode(input_text)
        else:
            encode(input_text)
    else:
        break





    # Does user need another decoding/encoding?
    response = ""
    if response != "Y" or response != "N":
        response = input("\nNeed More Encoding/Decoding? Y/N: ")
        if response == "N":
            need_encoding = False
        elif response == "Y":
            clear()
            print("\n\n/////////// NEW ENCODING ///////////")
            need_encoding = True


print("\n//////////// Good Bye! /////////////")




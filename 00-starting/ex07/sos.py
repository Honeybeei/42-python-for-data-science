from sys import argv


def is_valid_input_str(input_str: str) -> bool:
    """Check if the input string is valid

    Args:
        input_str (str): The input string

    Returns:
        bool: True if the input string has only alphanumeric characters and
        spaces, False otherwise
    """
    for c in input_str:
        if not c.isalnum() and c != " ":
            return False
    return True


def char_to_morse(char: str) -> str:
    """Convert a character to morse code

    Args:
        char (str): The character to convert

    Returns:
        str: The morse code for the character
    """
    # Check if the input is valid
    if not char.isalnum() and char != " " or len(char) != 1:
        raise AssertionError(
            "Input should be an alphanumeric character or a \
space"
        )
    morse_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        " ": "\\ ",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
    }
    return morse_dict[char.upper()]


def main():
    """This is the main function"""
    try:
        # check args
        args = argv
        if len(args) != 2:
            raise AssertionError("There should be a single argument")
        str_to_convert = args[1]
        if not is_valid_input_str(str_to_convert):
            raise AssertionError(
                "Argument string only should have alphanumeric characters and \
spaces"
            )
        else:
            morse_str = " ".join([char_to_morse(c) for c in str_to_convert])
            print(morse_str)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)


if __name__ == "__main__":
    main()

from sys import argv


def count_uppercase_letters(string: str) -> int:
    """This function counts the number of uppercase letters in a string

    Args:
        string (str): The string to parse

    Returns:
        int: The number of uppercase letters
    """
    count = 0
    for char in string:
        if char.isupper():
            count += 1
    return count


def count_lowercase_letters(string: str) -> int:
    """This function counts the number of lowercase letters in a string

    Args:
        string (str): The string to parse

    Returns:
        int: The number of lowercase letters
    """
    count = 0
    for char in string:
        if char.islower():
            count += 1
    return count


def count_punctuation(string: str) -> int:
    """This function counts the number of punctuation characters in a string

    Args:
        string (str): The string to parse

    Returns:
        int: The number of punctuation characters
    """
    count = 0
    for char in string:
        if not char.isalnum() and not char.isspace():
            count += 1
    return count


def count_spaces(string: str) -> int:
    """This function counts the number of spaces in a string

    Args:
        string (str): The string to parse

    Returns:
        int: The number of spaces
    """
    count = 0
    for char in string:
        if char.isspace():
            count += 1
    return count


def count_digits(string: str) -> int:
    """This function counts the number of digits in a string

    Args:
        string (str): The string to parse

    Returns:
        int: The number of digits
    """
    count = 0
    for char in string:
        if char.isdigit():
            count += 1
    return count


def get_string_from_user() -> str:
    """This function gets a string from the user

    Raises:
        AssertionError: If there are too many arguments (more than 1)

    Returns:
        str: The string to parse
    """
    str_to_return = ""
    # check argc
    arguments = argv
    if len(arguments) == 1:
        str_to_return = input("Give me the text to parse.\n")
    elif len(arguments) == 2:
        str_to_return = argv[1]
    else:
        raise AssertionError("Too many arguments")
    return str_to_return


def main():
    """This is the main function"""
    try:
        str_to_parse = get_string_from_user()
        print(f"Total characters  : {len(str_to_parse)}")
        print(f"Uppercase letters : {count_uppercase_letters(str_to_parse)}")
        print(f"Lowercase letters : {count_lowercase_letters(str_to_parse)}")
        print(f"Punctuations      : {count_punctuation(str_to_parse)}")
        print(f"Spaces            : {count_spaces(str_to_parse)}")
        print(f"Digits            : {count_digits(str_to_parse)}")

    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)


if __name__ == "__main__":
    main()

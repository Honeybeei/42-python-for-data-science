from sys import argv
from ft_filter import ft_filter


def main():
    """This is the main function"""
    try:
        args = argv
        # Check arguments
        if not len(args) == 3:
            raise AssertionError("Please provide two argument")
        if not args[2].isdigit():
            raise AssertionError("Second argument should be a positive int")
        input_string = args[1]
        input_integer = int(args[2])
        splitted_words = input_string.split()
        filtered_result = ft_filter(
            lambda word: len(word) > input_integer, splitted_words
        )
        print(filtered_result)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)


if __name__ == "__main__":
    main()

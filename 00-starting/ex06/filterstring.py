from sys import argv


def main():
    """This is the main function"""
    try:
        args = argv
        if not len(args) == 3:
            raise AssertionError("Please provide two argument")
        print(args)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)


if __name__ == "__main__":
    main()

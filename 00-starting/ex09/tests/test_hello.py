from ft_package.hello import say_hello


def main():
    """This is the main function"""
    print(say_hello.__doc__)
    say_hello()


if __name__ == "__main__":
    main()

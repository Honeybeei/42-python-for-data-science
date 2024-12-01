from ft_package.count import count_in_list


def main():
    """This is the main function"""
    print(count_in_list.__doc__)
    print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
    print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0


if __name__ == "__main__":
    main()

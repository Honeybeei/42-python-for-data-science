from ft_package import *


def main():
    """This is the main function"""
    say_hello()
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 5
    print(
        f"The number of times {target} appears in the list is {count_in_list(lst, target)}"
    )


if __name__ == "__main__":
    main()

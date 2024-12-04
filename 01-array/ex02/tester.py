from load_image import ft_load


def main():
    """This is the main function"""
    try:
        print(ft_load("../../images/animal.jpeg"))
        print(ft_load("../../images/landscape.jpg"))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

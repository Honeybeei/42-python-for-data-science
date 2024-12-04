from load_image import ft_load


def main():
    """This is the main function"""
    image = ft_load("../../images/animal.jpeg")
    print(image)
    # zoomed_image = zoom(image) # TODO


if __name__ == "__main__":
    main()

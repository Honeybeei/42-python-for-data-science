from give_bmi import give_bmi, apply_limit


def main():
    try:
        """This is the main function"""
        height = [2.71, 1.15]
        weight = [165.3, 38.4]

        bmi = give_bmi(height, weight)

        print(bmi, type(bmi))

        print(apply_limit(bmi, 26))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()

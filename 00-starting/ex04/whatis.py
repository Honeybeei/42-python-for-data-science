import sys

args = sys.argv

try:
    # Check if there are more than one argument
    if len(args) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(args) < 2:
        sys.exit(0)

    # Check if the argument is an integer
    if not args[1].isdigit() and not args[1][0] == "-":
        raise AssertionError("argument is not an integer")
except AssertionError as e:
    print(f"AssertionError: {e}")
    sys.exit(1)

number = int(args[1])
print(number)

if number % 2 == 0:
    print("I'm Even")
else:
    print("I'm Odd")

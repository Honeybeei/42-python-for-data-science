ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Handle list (list is mutable)
ft_list.pop()
ft_list.append("World!")

# Handle tuple (tuple is immutable)
ft_tuple = ("Hello", "Germany!")

# Handle set (set is mutable)
ft_set.remove("tutu!")
ft_set.add("Wolfsburg!")

# Handle dict (dict is mutable)
ft_dict["Hello"] = "42Wolfsburg!"


def print_set_in_order(s: set):
    # Set is unordered, so we need to sort it before printing
    ordered_list_str = str(sorted(s))
    translation_table = str.maketrans("[]", "{}")
    print(ordered_list_str.translate(translation_table))


print(ft_list)
print(ft_tuple)
print_set_in_order(ft_set)
print(ft_dict)

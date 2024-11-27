def all_thing_is_obj(object: any) -> int:
    type_of_object = type(object)
    if type_of_object == str:
        print(f"{object} is in the kitchen : {type_of_object}")
    elif (
        type_of_object == dict
        or type_of_object == set
        or type_of_object == list
        or type_of_object == tuple
    ):
        capitalized_type_name = type_of_object.__name__.capitalize()
        print(f"{capitalized_type_name} : {type_of_object}")
    else:
        print("Type not found")
    return 42

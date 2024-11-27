from types import NoneType


def NULL_not_found(object: any) -> int:
    object_type = type(object)
    head_str = ""
    if object_type == NoneType:
        head_str = "Nothing"
    elif object_type == float:
        head_str = "Cheese"
    elif object_type == int:
        head_str = "Zero"
    elif object_type == str and object == "":
        head_str = "Empty"
    elif object_type == bool:
        head_str = "Fake"
    else:
        print("Type not Found")
        return 1
    print(f"{head_str}: {object} {object_type}")
    return 0

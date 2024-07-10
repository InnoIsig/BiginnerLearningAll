def format_name(f_name, l_name):
    format_f_name = f_name.title()
    format_l_name = l_name.title()

    return f"{format_f_name} {format_l_name}"

final_name = format_name(input("Quel est ton nom ? "), input("Quel est ton post-nom ? "))
print(final_name)
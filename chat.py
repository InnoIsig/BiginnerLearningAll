line1 = ["⬜", "⬜", "⬜"]
line2 = ["⬜", "⬜", "⬜"]
line3 = ["⬜", "⬜", "⬜"]

map = [line1, line2, line3]
print("Handing your treasure! X markers the spot")

position = input("Where do you put the treasure? ").strip()  # Strip any leading/trailing spaces

if len(position) != 2:
    print("Error: Input should be exactly 2 characters long (a letter and a number).")
else:
    letter = position[0].lower()
    number = position[1]

    abc = ["a", "b", "c"]

    if letter not in abc:
        print(f"Error: '{letter}' is not a valid column (should be 'A', 'B', or 'C').")
    elif not number.isdigit() or int(number) not in range(1, 4):
        print(f"Error: '{number}' is not a valid row (should be '1', '2', or '3').")
    else:
        letter_index = abc.index(letter)
        number_index = int(number) - 1

        map[number_index][letter_index] = "X"

        for line in map:
            print(" ".join(line))
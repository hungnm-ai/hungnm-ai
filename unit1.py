input_str = 'Hello "world'
Input_str_reversed =      ""
print("len(input_str): ", len(input_str))

for idx in range(len(input_str) - 1, -1, -1):# start, end, step
    print("idx: ", idx)
    char = input_str[idx]
    Input_str_reversed += char
print(Input_str_reversed)

for idx in range(10, 20, 2):
    print("idx: ", 10)
print(
    "This is a very long line of code that exceeds the maximum line length specified by flake8, and therefore would generate a warning."
)

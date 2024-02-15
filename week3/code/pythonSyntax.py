try:
    with open('file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('\033[31mNo such file\033[0m')
else:
    print('\033[32mFile content: \033[0m', content)

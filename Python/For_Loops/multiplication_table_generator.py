num = int(input("Table of what number do you want?: "))
table_range = int(input("Till what number, do you want the table?: "))

for i in range(1, table_range + 1):
    print(f'{num} x {i} = {num * i}')
star = '*'
space = ' '
bar = '|'

def make_tree(rows):
    rows_to_do = rows
    stars_in_row = 1
    tree = ''

    while rows_to_do > 0:
        tree += bar + space * (rows_to_do - 1) + star * stars_in_row + space * (rows_to_do - 1) + bar + '\n'
        stars_in_row += 2
        rows_to_do -= 1

    tree += bar + space * (rows - 1) + bar + space * (rows - 1) + bar
    return tree

num_rows = int(input("Enter the number of rows for the Christmas tree: "))
print(make_tree(num_rows))
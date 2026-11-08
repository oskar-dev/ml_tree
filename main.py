def load(path: str, separator: str) -> list:
    table = []
    with open(path, "r") as file:
        for line in file:
            table.append(line.replace("\n", "").split(separator))

    file.close()

    return table


def read_column(data: list, col: int) -> list:
    buf = []
    for y in range(len(data)):
        row = data[y]
        buf.append(row[col])
    return buf


def count_unique_attr_column(data: list, col: int) -> int:
    buf = read_column(data, col)

    return len(set(buf))


def count_attr_value_column(data: list, col: int) -> dict:
    buf = read_column(data, col)

    count_table = {}

    for key in list(set(buf)):
        count_table[key] = 0

    for value in buf:
        count_table[value] += 1

    return count_table


def print_table(data: list, headers: list) -> None:
    print("\t".join(headers))

    for row in data:
        print("\t".join(row) + "\n")


basic_headers = ["a1", "a2", "a3", "a4", "d"]
basic_list = load("basic_data.txt", " ")

print("========= BASIC DATA =========")
print_table(basic_list, basic_headers)
for i in range(4):
    print(f"Unique count column: ({i}): ", count_unique_attr_column(basic_list, i))
    print(f"Value count column: ({i}): ", count_attr_value_column(basic_list, i))

print("========= ADVANCED DATA =========")
advanced_list = load("advanced_data.txt", ";")
print_table(advanced_list, basic_headers)
for i in range(4):
    print(f"Unique count column: ({i}): ", count_unique_attr_column(advanced_list, i))
    print(f"Value count column: ({i}): ", count_attr_value_column(advanced_list, i))

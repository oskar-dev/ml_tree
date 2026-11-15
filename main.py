import math


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


def calc_entropy(p_values: list) -> float:
    result = 0.0

    for p in p_values:
        if p == 0:
            continue
        result += p * math.log2(p)

    return -result


def group_by_column(data: list, col: int, d_col: int) -> dict:

    map = {}

    for key in count_attr_value_column(data, col):
        dmap = {}
        for dkey in count_attr_value_column(data, d_col):
            dmap[dkey] = 0
        map[key] = dmap

    for row in data:
        map[row[col]][row[d_col]] += 1

    return map


def info_attr(data: list, col: int, d_col: int) -> float:
    group = group_by_column(data, col, d_col)

    attr_entropy = 0

    total_size = 0
    for a in group:
        size = 0
        for x in group[a]:
            size += group[a][x]
        total_size += size

    for a in group:
        size = 0
        for x in group[a]:
            size += group[a][x]

        weight = size / total_size
        entropy = calc_entropy([x / size for x in group[a].values()])
        attr_entropy += weight * entropy

    return attr_entropy


# basic_headers = ["a1", "a2", "a3", "a4", "d"]
# basic_list = load("basic_data.txt", " ")
#
# print("========= BASIC DATA =========")
# print_table(basic_list, basic_headers)
# for i in range(4):
#     print(f"Unique count column: ({i}): ", count_unique_attr_column(basic_list, i))
#     print(f"Value count column: ({i}): ", count_attr_value_column(basic_list, i))
#
# print("========= ADVANCED DATA =========")
# advanced_list = load("advanced_data.txt", ";")
# print_table(advanced_list, basic_headers)
# for i in range(4):
#     print(f"Unique count column: ({i}): ", count_unique_attr_column(advanced_list, i))
#     print(f"Value count column: ({i}): ", count_attr_value_column(advanced_list, i))
#

test_headers = ["a1", "a2", "a3", "a4", "d"]
test_list = load("test_data.txt", " ")

print(count_unique_attr_column(test_list, 2))
print(
    count_attr_value_column(test_list, 3)
)  # <- suma elementów słownika dla której kolwiek kolumn to 'n'. Wszystkie kolumny mają taki sam wynik

print(info_attr(test_list, 3, 4))

def determine_order(notes):
    ascending_order = [1, 2, 3, 4, 5, 6, 7, 8]
    descending_order = [8, 7, 6, 5, 4, 3, 2, 1]

    if notes == ascending_order:
        return "ascending"
    elif notes == descending_order:
        return "descending"
    else:
        return "mixed"


notes = list(map(int, input().split()))

result = determine_order(notes)
print(result)

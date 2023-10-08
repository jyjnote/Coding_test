def calculate_pieces_difference(white_pieces):

    correct_pieces = [1, 1, 2, 2, 2, 8]


    difference = [correct_pieces[i] - white_pieces[i] for i in range(len(correct_pieces))]

    return difference


white_pieces = list(map(int, input().split()))


difference = calculate_pieces_difference(white_pieces)


print(*difference)

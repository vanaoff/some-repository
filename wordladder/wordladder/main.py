begin_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

complete_list = [begin_word] + word_list


def distance(one, another):
    assert len(one) == len(another)
    count = 0
    for i, char in enumerate(one):
        count += 1 if char != another[i] else 0
    return count if count <= 1 else 0


def distance_matrix(words):
    matrix = []
    for i, word in enumerate(words):
        matrix += [[0] * i + [distance(word, x) for x in complete_list[i:]]]
    return matrix


def indexes_minimal(lst):
    return [i[0] for i in list(filter(lambda x: x[1] == 1, enumerate(lst)))]


if __name__ == '__main__':
    matrix = distance_matrix(complete_list)
    raw = [[i, word, 0] for i, word in enumerate(complete_list)]


    def increase(indexes, val):
        for i in indexes:
            if raw[i][2] == 0 or val < raw[i][2]:
                raw[i][2] = val
                increase(indexes_minimal(matrix[i]), val + 1)


    increase(indexes_minimal(matrix[0]), 2)

    final = list(filter(lambda x: x[1] == end_word, raw))[0]

    print(final[2])

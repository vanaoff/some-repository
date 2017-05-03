from collections import deque

begin_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

complete_list = [begin_word] + word_list


def is_edge(one, another):
    assert len(one) == len(another)
    count = 0
    for i, char in enumerate(one):
        count += 1 if char != another[i] else 0
    return count == 1


def find_edges(word, words):
    i = words.index(word)
    return [x[1] for x in filter(lambda x: is_edge(x[1], word) and x[0] > i, enumerate(words))]


def evaluate_edges(edges, value):
    return [[e, value] for e in edges]


def append(queue, list_):
    for i in list_:
        queue.append(i)


if __name__ == '__main__':
    result = {}

    queue = deque(evaluate_edges(find_edges(begin_word, complete_list), 1))
    while len(queue) > 0:
        t = queue.popleft()
        word = t[0]
        dist = t[1]
        if word not in result.keys():
            append(queue, evaluate_edges(find_edges(word, complete_list), dist + 1))
            result[word] = dist

    print(result.get(end_word, -1) + 1)

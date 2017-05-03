from collections import deque

begin_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]


def is_edge(one, another):
    assert len(one) == len(another)
    count = 0
    for i, char in enumerate(one):
        count += 1 if char != another[i] else 0
    return count == 1


def find_edges(word, words):
    return [x[1] for x in filter(lambda x: is_edge(x[1], word), enumerate(words))]


def evaluate_edges(edges, value):
    return [[e, value] for e in edges]


def append(queue, evaluated):
    for i in evaluated:
        queue.append(i)


def compute_distances(word_, word_list_):
    assert word_ not in word_list_
    full_list = [word_] + word_list_
    result = {}
    queue = deque(evaluate_edges(find_edges(word_, full_list), 1))
    while len(queue) > 0:
        t = queue.popleft()
        word_ = t[0]
        dist = t[1]
        if word_ not in result.keys():
            append(queue, evaluate_edges(find_edges(word_, full_list), dist + 1))
            result[word_] = dist
    return result


def chain_length(distances_, word_):
    return distances_.get(word_, -1) + 1


if __name__ == '__main__':
    distances = compute_distances(begin_word, word_list)
    print(chain_length(distances, end_word))

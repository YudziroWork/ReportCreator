def damerau_levenshtein_distance(s1: str, s2: str) -> int:
    d = {}
    len1 = len(s1)
    len2 = len(s2)

    for i in range(-1, len1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, len2 + 1):
        d[(-1, j)] = j + 1

    for i in range(len1):
        for j in range(len2):
            cost = 0 if s1[i] == s2[j] else 1

            d[(i, j)] = min(
                d[(i - 1, j)] + 1,
                d[(i, j - 1)] + 1,
                d[(i - 1, j - 1)] + cost
            )

            if i > 0 and j > 0 and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[(i - 2, j - 2)] + cost)

    return d[(len1 - 1, len2 - 1)]


def compare_lists(list1: list[list[str]], list2: list[list[str]]):
    """
    Для каждой строки из list2 ищет лучшее совпадение в list1.
    Возвращает список словарей.
    """
    results = []

    for row2 in list2:
        min_distance = float("inf")
        best_match = None

        for row1 in list1:
            total_distance = 0

            for cell1, cell2 in zip(row1, row2):
                total_distance += damerau_levenshtein_distance(cell1, cell2)

            if total_distance < min_distance:
                min_distance = total_distance
                best_match = row1

        results.append({
            "recognized": row2,
            "best_match": best_match,
            "distance": min_distance
        })

    return results
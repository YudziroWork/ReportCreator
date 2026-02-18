from collections import Counter


def calculate_statistics(results, etalon_list, threshold_ratio: float = 0.55):
    total = len(results)
    fully = 0
    partial = 0
    incorrect = 0

    distances = []
    used_etalon = set()
    best_matches_for_duplicates = []

    for item in results:
        dist = item["distance"]
        best = item["best_match"]

        distances.append(dist)

        if best:
            best_string = "".join(best)
            max_len = len(best_string)
            threshold = threshold_ratio * max_len

            #used_etalon.add(tuple(best))


            if dist == 0:
                fully += 1
                used_etalon.add(tuple(best))
                best_matches_for_duplicates.append(tuple(best))


            elif dist < threshold:
                partial += 1
                used_etalon.add(tuple(best))
                best_matches_for_duplicates.append(tuple(best))


            else:
                incorrect += 1
        else:
            incorrect += 1

    avg_distance = sum(distances) / total if total else 0

    # -------- Повторы только зелёные + жёлтые --------
    counter = Counter(best_matches_for_duplicates)
    duplicates_count = sum(count - 1 for count in counter.values() if count > 1)

    total_etalon = len(etalon_list)
    not_used_count = sum(
        1 for row in etalon_list if tuple(row) not in used_etalon
    )

    return {
        "total": total,
        "fully_matched": fully,
        "partially_matched": partial,
        "incorrect": incorrect,
        "accuracy_percent": (fully / total * 100) if total else 0,
        "full_plus_part": ((fully + partial) / total * 100) if total else 0,
        "avg_distance": avg_distance,
        "max_distance": max(distances) if distances else 0,
        "min_distance": min(distances) if distances else 0,
        "total_etalon": total_etalon,
        "not_used_count": not_used_count,
        "duplicates_count": duplicates_count,
    }
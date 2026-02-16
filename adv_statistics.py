from collections import Counter, defaultdict


def calculate_advanced_statistics(results, threshold_ratio=0.55):
    etalon_usage = Counter()
    error_stats = Counter()

    for item in results:
        best = item["best_match"]
        dist = item["distance"]

        if not best:
            continue

        best_string = "".join(best)
        recognized_string = "".join(item["recognized"])

        max_len = len(best_string)
        threshold = threshold_ratio * max_len


        if dist == 0:
            etalon_usage[best_string] += 1


        elif dist < threshold:
            etalon_usage[best_string] += 1

            # --- анализ ошибок ---
            min_len = min(len(best_string), len(recognized_string))

            for i in range(min_len):
                if best_string[i] != recognized_string[i]:
                    key = f"{recognized_string[i]} → {best_string[i]}"
                    error_stats[key] += 1

            # если строки разной длины
            if len(recognized_string) != len(best_string):
                error_stats["Длина отличается"] += 1

    return {
        "etalon_usage": dict(etalon_usage),
        "error_stats": dict(error_stats),
    }
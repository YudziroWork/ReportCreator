from excel_reader import read_excel_as_list
from comparison import compare_lists
from statistics import calculate_statistics
from report import generate_report


def process(
    etalon_path: str,
    recognized_path: str,
    output_path: str,
    show_threshold_matches: bool,
    make_stat1: bool,
    make_stat2: bool,
    make_not_used: bool,
):
    # Читаем файлы
    etalon_list = read_excel_as_list(etalon_path)
    recognized_list = read_excel_as_list(recognized_path)

    # Сравниваем
    results = compare_lists(etalon_list, recognized_list)

    # Считаем статистику
    stats = calculate_statistics(results, etalon_list)

    # Генерируем отчёт
    generate_report(
        results,
        stats,
        etalon_list,
        output_path,
        show_threshold_matches,
        make_stat1,
        make_stat2,
        make_not_used,
    )

    return stats
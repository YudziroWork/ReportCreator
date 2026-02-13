from excel_reader import read_excel_as_list
from comparison import compare_lists
from statistics import calculate_statistics
from report import generate_report


def process(etalon_path: str, recognized_path: str, output_path: str):
    list1 = read_excel_as_list(etalon_path)
    list2 = read_excel_as_list(recognized_path)

    results = compare_lists(list1, list2)

    stats = calculate_statistics(results, list1)

    generate_report(results, stats, list1, output_path)

    return stats
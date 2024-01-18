import csv
import os
from datetime import date


def compare_csv(file1_path, file2_path, output_file_path, key_fields):
    data1, headers1 = read_csv(file1_path, delimiter=";")
    data2, headers2 = read_csv(file2_path, delimiter=";")

    compared_data, headers = compare_data(data1, data2, key_fields)

    write_csv(compared_data, headers, output_file_path, delimiter=";")


def read_csv(file_path, delimiter=";"):
    with open(file_path, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file, delimiter=delimiter)
        headers = next(csv_reader)
        data = list(csv_reader)

    return data, headers


def compare_data(data1, data2, key_fields):
    compared_data = []

    headers = []
    for key_field in key_fields:
        headers.append(f"{key_field}_file1")
        headers.append(f"{key_field}_file2")
        headers.append(f"{key_field}_comparison")

    for row1 in data1:
        key_values = [row1[key_field] for key_field in key_fields]

        row2 = find_matching_row(data2, key_values)
        if row2 is not None:
            comparison_result = compare_rows(row1, row2)
            compared_data.append(row1 + row2 + comparison_result)
        else:
            comparison_result = ["NOT FOUND"] + [""] * len(key_fields) + row1
            compared_data.append(comparison_result)

    return compared_data, headers


def find_matching_row(data, key_values):
    for row in data:
        if all(
            row[key_field] == key_value
            for key_field, key_value in zip(key_fields, key_values)
        ):
            return row
    return None


def compare_rows(row1, row2):
    comparison_result = []
    for field1, field2 in zip(row1, row2):
        try:
            field1 = float(field1)
            field2 = float(field2)
            difference = field1 - field2
            comparison_result.append(difference)
        except ValueError:
            if field1 == field2:
                comparison_result.append("EQUAL")
            else:
                comparison_result.append("DIFFERENT")
                comparison_result.extend([field1, field2])

    return comparison_result


def write_csv(data, headers, file_path, delimiter=";"):
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        csv_writer = csv.writer(file, delimiter=delimiter)
        csv_writer.writerow(headers)
        csv_writer.writerows(data)


# Пример использования
file1_path = "/путь/к/файлу1.csv"
file2_path = "/путь/к/файлу2.csv"
today = date.today()
directory = "/путь/к/папке/"
filename = f"output_{today.strftime('%Y-%m-%d')}.csv"
output_file_path = os.path.join(directory, filename)
key_fields = ["id", "name"]  # Список ключевых полей
compare_csv(file1_path, file2_path, output_file_path, key_fields)

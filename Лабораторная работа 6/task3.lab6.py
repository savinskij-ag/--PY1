from typing import List
import csv

OUTPUT_FILE = "output.csv"


headers_list = ['longitude', 'latitude', 'housing_median_age', 'rooms_in_total', 'bedrooms_in_total', 'population',
                'house_holds', 'median_income_1', 'median_house_value']

data = [
    ['-122.050800', '37.3700080', '27.0008000', '3885.0300000', '661.000000', '1537.000000', '606.000000', '6.608500',
     '344700.000000'],
    ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000', '809.000000', '277.000000', '3.599000',
     '176500.000000'],
    ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000', '1484.000000', '495.000000', '5.793400',
     '270500.000000'],
    ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000', '49.000000', '11.000000', '6.135900',
     '330000.000000'],
]


def to_csv_file(file_name: str, headers: List[str], rows: List[List[str]], delimiter=",", new_line="\n"):
    """
    :param file_name: название файла
    :param headers: заголовки
    :param rows: строки
    :param delimiter: разделитель
    :param new_line: символ новой строки
    :return:
    """
    with open(file_name, "a", newline=new_line) as file:
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=delimiter)
        writer.writeheader()
        for row in rows:
            writer.writerow({headers[index]: elem for index, elem in enumerate(row)})


to_csv_file(OUTPUT_FILE, headers_list, data)

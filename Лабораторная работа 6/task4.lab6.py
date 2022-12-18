import json

INPUT_FILE = "output.csv"


def csv_to_list_dict(file_name: str, delimiter=",", new_line="\n") -> list[dict]:
    """
    :param file_name: название файла
    :param delimiter: разделитель
    :param new_line: символ новой строки
    :return:
    """
    with open(file_name, "r", newline=new_line) as file:
        headers = file.readline().replace("\n", "").split(delimiter)
        return [
            {
                headers[index]: value
                for index, value in enumerate(line.replace("\n", "").split(delimiter))
            }
            for line in file.readlines()
        ]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

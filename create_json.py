import os
import sys

from funtions.config import config, json_schema


def main():
    path = sys.argv[1]
    json_name = config.get("json_name")
    elements_in_path = [f for f in os.listdir(path)]
    index_counter = 0
    with open(path + os.sep + json_name, "at") as json_file:
        json_file.write("{\n")
        for element, text in json_schema:
            if element in elements_in_path:
                if "-rename" in sys.argv:
                    index_counter = rename_sequentially(path + os.sep + element, index_counter)
                inside_element = path + os.sep + element
                files_in_element = sorted(
                    [f for f in os.listdir(inside_element) if os.path.isfile(os.path.join(inside_element, f))])
                json_chunk = text.replace("$LEN_ELEMENTS$", len(files_in_element))
                json_chunk = json_chunk.replace("$FIRST_INDEX$", files_in_element.pop(0))
                json_file.write(json_chunk)

        json_file.write("}\n")


def rename_sequentially(path, start_index):
    file_name = sorted([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    index = start_index
    for i, old_name in enumerate(file_name):
        extension = ".".join(old_name.split('.')[1])
        index = index + i
        new_name = f'{index:04}'
        os.rename(path + os.path.sep + old_name, path + os.path.sep + new_name + extension)
    return index + 1

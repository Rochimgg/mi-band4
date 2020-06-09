import os
import sys

from funtions.config import config, json_schema


def main():
    path = sys.argv[1]
    json_name = config.get("json_name")
    elements_in_path = [f for f in os.listdir(path)]
    with open(path + os.sep + json_name, "at") as json_file:
        json_file.write("{\n")
        for element, text in json_schema:
            if element in elements_in_path:
                inside_element = path + os.sep + element
                files_in_element = sorted([f for f in os.listdir(inside_element) if os.path.isfile(os.path.join(inside_element, f))])
                json_chunck = text.replace("$LEN_ELEMENTS$", len(files_in_element))
                json_chunck = json_chunck.replace("$FIRST_INDEX$", files_in_element.pop(0))
                json_file.write(json_chunck)

        json_file.write("}\n")


def print_json_animation(json_file):
    path = sys.argv[1]
    elements_in_path = [f for f in os.listdir(path)]
    if "animation" in elements_in_path:
        anim_path = path + os.sep + "animation"
        anim_elem = sorted([f for f in os.listdir(anim_path) if os.path.isfile(os.path.join(anim_path, f))])
        len_anim_elem = str(len(anim_elem))
        first_num = anim_elem.pop(0).split(".")[0]
        json_file.write(json_schema.get("animation").replace("$FIRST_INDEX$", first_num).replace("$LEN_ELEMENTS$", len_anim_elem))


def print_json_background(json_file):
    mypath = sys.argv[1]
    elements_in_path = [f for f in os.listdir(mypath)]
    if "background" in elements_in_path:
        bg_path = mypath + os.sep + "background"
        bg_elem = sorted([f for f in os.listdir(bg_path) if os.path.isfile(os.path.join(bg_path, f))])
        first_num = bg_elem.pop(0).split(".")[0]
        json_file.write(json_schema.get("background").replace("$FIRST_INDEX$", first_num))

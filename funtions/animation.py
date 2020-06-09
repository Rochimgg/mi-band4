import os
import sys

path = sys.argv[1]
file_name = sys.argv[2] if len(sys.argv) > 2 else "example.json"
elements_in_path = [f for f in os.listdir(path)]

if "animation" in elements_in_path:
    anim_path = path + os.sep + "animation"
    anim_elem = sorted([f for f in os.listdir(anim_path) if os.path.isfile(os.path.join(anim_path, f))])
    len_anim_elem = len(anim_elem)
    print(anim_elem.pop(0).split(".")[0])
    first_num = int(anim_elem.pop(0).split(".")[0])
    with open(path + os.sep + file_name, "at") as json_file:
        json_file.write("\n  \"Other\": {\n" +
                        "    \"Animation\": {\n" +
                        "      \"AnimationImage\": {\n" +
                        "        \"X\": 0,\n" +
                        "        \"Y\": 0,\n" +
                        "       \"ImageIndex\": " + str(first_num) + ",\n" +
                        "       \"ImagesCount\": " + str(len_anim_elem) + ",\n" +
                        "       \"X3\": 0\n" +
                        "      },\n" +
                        "      \"Speed\": 4,\n" +
                        "      \"RepeatCount\": 50,\n" +
                        "      \"x2\": 5\n" +
                        "    }\n" +
                        "  }\n")

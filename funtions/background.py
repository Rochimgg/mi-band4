import os
import sys

mypath = sys.argv[1]
file_name = sys.argv[2] if len(sys.argv) > 2 else "example.json"
elements_in_path = [f for f in os.listdir(mypath)]

if "background" in elements_in_path:
    bg_path = mypath + os.sep + "background"
    bg_elem = sorted([f for f in os.listdir(bg_path) if os.path.isfile(os.path.join(bg_path, f))])
    len_anim_elem = len(bg_elem)
    first_num = int(bg_elem.pop(0).split(".")[0])
    with open(mypath + os.sep + file_name, "at") as json_file:
        json_file.write(
            "  \"Background\": {" +
            "    \"Image\": {" +
            "    \"X\": 0," +
            "    \"Y\": 0," +
            "    \"ImageIndex\": " + str(first_num) +
            "  }"
        )



config = {
    "json_name": "example.json",
    "animation": {
        "x": 0,
        "y": 0
    }

}



json_schema = {
    "background": "  \"Background\": {" +
                  "    \"Image\": {" +
                  "    \"X\": 0," +
                  "    \"Y\": 0," +
                  "    \"ImageIndex\": $FIRST_INDEX$" +
                  "  }",

    "animation": "\n  \"Other\": {\n" +
                 "    \"Animation\": {\n" +
                 "      \"AnimationImage\": {\n" +
                 "        \"X\": " + str(config.get("animation").get("x")) + ",\n" +
                 "        \"Y\": " + str(config.get("animation").get("y")) + ",\n" +
                 "       \"ImageIndex\": $FIRST_INDEX$,\n" +
                 "       \"ImagesCount\": $LEN_ELEMENTS$,\n" +
                 "       \"X3\": 0\n" +
                 "      },\n" +
                 "      \"Speed\": 4,\n" +
                 "      \"RepeatCount\": 50,\n" +
                 "      \"x2\": 5\n" +
                 "    }\n" +
                 "  }\n",
}

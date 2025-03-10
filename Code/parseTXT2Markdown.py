import os
import nest_asyncio
import llamaParseKey

nest_asyncio.apply()

from llama_parse import LlamaParse

folder_path = "manual/"  # Change this to your target folder
file_names = os.listdir(folder_path)

fileNamesCompleted = os.listdir("llamaParsed1\\")

# llamaParsed0 parsing_instruction="The provided document is a text file. Convert it to markdown with appropriate levels of headers defined."
parser = LlamaParse(
    api_key=llamaParseKey.llamaParseAPIKey,  # can also be set in your env as LLAMA_CLOUD_API_KEY
    result_type="markdown",
    num_workers=4,
    verbose=True,
    language="en",
    parsing_instruction="The provided document is a text file. Convert it to markdown, word for word, with appropriate levels of headers defined. Do not change the wording, just the foramtting. If there are any non-UTF-8 characters, convert them to their UTF-8 counterparts."
)

for file in file_names:
    if "SKIPPED" in file:
        continue
    if file in fileNamesCompleted:
        continue
    print(file)
    document = parser.load_data("manual\\" + file)

    with open("llamaParsed1\\" + file, "w") as f:
        for page in document:
            f.write(page.text)
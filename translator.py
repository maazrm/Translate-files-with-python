import pandas as pd
from deep_translator import GoogleTranslator
import time

def translate_and_save(input_file, output_file):
    #records the start time of the function
    start_time = time.time()

    # Read XLS file into DataFrame
    df = pd.read_excel(input_file)

    # Create translator object
    translator = GoogleTranslator(source='zh-TW', target='en')

    # Translate headers and text, ignoring non-Chinese content
    df.columns = df.columns.map(lambda x: translator.translate(x) if is_chinese(x) else x)
    df = df.applymap(lambda x: translator.translate(x) if is_chinese(x) else x)

    # Save translated DataFrame to CSV
    df.to_csv(output_file, index=False)

    end_time = time.time()
    elapsed_time = end_time - start_time

    #prints out the time taken to translate
    print(f"Translation and saving completed in: {elapsed_time:.2f} seconds")

def is_chinese(text):
    if isinstance(text, str):
        return any(char >= '\u4e00' and char <= '\u9fff' for char in text) #It compares each character's Unicode code point (numerical representation) to the range \u4e00 to \u9fff, which encompasses most Chinese characters.
    else:
        return False

# Specify file paths
input_file = "C:/Users/maazr/Documents/repos/Translate-files-with-python/Order Export.xls"
output_file = "C:/Users/maazr/Documents/repos/Translate-files-with-python/translated_file.csv"

translate_and_save(input_file, output_file)
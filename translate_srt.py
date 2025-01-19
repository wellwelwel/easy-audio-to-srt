import os
import re
from googletrans import Translator

def translate_srt(input_file, output_file, target_language="en"):
    translator = Translator()
    with open(input_file, 'r') as file:
        lines = file.readlines()

    output_lines = []
    for line in lines:
        if re.match(r'^\d+$', line) or '-->' in line:
            output_lines.append(line)
        else:
            try:
                translated_line = translator.translate(line.strip(), dest=target_language).text
                output_lines.append(translated_line + '\n')
            except Exception as e:
                output_lines.append(line)

    with open(output_file, 'w') as file:
        file.writelines(output_lines)

input_srt = os.getenv("FILE")

if not input_srt:
    raise ValueError("The FILE environment variable has not been set.")

output_srt = re.sub(r'(\.srt)$', r'-en\1', input_srt)

translate_srt(input_srt, output_srt)

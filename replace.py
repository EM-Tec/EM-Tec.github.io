import os
import re

def replace_text_in_file(file_path, old_text, new_text):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        new_content = re.sub(old_text, new_text, content)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        
        print(f'Replaced in: {file_path}')

    except Exception as e:
        print(f'Error processing {file_path}: {str(e)}')

def process_files_in_directory(directory, old_text, new_text):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.toml') or file.endswith('.md'):
                file_path = os.path.join(root, file)
                replace_text_in_file(file_path, old_text, new_text)

# Replace the old and new text accordingly
old_text = 'EM-Tec.github.io'
new_text = 'emtech.cc'

# Specify the root directory where you want to start the replacement
root_directory = 'D:\GayHub\EM-Tec.github.io'

# Call the function to process files
process_files_in_directory(root_directory, old_text, new_text)

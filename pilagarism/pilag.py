import os
import difflib

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def calculate_similarity(text1, text2):
    return difflib.SequenceMatcher(None, text1, text2).ratio()

def check_plagiarism(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    file_texts = {file: read_file(os.path.join(directory, file)) for file in files}
    compared_pairs = set()

    for i, file1 in enumerate(files):
        for file2 in files[i + 1:]:
            pair = tuple(sorted([file1, file2]))
            
            if pair not in compared_pairs:
                similarity = calculate_similarity(file_texts[file1], file_texts[file2])
                print(f"Similarity between {file1} and {file2}: {similarity:.2f}")
                compared_pairs.add(pair)
directory_path = 'D:\madhu\AI_intern\pilagarism'
check_plagiarism(directory_path)

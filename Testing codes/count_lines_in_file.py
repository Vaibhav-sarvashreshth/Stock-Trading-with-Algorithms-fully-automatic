import json

def count_lines_in_ipynb(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    code_lines = 0
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            code_lines += len(cell['source'])

    return code_lines

# Example usage
filename = 'D:/Komputer_Science/Summer After 8th sem/Kotak/my_env/sockets.ipynb'
lines_of_code = count_lines_in_ipynb(filename)
print(f"Total lines of code: {lines_of_code}")

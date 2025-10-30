def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def append_file(path, content):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(content + '\n')

COMMAND_FILE = "commands.txt"

def fetch_commands():
    with open(COMMAND_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    open(COMMAND_FILE, 'w').close()  # очистить после чтения
    return [line.strip() for line in lines if line.strip()]

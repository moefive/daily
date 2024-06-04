SOURCE_FILE_PATH = "pac/whitelist.pac"
DEST_FILE_PATH = "whitelist.pac"

SEARCH_TEXT = "SOCKS5 127.0.0.1:1080"
REPLACE_TEXT = "SOCKS5 127.0.0.1:7900"

def copy_file(source_path, dest_path):
    with open(source_path, 'r') as source_file:
        data = source_file.read()
    
    with open(dest_path, 'w') as dest_file:
        dest_file.write(data)

def replace_text(file_path, search_text, replace_text):
    with open(file_path, 'r') as file:
        data = file.read()
    
    new_data = data.replace(search_text, replace_text)
    
    with open(file_path, 'w') as file:
        file.write(new_data)

if __name__ == "__main__":
    # 复制文件到根目录
    copy_file(SOURCE_FILE_PATH, DEST_FILE_PATH)
    
    # 对复制到根目录的文件执行查找替换
    replace_text(DEST_FILE_PATH, SEARCH_TEXT, REPLACE_TEXT)

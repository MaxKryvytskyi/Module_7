
path = "file.txt"
additional_info = "Hello"
start_pos = 10
count_chars = 5


def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, "a") as f:
        f.write(additional_info)
        f.close()
    with open(path, "r") as f:
        f.seek(start_pos)
        data = f.read(count_chars)
    return data
file_operations(path, additional_info, start_pos, count_chars)
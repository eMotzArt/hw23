def file_reader(file_path: str):
    with open(file_path) as file:
        for line in file.readlines():
            yield line


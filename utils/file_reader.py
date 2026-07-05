def read_file(file_path):
    """
    Verilen dosya yolundaki metni okur ve döndürür.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


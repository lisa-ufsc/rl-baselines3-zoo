import os

class Logger:

    def __init__(self, path, file_name) -> None:
        self.__path = path
        self.__file_name = file_name
        try:
            os.makedirs(self.__path)
        except FileExistsError as e:
            pass

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, new_path: str) -> None:
        self.__path = new_path

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, new_file_name):
        self.__file_name = new_file_name

    def recorder(self, text: str) -> None:
        with open(f"{self.path}/{self.file_name}", 'a') as file:
            file.write(text + "\n")



class Experiment:

    def __init__(self, train_command: list = [], enjoy_command: list = []) -> None:
        self.__train_command = train_command
        self.__enjoy_command = enjoy_command

    @property
    def train_command(self) -> list:
        return self.__train_command

    @train_command.setter
    def train_command(self, new_train_command: list) -> None:
        self.__train_command = new_train_command

    @property
    def enjoy_command(self) -> list:
        return self.__enjoy_command

    @enjoy_command.setter
    def enjoy_command(self, new_enjoy_command) -> None:
        self.__enjoy_command = new_enjoy_command

    def __str__(self) -> str:
        return "{'train':" + "self.train_command" + ", 'enjoy':" + "self.enjoy_command" + "}"


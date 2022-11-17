
from automation_script.prompt import Prompt


class AutomaticCommit:

    def __init__(self, msg):
        self.__msg = msg

    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, new_msg):
        self.__msg = new_msg

    def git_init(self):
        Prompt().execute_command('git init')

    def git_add(self):
        Prompt().execute_command('git add .')

    def git_commit(self):
        Prompt().execute_command(f'git commit -m "{self.msg}"')

    def git_push(self):
        Prompt().execute_command(f'git push')

    def update(self):
        self.git_init()
        self.git_add()
        self.git_commit()
        self.git_push()

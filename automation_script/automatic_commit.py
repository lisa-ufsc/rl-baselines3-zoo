
from automation_script.prompt import Prompt


class AutomaticCommit:

    def __init__(self, msg, branch, url):
        self.__msg = msg
        self.__branch = branch
        self.__url = url

    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, new_msg):
        self.__msg = new_msg

    @property
    def branch(self):
        return self.__branch

    @branch.setter
    def branch(self, new_branch):
        self.__branch = new_branch

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, new_url):
        self.__url = new_url

    def git_init(self):
        Prompt().execute_command('git init')

    def git_add(self):
        Prompt().execute_command('git add .')

    def git_commit(self):
        Prompt().execute_command(f'git commit -m "{self.msg}"')

    def git_branch(self):
        Prompt().execute_command(f'git branch -M {self.branch}')

    def git_remote(self):
        Prompt().execute_command(f'git remote add origin {self.url}')

    def git_push(self):
        Prompt().execute_command(f'git push -u origin {self.branch}')

    def update(self):
        self.git_init()
        self.git_add()
        self.git_commit()
        self.git_branch()
        self.git_remote()
        self.git_push()

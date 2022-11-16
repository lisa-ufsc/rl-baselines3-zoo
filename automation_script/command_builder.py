

class CommandBuilder:

    def __init__(self, basic_command, env, algo, seed=None, n_steps=None, log_folder=None, tensorboard_log=None):
        self.__basic_command = basic_command
        self.__env = env
        self.__algo = algo
        self.__seed = seed
        self.__n_steps = n_steps
        self.__log_folder = log_folder
        self.__tensorboard_log = tensorboard_log

    @property
    def basic_command(self):
        return self.__basic_command

    @basic_command.setter
    def basic_command(self, new_basic_command):
        self.__basic_command = new_basic_command

    @property
    def env(self):
        return self.__env

    @env.setter
    def env(self, new_env):
        self.__env = new_env

    @property
    def algo(self):
        return self.__algo

    @algo.setter
    def algo(self, new_algo):
        self.__algo = new_algo

    @property
    def seed(self):
        return self.__seed

    @seed.setter
    def seed(self, new_seed):
        self.__seed = new_seed

    @property
    def n_steps(self):
        return self.__n_steps

    @n_steps.setter
    def n_steps(self, new_n_steps):
        self.__n_steps = new_n_steps

    @property
    def log_folder(self):
        return self.__log_folder

    @log_folder.setter
    def log_folder(self, new_log_folder):
        self.__log_folder = new_log_folder

    @property
    def tensorboard_log(self):
        return self.__tensorboard_log

    @tensorboard_log.setter
    def tensorboard_log(self, new_tensorboard_log):
        self.__tensorboard_log = new_tensorboard_log

    def make_basic_command(self):
        return self.basic_command + " "

    def make_env(self):
        return f"--env {self.env} "

    def make_algo(self):
        return f"--algo {self.algo} "

    def make_seed(self):
        if self.seed is None:
            return ""
        return f"--seed {self.seed} "

    def make_log_folder(self):
        if self.log_folder is None:
            return ""
        return f"--log-folder  {self.log_folder}/seed_{self.seed}/n_steps_{self.n_steps} "

    def make_tensorboard_log(self):
        if self.tensorboard_log is None:
            return ""
        return f"--tensorboard-log {self.tensorboard_log}/seed_{self.seed}/n_steps_{self.n_steps} "

    def make_hyperparams(self):
        if self.n_steps is None:
            return ""
        if self.algo in ["td3", "sac", "tqc"]:
            return f"--hyperparams train_freq:{self.n_steps}"
        return f"--hyperparams n_steps:{self.n_steps}"

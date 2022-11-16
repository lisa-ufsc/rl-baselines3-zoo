

class CommandBuilderDirector:

    def __init__(self, builder):
        self.__builder = builder

    @property
    def builder(self):
        return self.__builder

    @builder.setter
    def builder(self, new_builder):
        self.__builder = new_builder

    def generate(self):
    
        command = self.builder.make_basic_command()
        command += self.builder.make_env()
        command += self.builder.make_algo()
        command += self.builder.make_seed()
        command += self.builder.make_log_folder()
        command += self.builder.make_tensorboard_log()
        command += self.builder.make_hyperparams()
        
        return command

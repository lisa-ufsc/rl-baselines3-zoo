from automation_script.command_builder import CommandBuilder
from automation_script.command_builder_director import CommandBuilderDirector
from automation_script.experiment_manager import ExperimentManager



class Laboratory:

    def __init__(self):
        self.__experiment_manager = None

    def to_set_up(self):

        # Aqui que se altera os valores das seeds, dos n_steps,
        # dos processos simultaneos e do número de experimentos por agentes
        seeds = [3372438727, 896053610, 2784473964, 2183673577, 1843725486, 814179323, 2594327367, 3632205932, 3203387808, 2619532351]
        n_steps = [4,8,16]
        processes = 1

        commands = list()
        for s in seeds:
            for n in n_steps:

                builder = CommandBuilder("python ../train.py", "AntBulletEnv-v0", "tqc", s, n,
                                        "../experiments/exploration", "../experiments/exploration/tensorboard")
                ant_command = CommandBuilderDirector(builder).generate()

                builder = CommandBuilder("python ../train.py", "HopperBulletEnv-v0", "tqc", s, n,
                                        "../experiments/exploration", "../experiments/exploration/tensorboard")
                hopper_command = CommandBuilderDirector(builder).generate()

                builder = CommandBuilder("python ../train.py", "HalfCheetahBulletEnv-v0", "tqc", s, n,
                                        "../experiments/exploration", "../experiments/exploration/tensorboard")
                half_command = CommandBuilderDirector(builder).generate()

                commands.append(ant_command)
                commands.append(half_command)
                commands.append(hopper_command)

        self.__experiment_manager = ExperimentManager("hermes.deus.da.riqueza@gmail.com", "cbaksyebdtgwltbv",
                                                      "Test", "https://github.com/AHVG/rl-baselines3-zoo",
                                                      commands, processes)

    def run(self):
        self.to_set_up()
        self.__experiment_manager.run_experiments()
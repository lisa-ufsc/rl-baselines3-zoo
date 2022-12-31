import argparse

from automation_script.experiment_factory import ExperimentFactory
from automation_script.experiment_manager import ExperimentManager


class Laboratory:

    def __init__(self):
        self.__experiment_manager = None

    def to_set_up(self):

        parser = argparse.ArgumentParser(add_help=False)

        parser.add_argument('-e', '--email', action='store', type=str, required=True, help='Email for notification')
        parser.add_argument('-k', '--key', action='store', type=str, required=True, help='Key to enter email')
        parser.add_argument('-s', '--subject', action='store', type=str, default="Experimentos", help='Subject for email')

        args = parser.parse_args()
    
        # Aqui que se altera os valores das seeds, dos n_steps,
        # dos processos simultaneos e do número de experimentos por agentes
        seeds = [3372438727, 896053610, 2784473964, 2183673577, 1843725486, 814179323, 2594327367, 3632205932, 3203387808, 2619532351]
        steps = [128, 64, 32, 16, 8, 4, 2, 1]
        envs  = ["AntBulletEnv-v0", "HopperBulletEnv-v0", "HalfCheetahBulletEnv-v0"]
        algos = ["tqc"]
        n = 1000000
        experiments = ExperimentFactory().create(algos, envs, seeds, steps, n)

        self.__experiment_manager = ExperimentManager(args.email, args.key,
                                                      " ".join(args.subject.split("_")), experiments)

    def run(self):
        self.to_set_up()
        self.__experiment_manager.run_experiments()
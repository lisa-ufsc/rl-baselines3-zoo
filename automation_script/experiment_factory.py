from automation_script.experiment import Experiment

class ExperimentFactory:

    def create(self, algos, envs, seeds, steps, n):
        experiments = []
        for algo in algos:
            for env in envs:
                for seed in seeds:
                    for step in steps:
                        experiment = Experiment()
                        train_command = ["python3", 
                                        "--algo", f"{algo}",
                                        "--env", f"{env}",
                                        "--seed", f"{seed}",
                                        "--log-folder", f"experiments/exploration/seed_{seed}/n_steps_{step}",
                                        "--tensorboard-log", f"experiments/exploration/tensorboard/seed_{seed}/n_steps_{step}",
                                        "--hyperparams", f"train_freq:{step}"]
                        experiment.train_command = train_command

                        enjoy_command = ["python3",
                                        "--algo", f"{algo}",
                                        "--env", f"{env}",
                                        "-f", f"experiments/exploration/seed_{seed}/n_steps_{step}",
                                        "--reward-log", f"experiments/exploration/rewards/seed_{seed}/n_steps_{step}/{algo}/{env}",
                                        "-n", f"{n}",
                                        "--load-best",
                                        "--no-render"]
                        experiment.enjoy_command = enjoy_command
                        experiments.append(experiment)
        return experiments[:]


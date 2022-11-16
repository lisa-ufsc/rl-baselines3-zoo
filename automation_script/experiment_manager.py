
from multiprocessing import Pool

from automation_script.chronometer import Chronometer
from automation_script.prompt import Prompt
from automation_script.logger_txt import Logger
from automation_script.logger_email import MessageFactory, Dispatcher
from automation_script.automatic_commit import AutomaticCommit


class ExperimentManager:

    def __init__(self, email, key, msg, repo_url, experiments, processes):
        self.__email = email
        self.__key = key
        self.__msg = msg
        self.__repo_url = repo_url
        self.__experiments = experiments[:]
        self.__processes = processes

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        self.__email = new_email

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, new_key):
        self.__key = new_key

    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, new_msg):
        self.__msg = new_msg

    @property
    def repo_url(self):
        return self.__repo_url

    @repo_url.setter
    def repo_url(self, new_repo_url):
        self.__repo_url = new_repo_url

    @property
    def processes(self):
        return self.__processes

    @processes.setter
    def processes(self, new_processes):
        self.__processes = new_processes

    @property
    def experiments(self):
        return self.__experiments

    @experiments.setter
    def experiments(self, new_experiments):
        self.__experiments = new_experiments

    def add_experiments(self, experiments):
        self.__experiments.extend(experiments)

    def _convert_experiments(self, experiments, num=10):
        experiments = []
        aux = []
        for experiment in experiments:
            if num == 0:
                experiments.append(aux)
                aux = []
            aux.append(experiment)
            num -= 1
        if num != 0:
            experiments.append(aux)
        return experiments

    def _notify_by_email(self, msg):
        sender = self.email
        receiver = self.email
        subject = self.msg
        password = self.key
        body = msg

        message = MessageFactory().create(sender, receiver, subject, body)
        Dispatcher(message, password).send()

    def _notify_by_txt(self, msg):
        logger = Logger("./logs", "logs.txt")
        logger.recorder(msg)

    def run_experiments(self):
        chronometer = Chronometer()
        
        experiments = self._convert_experiments(self.experiments)
        dones_experiments = []

        chronometer.start_counting()
        for exp in experiments:
            try:
                c = Chronometer()
                processes = int(self.processes)

                c.start_counting()
                pool = Pool(processes=processes)
                pool.map(Prompt.execute_command, exp)
                c.finish_counting()

                dones_experiments.extend(exp)
                percentual = len(dones_experiments)/len(self.experiments)
                msg_email = f"""<body>
                                    <p><b>Início:</b> {c.start_d}s</p>
                                    <p><b>Fim:</b> {c.end_d}s</p>
                                    <p><b>Tempo de execução:</b> {c.delta_d()}</p>
                                    <p><b>Percentual:</b>{percentual}</p>
                                </body>"""
                self._notify_by_email(msg_email)

            except KeyboardInterrupt as e:
                pass

        chronometer.finish_counting()

        msg_txt = f"""Experimentos finalizados!\n
                    - Incio: {chronometer.start_d}\n
                    - Fim: {chronometer.end_d}\n
                    - Tempo de execução: {chronometer.delta_d()}\n
                    - Número de comandos: {len(self.experiments)}\n
                    - Comandos executados:\n
                    {self.experiments}\n"""
        self._notify_by_txt(msg_txt)

        msg_email = f"""<body>
                            <p><b>Início:</b> {chronometer.start_d}s</p>
                            <p><b>Fim:</b> {chronometer.end_d}s</p>
                            <p><b>Tempo de execução:</b> {chronometer.delta_d()}</p>
                            <p><b>Número de comandos:</b>{len(self.experiments)}</p>
                        </body>"""
        self._notify_by_email(msg_email)
        AutomaticCommit(self.msg, "master", self.repo_url).update()

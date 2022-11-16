
from multiprocessing import Pool

import chronometer
from prompt import Prompt
from logger_txt import Logger
from logger_email import MessageFactory, Dispatcher


class ExperimentManager:

    def __init__(self, experiments: list, processes):
        self.__experiments = experiments[:]
        self.__processes = processes

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

    def _notify(self):
        sender = "hermes.deus.da.riqueza@gmail.com"
        receiver = "hermes.deus.da.riqueza@gmail.com"
        subject = "Semana 7"
        password = "key"

        body = f"""<body>
                    <h1>Email automatico dos experimentos</h1>
                    <p><b>Experimento feito:</b> {command}</p>
                    <p><b>Início:</b> {c.start_d}s</p>
                    <p><b>Fim:</b> {c.end_d}s</p>
                    <p><b>Tempo de execução:</b> {c.delta_d()}s</p>
                """
        if c.delta_s() < 600:
            subject += " - Problema"
            body += """<p><font color="#FF0000"><b>Aviso:</b> Simulação possivelmente terminou com falha</p></font>"""
        body += """</body>"""
        message = MessageFactory().create(sender, receiver, subject, body)
        Dispatcher(message, password).send()

    def run_experiments(self) -> None:
        c = chronometer.Chronometer()
        l = Logger("./logs", "logs.txt")
        
        c.start_counting()
        experiments = self._convert_experiments(self.experiments)
        dones_experiments = []
        for exp in experiments:
            try:

                processes = int(self.processes)
                pool = Pool(processes=processes)   
                pool.map(Prompt().execute_command, exp)
                dones_experiments.extend(exp)

                

            except KeyboardInterrupt as e:
                pass

        c.finish_counting()

        l.recorder( "Experimentos finalizados!")
        l.recorder(f" - Incio: {c.start_d}")
        l.recorder(f" - Fim: {c.end_d}")
        l.recorder(f" - Tempo de execução: {c.delta_d()}")
        l.recorder(f" - Número de comandos: {len(self.experiments)}")
        l.recorder(f" - Comandos executados:")
        [l.recorder(f"      {experiment}") for experiment in self.experiments]
        l.recorder("")

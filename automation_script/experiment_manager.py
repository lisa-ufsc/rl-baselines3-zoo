
import sys
from rl_zoo3.train import train
from rl_zoo3.enjoy import enjoy

from automation_script.chronometer import Chronometer
from automation_script.logger_txt import Logger
from automation_script.logger_email import MessageFactory, Dispatcher
from automation_script.automatic_commit import AutomaticCommit


class ExperimentManager:

    def __init__(self, email, key, msg, experiments):
        self.__email = email
        self.__key = key
        self.__msg = msg
        self.__experiments = experiments[:]

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
    def experiments(self):
        return self.__experiments

    @experiments.setter
    def experiments(self, new_experiments):
        self.__experiments = new_experiments

    def _notify_by_email(self, msg):
        sender = self.email
        receiver = self.email
        subject = self.msg
        password = self.key
        body = msg

        message = MessageFactory().create(sender, receiver, subject, body)
        print(Dispatcher(message, password).send())

    def _notify_by_txt(self, msg):
        logger = Logger("./automation_script/logs", "logs.txt")
        logger.recorder(msg)

    def run_experiments(self):
        chronometer = Chronometer()
        
        do_experiments = []
        dones_experiments = []
        chronometer.start_counting()
        for i, exp in enumerate(self.experiments):
            try:
                do_experiments = self.experiments[i:len(self.experiments)]
                msg_txt = "["
                for command in do_experiments:
                    msg_txt += f"{command},\n"
                msg_txt += "]"
                self._notify_by_txt(f"Checkpoint {i + 1}")
                self._notify_by_txt(msg_txt)

                c = Chronometer()

                c.start_counting()
                sys.argv = exp.train_command[:]
                #train() 

                sys.argv = exp.enjoy_command[:]
                #enjoy()
                c.finish_counting()

                dones_experiments.append(exp)
                percentual = 100 * len(dones_experiments)/len(self.experiments)
                msg_email = f"""<body>
                                    <p><b>Início:</b> {c.start_d}s</p>
                                    <p><b>Fim:</b> {c.end_d}s</p>
                                    <p><b>Tempo de execução:</b> {c.delta_d()}</p>
                                    <p><b>Percentual:</b>{percentual:.2f} %</p>
                                </body>"""
                
                self._notify_by_email(msg_email)
                AutomaticCommit(str(exp)).update()

            except KeyboardInterrupt as e:
                exit(1)
            except:
                pass

        chronometer.finish_counting()

        msg_txt = f"""
Experimentos finalizados!
    - Inicio: {chronometer.start_d}
    - Fim: {chronometer.end_d}
    - Tempo de execucao: {chronometer.delta_d()}
    - Numero de comandos: {len(self.experiments)}
    - Comandos executados:
    """
        for command in self.experiments:
            msg_txt += f"      {command}\n"
        self._notify_by_txt(msg_txt)

        msg_email = f"""<body>
                            <p><b>Início:</b> {chronometer.start_d}s</p>
                            <p><b>Fim:</b> {chronometer.end_d}s</p>
                            <p><b>Tempo de execução:</b> {chronometer.delta_d()}</p>
                            <p><b>Número de comandos:</b>{len(self.experiments)}</p>
                        </body>"""
        self._notify_by_email(msg_email)
        AutomaticCommit(self.msg).update()

# Para futuras implementações
# Notificar por email o andamento dos experimentos

import smtplib, ssl
import email.message


class Dispatcher:

    _port = 587
    _smtp_server = "smtp.gmail.com"

    def __init__(self, message, password) -> None:
        self.__message = message
        self.__password = password

    def send(self):
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP(self._smtp_server, self._port) as server: 
                server.starttls(context=context)
                server.login(self.__message['from'], self.__password)
                server.sendmail(self.__message['from'], self.__message['to'], self.__message.as_string().encode('utf-8'))
        except smtplib.SMTPAuthenticationError as e:
            return "Failed to send. Authentication error."
        except smtplib.SMTPRecipientsRefused as e:
            return "Failed to send. Receiver refused."
        except smtplib.SMTPServerDisconnected as e:
            return "Server disconnected"
        except:
            return "some error occurred!"
        return "Email sent!"

class MessageFactory:

    def create(self, sender, receiver, subject, body):
        message = email.message.Message()

        message['from'] = sender
        message['to'] = receiver
        message['subject'] = subject
        message.add_header("Content-Type", 'text/html')
        message.set_payload(body)

        return message

"""
sender = "my@gmail.com"
receiver = "somebody@gmail.com"
subject = "Semana 7"
body = f'''<h3>Oiiiiiiiiiii, sou o email automatico</h3>
<h4>
Algum texto muito legal aqui
</h4>

<h3>
Até outro email!
</h3>'''


password = "key"

message = MessageFactory().create(sender, receiver, subject, body)
r = Dispatcher(message, password).send()

print(r)
"""
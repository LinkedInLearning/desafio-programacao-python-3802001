import sched
import time

def agendamento(horario_do_evento, funcao, *args):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(horario_do_evento, 1, funcao, argument=args)
    print(f'{funcao.__name__}() agendado para {time.asctime(time.localtime(horario_do_evento))}')
    s.run()


# comandos usados na vídeo para referência
if __name__ == '__main__':
    agendamento(time.time() + 3, print, 'Olá!')
    agendamento(time.time() + 3, print, 'Olá!', 'Como você está?')
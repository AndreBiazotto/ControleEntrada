from threading import Thread
from datetime import datetime, timedelta
import rpyc
from time import sleep

def func(comeco, nome):
    while True:
        if datetime.now().replace(microsecond=0) != comeco:
            continue
        else:
            print(f"Tentativas de {nome}")
            conn = rpyc.connect("localhost", 18861)
            root = conn.root

            acoes = ["cabelo", "barba", "bigode"]
            ponteiro = 0

            for i in range(20):
                if ponteiro < 3:
                    if root.usar_recurso(acoes[ponteiro], nome) == "espere":
                        sleep(root.tempo_sono)
                    else:
                        sleep(2)
                        ponteiro = ponteiro + 1
            
            print(f'Fim das tentativas de {nome}')
            break



time_deslocado = datetime.now().replace(microsecond=0) + timedelta(seconds=3)

t1 = Thread(target=func, args=[time_deslocado, "A"])
t2 = Thread(target=func, args=[time_deslocado, "B"])
t3 = Thread(target=func, args=[time_deslocado, "C"])
t4 = Thread(target=func, args=[time_deslocado, "D"])

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

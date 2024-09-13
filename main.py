import rpyc
from time import sleep

conn = rpyc.connect("localhost", 18861)
root = conn.root

acoes = ["cabelo", "barba", "bigode"]
ponteiro = 0

user = input("USER: ")

for i in range(20):
    if ponteiro < 3:
        if root.usar_recurso(acoes[ponteiro], user) == "espere":
            sleep(root.tempo_sono)
        else:
            sleep(2)
            ponteiro = ponteiro + 1
        
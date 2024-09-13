import rpyc
from barbeiro import Barbeiro

bar = Barbeiro()

class MyService(rpyc.Service):
    def on_connect(self, conn):
        pass
        
    def on_disconnect(self, conn):
        pass

    exposed_tempo_sono = 0

    def exposed_status_recurso(self, user):
        return bar.ocupado

    def exposed_usar_recurso(self, option, user):
        if not bar.ocupado:
            
            bar.ocupado = True

            if option == "cabelo":
                bar.cortarCabelo(user)
                exposed_tempo_sono = 3
            elif option == "barba":
                bar.cortarBarba(user)
                exposed_tempo_sono = 4
            elif option == "bigode":
                bar.cortarBigode(user)
                exposed_tempo_sono = 5
            else:
                print("ERROR")
                
            bar.ocupado = False
        else:
            return "espere"

if __name__ == "__main__":
    from rpyc.utils.server import ThreadPoolServer
    t = ThreadPoolServer(MyService, port=18861)
    t.start()

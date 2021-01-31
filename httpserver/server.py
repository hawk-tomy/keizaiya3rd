from cheroot.wsgi import PathInfoDispatcher
from cheroot.wsgi import Server
from .app import app

d = PathInfoDispatcher({'/': app})
server = Server(('0.0.0.0', 8080), d)

if __name__ == '__main__':
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
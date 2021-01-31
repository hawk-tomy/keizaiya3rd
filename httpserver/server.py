from cheroot.wsgi import PathInfoDispatcher, Server
from app import app

d = PathInfoDispatcher({'/': app})
server = Server(('localhost', 80), d)

if __name__ == '__main__':
    try:
        print('start server')
        server.start()
    except KeyboardInterrupt:
        server.stop()

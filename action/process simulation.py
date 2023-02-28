class Server:

    def __init__(self):
        self.buffer = []
        self.ip = id(self)

    def send_data(self, data):
        router.buffer.append(data)
        router.buffer[-1].ip = data.ip

    def get_data(self):
        data = self.buffer
        self.buffer = []
        return data

    def get_ip(self):
        return self.ip


class Router:

    def __init__(self):
        self.buffer: list = []
        self.server_registry: set = set()

    def link(self, server):
        self.server_registry.add(server)

    def unlink(self, server):
        self.server_registry.remove(server)

    def send_data(self):
        for data in self.buffer:
            for server in self.server_registry:
                if server.get_ip() == data.ip:
                    server.buffer.append(data)
        self.buffer = []


class Data:

    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
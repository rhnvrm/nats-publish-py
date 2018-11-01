import socket

PUB_CMD = b"PUB"
CR_LF = "\r\n"


class NatsPublish(object):
    def __init__(self, conn_options=None):
        if conn_options == None:
            self.conn_options = {
                "hostname": "localhost",
                "port": 4222,
            }
        else:
            self.conn_options = conn_options
        
        # setup socket
        self.sock = self.setup_socket()

    def __del__(self):
        self.sock.shutdown(1)

    def setup_socket(self):
        sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

        sock.connect((self.conn_options["hostname"], self.conn_options["port"]))
        return sock

    def send_command(self,d):
        self.sock.sendall(bytes(d, 'utf-8'))

    def publish(self, msg="hello world", subject="", opt_reply=""):
        msg = str(msg)
        self.send_command("PUB {} {} {}{}{}{}".format(subject, opt_reply, len(msg), CR_LF, msg, CR_LF))

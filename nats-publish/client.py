import socket

conn_options = {
    "hostname": "demo.nats.io",
    "port": 4222,
}

PUB_CMD = b"PUB"
CONNECT_CMD = b"CONNECT"
CR_LF = "\r\n"

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.settimeout(3)
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

sock.connect((conn_options["hostname"], conn_options["port"]))

def send_command(d):
    sock.sendall(d)

subject = "foo"
opt_reply = ""
msg = "hello world"

send_command("PUB {} {} {}{}{}{}".format(subject, opt_reply, len(msg), CR_LF, msg, CR_LF))
send_command("PUB {} {} {}{}{}{}".format(subject, opt_reply, len(msg), CR_LF, msg, CR_LF))
send_command("PUB {} {} {}{}{}{}".format(subject, opt_reply, len(msg), CR_LF, msg, CR_LF))

sock.shutdown(1)
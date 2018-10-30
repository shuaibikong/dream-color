import socket

server = socket.socket()
server.bind(("0.0.0.0", 8000))
server.listen()
import socket

from exporting_collector.config.config import settings


def syslog_sender(*, message: str):
    tcp_socket = socket.socket()
    tcp_socket.connect((settings.SYSLOG_HOST, settings.SYSLOG_PORT))
    tcp_socket.send(message)
    tcp_socket.close()

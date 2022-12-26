import socket

from loguru import logger

from config.settings import settings


def syslog_sender(*, data_to_send: dict):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
        connection.bind((settings.SYSLOG_HOST, settings.SYSLOG_PORT))
        connection.listen()
        conn, addr = connection.accept()
        with conn:
            logger.info(f"Connected to: {addr} with connection: {conn}")
            conn.sendall(data_to_send)

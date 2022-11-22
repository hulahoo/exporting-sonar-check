import socketserver

from loguru import logger


class TestSyslogTCPHandler(socketserver.BaseRequestHandler):
    """
    The test request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self) -> None:
        if not hasattr(self, "pattern"):
            self.initialize()

        incoming_events = bytes.decode(self.request.recv(1024).strip())
        if incoming_events is not None:
            try:
                logger.info(f"Received data: {incoming_events}")
            except Exception as e:
                logger.exception(f"Error occured: {e}")


if __name__ == "__main__":
    with socketserver.TCPServer(
        ("localhost", 1001), TestSyslogTCPHandler
    ) as server:
        logger.info("Start listening...")
        server.serve_forever(poll_interval=0.5)

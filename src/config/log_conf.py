import sys

# TODO: подумать над форматом сообщения
format = "{time} | {level} | {name}:{function}:{line} -> {message}"


configure = {
    "handlers": [
        {"sink": sys.stdout, "format": format},
    ]
}

import socket
from math import fabs

from flask import Flask, jsonify, request

DEBUG = True


def isOpen(ip: str | None, port: str | int) -> bool:
    """Check if posrt open

    Args:
        ip (str | None): Ip address
        port (str | int): port

    Returns:
        bool: Returns true if TCP port open
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Nothing here"

    @app.route("/ip")
    def client_ip():
        """Returns requester host Ip address

        Returns:
            str: Ip address
        """
        return request.remote_addr, 200

    @app.route("/memcached")
    def check_memcached():
        host = request.args.get("host")
        port = request.args.get("port")
        port = 11211 if not port else port
        host = request.remote_addr if not host else host
        return str(isOpen(host, port))

    return app


app = create_app()


def run_app(app: Flask):
    app.run(host="0.0.0.0", port=8888)  # nosec


# run_app(app)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8888, debug=DEBUG)  # nosec

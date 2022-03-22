import socket
from urllib.request import Request

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


def get_ip(req) -> str:

    return req.headers.get("X-Forwarded-For") or req.remote_addr


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
        try:
            return get_ip(request), 200
        except (RuntimeError, ValueError) as err:
            return err, 500

    @app.route("/memcached")
    def check_memcached():
        host = request.args.get("host")
        port = request.args.get("port")
        port = port or 11211
        host = host or get_ip(request)
        return str(isOpen(host, port))

    return app


app = create_app()


def run_app(app: Flask):
    app.run(host="0.0.0.0", port=8888)  # nosec


# run_app(app)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8888, debug=DEBUG)  # nosec

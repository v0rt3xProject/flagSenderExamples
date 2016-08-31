#!/usr/bin/python
import os
import socket
import urllib

# Configuration
FLAG_SERVER = os.environ.get("FLAG_SERVER", "10.0.0.10")

FLAG_TCP_HI_PORT = os.environ.get("FLAG_TCP_HI_PORT", 6666)
FLAG_TCP_NO_PORT = os.environ.get("FLAG_TCP_NO_PORT", 5555)
FLAG_TCP_LO_PORT = os.environ.get("FLAG_TCP_LO_PORT", 4444)

FLAG_HTTP_PORT = os.environ.get("FLAG_HTTP_PORT", 9999)

FLAG_HI_URL = os.environ.get(
    "FLAG_HI_URL", "http://%s:%s/flag/hi" % (FLAG_SERVER, FLAG_HTTP_PORT)
)
FLAG_NO_URL = os.environ.get(
    "FLAG_NO_URL", "http://%s:%s/flag/no" % (FLAG_SERVER, FLAG_HTTP_PORT)
)
FLAG_LO_URL = os.environ.get(
    "FLAG_LO_URL", "http://%s:%s/flag/lo" % (FLAG_SERVER, FLAG_HTTP_PORT)
)

FLAG_JSON_STATUS_URL = os.environ.get(
    "FLAG_JSON_STATUS_URL",
    "http://%s:%s/flag/status.json" % (FLAG_SERVER, FLAG_HTTP_PORT)
)


# Helper Classes
class FlagSenderTCPClient:

    def __init__(self, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((FLAG_SERVER, port))

    def send_flag(self, flag):
        self.socket.sendall("%s\n" % flag)

    @staticmethod
    def get_hi_client():
        return FlagSenderTCPClient(FLAG_TCP_HI_PORT)

    @staticmethod
    def get_no_client():
        return FlagSenderTCPClient(FLAG_TCP_NO_PORT)

    @staticmethod
    def get_lo_client():
        return FlagSenderTCPClient(FLAG_TCP_LO_PORT)

    def __del__(self):
        self.socket.close()


class FlagSenderHTTPClient:

    @staticmethod
    def send_hi(flag):
        return urllib2.urlopen("%s/%s" % (FLAG_HI_URL, flag))

    @staticmethod
    def send_no(flag):
        return urllib2.urlopen("%s/%s" % (FLAG_HI_URL, flag))

    @staticmethod
    def send_lo(flag):
        return urllib2.urlopen("%s/%s" % (FLAG_HI_URL, flag))


# Main Program
if __name__ == "__main__":

    example_tcp_client = FlagSenderTCPClient.get_hi_client()
    example_tcp_client.send_flag("0123456789abcdef0123456789abcdef=")

    FlagSenderHTTPClient.send_hi("0123456789abcdef0123456789abcdef=")

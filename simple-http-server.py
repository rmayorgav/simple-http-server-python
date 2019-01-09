#!/usr/bin/env python3

import http.server
import multiprocessing
import socket

HTTP_PORT = 8888


class HTTPServerIPv4(http.server.HTTPServer):
    address_family = socket.AF_INET


class HTTPServerIPv6(http.server.HTTPServer):
    address_family = socket.AF_INET6


def http_server_ipv4():
    server = HTTPServerIPv4(
        ('', HTTP_PORT),
        http.server.SimpleHTTPRequestHandler
    )
    server.serve_forever()


def http_server_ipv6():
    server = HTTPServerIPv6(
        ('', HTTP_PORT),
        http.server.SimpleHTTPRequestHandler
    )
    server.serve_forever()


if __name__ == '__main__':
    multiprocessing.freeze_support()

    server_ipv4 = multiprocessing.Process(target=http_server_ipv4)
    server_ipv6 = multiprocessing.Process(target=http_server_ipv6)

    server_ipv4.start()
    server_ipv6.start()

    print('Listening on port {}'.format(HTTP_PORT))
    print('Press CTRL-C to quit')

    server_ipv4.join()
    server_ipv6.join()

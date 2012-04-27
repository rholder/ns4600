import cookielib
import getopt
import time
import socket
import sys
import urllib
import urllib2

def wake(mac_address):
    """Wake the NAS when Wake-on-LAN is enabled on the device."""

    # convert to raw bytes
    hex_data = mac_address.split(':')
    raw_mac_bytes = ''.join([chr(int(item, 16)) for item in hex_data])
    magic_packet = '\xff'*6 + raw_mac_bytes*16

    # broadcast magic packet on LAN
    broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    broadcast_socket.sendto(magic_packet, ("255.255.255.255",9))
    broadcast_socket.close()

def shutdown(username, password, location):
    """Shutdown the NAS

    Log in and issue a shutdown command to the device. The location
    can include the port, as in 'http://fooserver:8081'.

    """

    # NAS login needs some cookies
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    # post login (yes, those are the actual valid args...)
    login_ms = int(round(time.time() * 1000))
    login_payload = urllib.urlencode([("rs", "ajaxlogin"),
                                      ("rst", ""),
                                      ("rsrnd", login_ms),
                                      ("rsargs[]", username),
                                      ("rsargs[]", password)])
    login_url = location + "/admin/index.php"
    login_response = opener.open(login_url, login_payload)

    # handle bad login, check cookie for cookie_key with a value
    is_valid = False
    for c in cj:
        if c.name == 'cookie_key':
            if len(c.value) > 0:
                is_valid = True
    if not is_valid:
        raise Exception("Could not log in with given username/password")

    # post shutdown
    shutdown_ms = int(round(time.time() * 1000))
    shutdown_payload = urllib.urlencode([("rs", "ajax"),
                                         ("rst", ""),
                                         ("rsrnd", shutdown_ms),
                                         ("rsargs[]", "shutdown")])
    shutdown_url = location + "/admin/shutdown.php"
    shutdown_response = opener.open(shutdown_url, shutdown_payload)


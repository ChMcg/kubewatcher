import time
import subprocess
import select


import asyncio
import aiofiles


log_filename = 'logs/audit-test.log'

# async def async_main():
#     async with aiofiles.open('logs/audit-test.log', mode='r') as f:
#         async for line in f:
#             print(line)

def main():
    f = subprocess.Popen(
            ['tail', '-f', log_filename],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

    p = select.poll()
    p.register(f.stdout)

    while True:
        if p.poll(1):
            print(f.stdout.readline())
        # else:
        #     time.sleep(1)




    

if __name__=="__main__":
    main()
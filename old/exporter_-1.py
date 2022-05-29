import asyncio
import aiofiles


async def async_main():
    async with aiofiles.open('logs/audit-test.log', mode='r') as f:
        async for line in f:
            print(line)
            

def main():
    asyncio.run(async_main())


if __name__=="__main__":
    main()

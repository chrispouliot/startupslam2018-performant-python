import asyncio
import aiohttp

url = "http://209.97.148.110"
loop = asyncio.get_event_loop()
client = aiohttp.ClientSession(loop=loop)


async def make_request(client, url):
    async with client.get(url) as response:
        print(await response.read())
        return

asyncio.ensure_future(make_request(client, url + "/100"))
loop.run_forever()


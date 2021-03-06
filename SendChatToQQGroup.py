import requests
import asyncio, aiohttp
from setting import CoolQHTTP_setting
async def report_data(textData):
    data = {'group_id': CoolQHTTP_setting['groupid'], 'message': textData}
    timeout = aiohttp.ClientTimeout(total=1)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.post(CoolQHTTP_setting['url'], data=data) as res:
            pass
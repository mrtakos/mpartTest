'''
HTTP load generator 
+ Program must accept file-based input for: serverURL, targetRPS, authKey.
+ Program must send up valid request body payload.
+ Program must sanely handle typical HTTP server responses.
+ Program must output to the console the current RPS and target RPS.
+ After the run has completed, program must output a summary of run including relevant request/response metrics.
+ Your API key is limited to 100,000 requests. Please contact us if you need that limit raised for any reason.
+ Program must be submitted via a git repo, and we will want to see commit history
'''

import aiohttp
import asyncio
from datetime import datetime, timezone
import json
import logging
import os
import sys

logging.basicConfig(filename='http_load.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)

goodresp = { "successful": 'true' }
statuscodecount = {
    "200": 0,
    "success": 0,
    "fail": 0
}

async def tick(url, key, rps):
    ''' runs every second
    '''
    global statuscodecount
    stamp = datetime.now(tz=timezone.utc).strftime('%Y/%m/%d/%H:%M:%S%f')
    rps = int(rps)
    reqcount = 0
    headers = {
        "X-Api-Key": key,
        "Content-Type": "application/json",
    }
    payload = {
        "name": "YOUR_NAME",
        "date": stamp,
        "requests_sent": rps
    }
    connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(headers=headers, connector=connector) as session:
        for i in range(rps):
            ## maybe check to see if current time is still within the 1 second window
            reqcount += 1
            try:
                async with session.get(url, data=payload) as resp:
                    result = await resp.json()
                    if result == goodresp:
                        statuscodecount['success'] += 1
                    else:
                        logger.error(result)
                        statuscodecount['fail'] += 1
                    if str(resp.status) in statuscodecount.keys():
                        statuscodecount[str(resp.status)] += 1
                    else:
                        statuscodecount[str(resp.status)] = 1
            except Exception as e:
                logger.error(e)
                break

    print(f"time: {stamp} target: {rps} actual: {reqcount}")
    

async def main():
    ''' Kick off our jobs in input.json
    '''
    inputpath = "input.json"
    try:
        with open(inputpath) as f:
            content = f.read()
    except Exception as e:
        logger.error(e)

    try:
        j = json.loads(content)
    except Exception as e:
        logger.error(e)

    while True:
        await tick(j['serverURL'], j['authKey'], j['targetRPS'])
        await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(json.dumps(statuscodecount))
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
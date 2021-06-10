'''
HTTP load generator 
+ Program must accept file-based input for: serverURL, targetRPS, authKey.
+ Program must send up valid request body payload.
* Program must sanely handle typical HTTP server responses.
+ Program must output to the console the current RPS and target RPS.
* After the run has completed, program must output a summary of run including relevant request/response metrics.
* Your API key is limited to 100,000 requests. Please contact us if you need that limit raised for any reason.
* Program must be submitted via a git repo, and we will want to see commit history
'''

import aiohttp
import asyncio
from datetime import datetime, timezone
import json
import logging
import requests
import sched
import time
from threading import Timer

logging.basicConfig()
logger = logging.getLogger(__name__)

s = sched.scheduler(time.time, time.sleep)

async def tick(url='', key='', rps=''):
    ''' runs every second
    '''
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
    async with aiohttp.ClientSession(headers=headers) as session:
        for i in range(rps):
            ## maybe check to see if current time is still within the 1 second window
            reqcount += 1
            async with session.get(url,data=payload,) as resp:
                
                result = await resp.json()
    print(f"time: {stamp} target: {rps}")



def main():
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

    s.enter(1, 1, tick, (j['serverURL'], j['authKey'], j['targetRPS']))        
    s.run()

if __name__ == "__main__":
    main()
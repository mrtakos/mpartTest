import asyncio
import json
import logging
import requests
import sched
import time
from threading import Timer

logging.basicConfig()
logger = logging.getLogger(__name__)

async def fire(url, key):
    ''' Hits the API
    '''
    headers = {
        "X-Api-Key": key,
        "Content-Type": "application/json",
    }
    requests.get(url=url,headers=headers)

def tick(url, key, rps):
    ''' runs every second
    '''
    for i in range(rps):
        fire(url,key) 

class RepeatedTimer(object):
    ''' Scheduler
    '''
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


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
        jobs = json.loads(content)
    except Exception as e:
        logger.error(e)

    for j in jobs:
        duration = int(j['durationSec'])
        rt = RepeatedTimer(1, tick, j['serverURL'], j['authKey'], j['targetRPS'])
        try:
            time.sleep(duration) # your long-running job goes here...
        finally:
            rt.stop()

if __name__ == "__main__":
    main()
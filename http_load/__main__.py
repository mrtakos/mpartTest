import json
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)

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

        for i in range(duration):
            print(j['targetRPS'])

if __name__ == "__main__":
    main()
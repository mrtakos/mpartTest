# mParticle | Senior Site Reliability Engineer (SRE)

## How to run

### command
    python3 -m http_load
### output
    time: 2021-06-10T04:51:40 target: 2 actual: 2
    time: 2021-06-10T04:51:42 target: 2 actual: 2
    time: 2021-06-10T04:51:43 target: 2 actual: 2
    ^C{"200": 5, "success": 6, "fail": 0, "301": 1}

## ASSIGNMENT:

Hello Michael,

We would like you to solve the following problem and commit your code as it progresses to a git repo you can provide us access to.  We normally allow 3 days for this project but if you require additional time due to prior commitments we are happy to work with you.

## PROBLEM:
As a company that runs HTTP services, questions of scale often come up. When you want to determine how a service will scale
before turning it loose in the wild, it's often prudent to run a load test to simulate your expected traffic. A good load 
generator should be able to provide ample RPS (requests per second) to help drive out potential performance problems before
any of your new users see them - the higher the better.

We would like you to construct a simple HTTP load generator using modern C#, python, or C++ async practices. It should accept an input file
specifying details like hostname, path, and requests per second, and then generate the requested load until the program
has been shut down. It should also handle/report on any obviously erroneous behavior from the server.
This task should be time-boxed at somewhere around 2 hours; we are not expecting a world-class application, but merely
would like to get to know you better as a developer through your code. 

## DETAILS:
* Server URL: https://c1i55mxsd6.execute-api.us-west-2.amazonaws.com/Live
* Permissions (in Header): 'X-Api-Key: RIqhxTAKNGaSw2waOY2CW3LhLny2EpI27i56VA6N'
* Expected Request Payload (in JSON): { "name": "YOUR_NAME", "date": "NOW_IN_UTC", "requests_sent": REQUESTS_THIS_SESSION }
* Expected Response Payload (in JSON): { "successful": true }
 
## REQUIREMENTS:
* Program must accept file-based input for: serverURL, targetRPS, authKey. Additional parameters may be added as desired for your clarity and ease of use.
* Program must send up valid request body payload.
* Program must sanely handle typical HTTP server responses.
* Program must output to the console the current RPS and target RPS.
* After the run has completed, program must output a summary of run including relevant request/response metrics.
* Your API key is limited to 100,000 requests. Please contact us if you need that limit raised for any reason.
* Program must be submitted via a git repo, and we will want to see commit history
 
## SUBMISSION:
We will review at the end of the interviewing session, and talk through design decisions and tradeoffs.

Please let us know if you have any questions.


Evan Furman

mParticle

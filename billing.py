#!/usr/bin/env python3
# from base64 import b64encode
from base64 import b64encode
from formant.sdk.agent.v1 import Client as FormantClient
import time
import concurrent.futures
import multiprocessing
from multiprocessing import Value
import sys
import os

# Maximum ingestion throttle is 20 Hz
hz = 20

# Prepare text
random_string = b64encode(os.urandom(1337)).decode("utf-8")

fclient = FormantClient(
    ignore_throttled=True, ignore_unavailable=True, agent_url="localhost:5501"
)

agent_id = fclient.get_agent_id()
print({agent_id})

def post_text(stream_name, shared_value):
    # experimental size is roughly 7150
    for i in range(hz):
        message = b64encode(os.urandom(1337)).decode("utf-8")
        fclient.post_text(stream_name, message)
        shared_value.value += 1
        time.sleep(0.05)


def post_concurrently(stream_names, num_calls):
    shared_value = Value("i", 0)
    posted_bytes = 0
    target_datapoints = 1320000
    posted_datapoints = 0
    datapoints_per_round = num_calls * hz
    bytes_per_round = datapoints_per_round * 1000

    while posted_datapoints < target_datapoints:
        start = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_calls) as executor:
            for stream_name in stream_names:
                executor.submit(post_text, stream_name, shared_value)
        posted_datapoints += datapoints_per_round
        posted_bytes += bytes_per_round
        if time.time() - start < 1:
            time.sleep(1 - (time.time() - start))
        print("currently ingested", 2 * shared_value.value, end="\r")


if __name__ == "__main__":
    print("Starting the ingestion....")
    
    text_bytes = 0
    num_calls = 60
    # posted_datapoint = 0

    num_calls1 = num_calls / 2
    # Define the list of streamnames
    stream_names = [f"billing{i}.text.test" for i in range(num_calls)]

    time.sleep(300)
    post_concurrently(stream_names, num_calls)

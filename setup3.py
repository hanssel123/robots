#!/usr/bin/env python3
import time
import random
import numpy as np
from formant.sdk.agent.v1 import Client as FormantClient
if __name__ == "__main__":
    print("Starting the ingestion....")
    fclient = FormantClient(
        ignore_throttled=True,
        ignore_unavailable=True
    )
    status = {"Online": True, "Button toggled": False}
    def handle_teleop(control_datapoint):
        if control_datapoint.stream == "Buttons":
            if (str(control_datapoint.bitset.bits[0]).find("true") != -1):
                status["Button toggled"] = not (status["Button toggled"])
    fclient.register_teleop_callback(handle_teleop, ["Buttons"])
    #  Ingest all datapoint
    def post_random_geolocation_data():
        dec_lat = random.random()/100
        dec_lon = random.random()/100
        fclient.post_geolocation("example.geolocation",  22.835+dec_lat, 33.631667 +
                                 dec_lon)  # lat, long
    def post_random_text_data():
        hex1 = '%012x' % random.randrange(16**12)  # 12 char random string
        fclient.post_text("example.text", "Hanssel")
    def triangular(inf, sup, num):
        if num <= (inf + sup) // 2:
            return num
        else:
            return inf + sup - num
    # def post_random_numeric_data():
    #     fclient.post_numeric("example.numeric", float(random.randint(0, 100)))
    def post_random_numericset_data():
        fclient.post_numericset(
            "example.numericset",
            {
                "frequency": (random.randint(70, 999), "Hz"),
                "usage": (random.randint(0, 100), "percent"),
                "warp factor": (float(random.randint(0, 100)), None),
            },
        )
   
    def post_status():
        fclient.post_bitset(
            "Status",
            status,
        )

    def post_bitset():
        fclient.post_bitset(
        "example.bitset", {"standing": True,
                           "walking": True, "sitting": True}
        )
        
    while True:
        post_status()
        post_bitset()
        post_random_geolocation_data()
        post_random_text_data()
        for i in range(1, 21):
            value = triangular(1, 20, i)
            fclient.post_numeric("example.numeric", value)
            time.sleep(2)
        post_random_numericset_data()
        time.sleep(10)